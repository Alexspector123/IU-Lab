# lab8_gui.py
import math
import sys
import time

import pygame

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QCheckBox,
    QFormLayout,
    QSpinBox,
    QSplitter,
    QComboBox,
)
from PySide6.QtOpenGL import QOpenGLWindow

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
)

from city_engine import CityEngine

# ------------------------------------------------------------
# Global OpenGL configuration (must be called before QApplication)
# ------------------------------------------------------------
def configure_opengl():
    """
    Request an OpenGL 3.3 Core profile so that GLSL #version 330
    shaders in py3d materials will compile correctly.
    """
    fmt = QSurfaceFormat()
    fmt.setRenderableType(QSurfaceFormat.OpenGL)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setVersion(3, 3)
    fmt.setDepthBufferSize(24)
    fmt.setStencilBufferSize(8)
    fmt.setSwapInterval(1)  # vsync

    QSurfaceFormat.setDefaultFormat(fmt)


# ------------------------------------------------------------
# OpenGL window that hosts the CityEngine
# ------------------------------------------------------------
class CityGLWindow(QOpenGLWindow):
    """
    A QOpenGLWindow that owns a CityEngine instance.

    pygame is *not* used for a real window. We just patch
    pygame.display.get_surface() so Renderer() can query the size.
    """

    def __init__(self, detail: float = 1.0, shadows: bool = True, parent=None):
        super().__init__(parent)
        self.engine = None
        self.auto_tour = False

        # high-level parameters
        self.detail = float(detail)
        self.use_shadows = bool(shadows)

        # engine & timing
        self.engine: CityEngine | None = None
        self.last_time: float | None = None
        self.paused: bool = False
        self.view_mode: str = "main"  # "main" or "sky"

        # pygame init for TextTexture
        if not pygame.get_init():
            pygame.init()
        if not pygame.font.get_init():
            pygame.font.init()

        # patch pygame display API so Renderer() can query window size
        self._pygame_patched = False
        self._patch_pygame_display()

        # timer to drive simulation & repaint
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._on_tick)
        self.timer.start(16)  # ~60 FPS

    # --------------------------------------------------------
    # pygame <-> Qt bridge
    # --------------------------------------------------------
    def _patch_pygame_display(self):
        """
        Make pygame.display.get_surface() return a dummy object
        whose get_size() is this QOpenGLWindow's *physical* size
        (logical size × devicePixelRatio).
        """
        if self._pygame_patched:
            return

        window = self

        class DummySurface:
            def get_size(self_inner):
                dpr = window.devicePixelRatio()
                w = max(1, int(window.width() * dpr))
                h = max(1, int(window.height() * dpr))
                return (w, h)

        def _get_surface():
            return DummySurface()

        def _set_mode(*args, **kwargs):
            # If any code calls pygame.display.set_mode, just return dummy
            return _get_surface()

        def _flip():
            # Qt handles buffer swapping
            return None

        pygame.display.get_surface = _get_surface
        pygame.display.set_mode = _set_mode
        pygame.display.flip = _flip

        self._pygame_patched = True

    # ------------- public API for the control panel -------------

    def set_paused(self, value: bool):
        self.paused = bool(value)

    def set_view_mode(self, mode: str):
        if mode in ("main", "sky"):
            self.view_mode = mode

    def reset_camera(self):
        """Reset camera rig to default position/view."""
        if self.engine is None:
            return
        print("Camera reset")
        self.engine.rig.set_position([0, 12, 45])
        self.engine.camera.look_at([0, 0, 0])

    def set_traffic_cycle(self, seconds: float):
        if self.engine is not None:
            self.engine.traffic_cycle = float(seconds)

    def rebuild_scene(self, detail: float | None = None, shadows: bool | None = None):
        """
        Recreate the CityEngine with new parameters.
        """
        if detail is not None:
            self.detail = float(detail)
        if shadows is not None:
            self.use_shadows = bool(shadows)

        self._patch_pygame_display()

        if self.context() is None:
            # GL not ready yet; engine will be created in initializeGL()
            return

        self.makeCurrent()
        dpr = self.devicePixelRatio()
        w = max(1, int(self.width() * dpr))
        h = max(1, int(self.height() * dpr))
        aspect = w / h

        self.engine = CityEngine(
            aspect_ratio=aspect,
            detail=self.detail,
            shadows=self.use_shadows,
        )
        # sync renderer window size with physical size
        self.engine.renderer._window_size = (w, h)

        self.last_time = time.perf_counter()
        self.doneCurrent()

    # ------------- QOpenGLWindow overrides -------------

    def initializeGL(self):
        self._patch_pygame_display()

        dpr = self.devicePixelRatio()
        w = max(1, int(self.width() * dpr))
        h = max(1, int(self.height() * dpr))
        aspect = w / h

        self.engine = CityEngine(
            aspect_ratio=aspect,
            detail=self.detail,
            shadows=self.use_shadows,
        )
        self.engine.renderer._window_size = (w, h)
        self.last_time = time.perf_counter()

        # debug: print GL info
        try:
            from OpenGL import GL

            version = GL.glGetString(GL.GL_VERSION)
            renderer = GL.glGetString(GL.GL_RENDERER)
            print("OpenGL Version:", version)
            print("OpenGL Renderer:", renderer)
        except Exception:
            pass

    def resizeGL(self, w: int, h: int):
        if self.engine is None or h <= 0:
            return

        # w, h are logical; GL framebuffer is physical
        dpr = self.devicePixelRatio()
        phys_w = max(1, int(w * dpr))
        phys_h = max(1, int(h * dpr))
        aspect = phys_w / phys_h

        # update cameras
        self.engine.camera.aspect_ratio = aspect
        self.engine.sky_camera.aspect_ratio = 1.0  # keep top view square

        # update renderer size to physical size (for glViewport)
        self.engine.renderer._window_size = (phys_w, phys_h)

    def paintGL(self):
        if self.engine is None:
            return

        if self.view_mode == "sky":
            self.engine.render_sky()
        else:
            self.engine.render_main()


    def toggle_tour(self, checked):
        self.auto_tour = checked
        if checked:
            self._tour_start_time = self.engine.time
            print("Tour started")
        else:
            self.reset_camera()
            print("Tour stopped")

    # ------------- simulation ticking -------------

    def _on_tick(self):
        if self.engine is None:
            return

        now = time.perf_counter()
        dt = now- self.last_time if self.last_time is not None else 0.0
        self.last_time = now

        self.engine.step(dt, input_state=None)

        if self.auto_tour:
            t = self.engine.time
            radius = 60.0

            x = radius * math.cos(0.1 * t)
            z = radius * math.sin(0.1 * t)

            self.engine.rig.set_position([x, 20, z])
            self.engine.camera.look_at([0, 0, 0])
        self.update()
    
    def set_view_front(self):
        if self.engine is None:
            return
        self.engine.rig.set_position([0, 12, 45])
        self.engine.camera.look_at([0, 0, 0])
        self.update()

    def set_view_left(self):
        if self.engine is None:
            return
        self.engine.rig.set_position([-45, 12, 0])
        self.engine.camera.look_at([0, 0, 0])
        self.update()

    def set_view_top(self):
        if self.engine is None:
            return
        self.engine.rig.set_position([0, 80, 0])
        self.engine.camera.look_at([0, 0, 0])
        self.update()
    
    def move_camera(self, dx=0.0, dy=0.0, dz=0.0):
        if self.engine is None:
            return
        
        pos = list(self.engine.rig.global_position)
        pos[0] += dx
        pos[1] += dy
        pos[2] += dz
        self.engine.rig.set_position(pos)


# ------------------------------------------------------------
# Control panel on the left
# ------------------------------------------------------------
class ControlPanel(QWidget):
    def __init__(self, gl_window: CityGLWindow, parent=None):
        super().__init__(parent)
        self.gl_window = gl_window

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(10)

        # --- Camera Presets ---
        group = QGroupBox("Camera presets")
        h = QHBoxLayout()

        self.btn_view_front = QPushButton("Front view")
        self.btn_view_left = QPushButton("Left view")
        self.btn_view_top = QPushButton("Top view")

        h.addWidget(self.btn_view_front)
        h.addWidget(self.btn_view_left)
        h.addWidget(self.btn_view_top)

        group.setLayout(h)
        layout.addWidget(group)

        self.btn_view_front.clicked.connect(self.gl_window.set_view_front)
        self.btn_view_left.clicked.connect(self.gl_window.set_view_left)
        self.btn_view_top.clicked.connect(self.gl_window.set_view_top)

        # --- Camera Movement ---
        self.btn_forward = QPushButton("Forward")
        self.btn_backward = QPushButton("Backward")
        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        layout.addWidget(QLabel("Camera Movement"))
        layout.addWidget(self.btn_forward)
        layout.addWidget(self.btn_backward)
        layout.addWidget(self.btn_left)
        layout.addWidget(self.btn_right)

        self.btn_forward.clicked.connect(
            lambda: self.gl_window.move_camera(0, 0, -5)
        )
        self.btn_backward.clicked.connect(
            lambda: self.gl_window.move_camera(0, 0, 5)
        )
        self.btn_left.clicked.connect(
            lambda: self.gl_window.move_camera(-5, 0, 0)
        )
        self.btn_right.clicked.connect(
            lambda: self.gl_window.move_camera(5, 0, 0)
        )

        # --- Tour button ---
        self.btn_tour = QPushButton("Start Tour")
        self.btn_tour.setCheckable(True)
        self.btn_tour.toggled.connect(self.gl_window.toggle_tour)
        layout.addWidget(QLabel("Camera Tour"))
        layout.addWidget(self.btn_tour)

        title = QLabel("City Controls")
        title.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)

        # Detail slider: 0.1 -> 1.0
        self.detail_slider = QSlider(Qt.Horizontal)
        self.detail_slider.setMinimum(1)
        self.detail_slider.setMaximum(10)
        self.detail_slider.setValue(int(gl_window.detail * 10))
        self.detail_slider.setTickPosition(QSlider.TicksBelow)
        self.detail_slider.setTickInterval(1)
        form.addRow("Detail (0.1 - 1.0):", self.detail_slider)

        # Shadows
        self.shadow_check = QCheckBox("Enable shadows")
        self.shadow_check.setChecked(gl_window.use_shadows)
        form.addRow("Shadows:", self.shadow_check)

        # Traffic cycle
        self.traffic_spin = QSpinBox()
        self.traffic_spin.setMinimum(4)
        self.traffic_spin.setMaximum(60)
        self.traffic_spin.setValue(14)
        form.addRow("Traffic cycle (s):", self.traffic_spin)

        # View mode
        self.view_combo = QComboBox()
        self.view_combo.addItems(["Main camera", "Top-down sky view"])
        form.addRow("View:", self.view_combo)

        layout.addLayout(form)

        # Pause
        self.pause_check = QCheckBox("Pause simulation")
        self.pause_check.stateChanged.connect(
            lambda state: self.gl_window.set_paused(state == Qt.Checked)
        )
        layout.addWidget(self.pause_check)

        # Buttons
        btn_row = QHBoxLayout()
        self.apply_btn = QPushButton("Rebuild Scene")
        self.apply_btn.clicked.connect(self.on_apply_clicked)
        btn_row.addWidget(self.apply_btn)

        self.reset_cam_btn = QPushButton("Reset Camera")
        self.reset_cam_btn.clicked.connect(self.gl_window.reset_camera)
        btn_row.addWidget(self.reset_cam_btn)

        layout.addLayout(btn_row)

        # View change signal
        self.view_combo.currentIndexChanged.connect(self.on_view_changed)

        layout.addStretch(1)

    def on_apply_clicked(self):
        detail = max(0.1, min(1.0, self.detail_slider.value() / 10.0))
        shadows = self.shadow_check.isChecked()

        self.gl_window.rebuild_scene(detail=detail, shadows=shadows)
        self.gl_window.set_traffic_cycle(self.traffic_spin.value())

    def on_view_changed(self, index: int):
        if index == 0:
            self.gl_window.set_view_mode("main")
        else:
            self.gl_window.set_view_mode("sky")


# ------------------------------------------------------------
# Main window with splitter: [ControlPanel | GL view]
# ------------------------------------------------------------
class CityMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("City Simulation (PySide6 + py3d)")

        splitter = QSplitter(Qt.Horizontal)

        # Right: OpenGL window embedded into a QWidget container
        self.gl_window = CityGLWindow(detail=1.0, shadows=True)
        gl_container = QWidget.createWindowContainer(self.gl_window, self)
        gl_container.setMinimumSize(640, 480)

        # Left: controls
        self.control_panel = ControlPanel(self.gl_window)

        splitter.addWidget(self.control_panel)
        splitter.addWidget(gl_container)

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        central = QWidget()
        layout = QHBoxLayout(central)
        layout.addWidget(splitter)
        central.setLayout(layout)

        self.setCentralWidget(central)
        self.resize(1200, 720)


# ------------------------------------------------------------
# main
# ------------------------------------------------------------
def main():
    configure_opengl()
    app = QApplication(sys.argv)
    win = CityMainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
