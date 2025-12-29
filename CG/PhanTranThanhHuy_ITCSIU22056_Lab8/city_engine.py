# city_engine.py
import math
import random

from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.core_ext.object3d import Object3D

from py3d.geometry.box import BoxGeometry
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry

from py3d.material.texture import TextureMaterial
from py3d.material.phong import PhongMaterial
from py3d.material.material import Material

from py3d.light.ambient import AmbientLight
from py3d.light.directional import DirectionalLight

from py3d.extras.movement_rig import MovementRig
from py3d.extras.text_texture import TextTexture


# ---------------------------------------------------------
# Wrapper: Phong + shadows, filter unsupported keys
# ---------------------------------------------------------
class SurfaceMaterial(PhongMaterial):
    """Phong material with shadows, stripping unsupported keys."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("number_of_light_sources", 2)  # ambient + sun
        kwargs.setdefault("use_shadow", True)

        pd = kwargs.get("property_dict")
        if pd is not None:
            pd = dict(pd)
            pd.pop("specularColor", None)
            pd.pop("shininess", None)
            kwargs["property_dict"] = pd

        super().__init__(*args, **kwargs)


class CityEngine:
    """
    City simulation + rendering engine.

    - Owns Scene, Renderer, Cameras, lights, vehicles, pedestrians, etc.
    - Does NOT own window / main loop.
    - GUI code is responsible for:
        * calling engine.step(dt, input_state)
        * calling engine.render_main() (or render_sky()) each frame.
    """

    def __init__(self, aspect_ratio=4.0 / 3.0, detail: float = 1.0, shadows: bool = True):
        self.aspect_ratio = aspect_ratio
        self.detail = max(0.1, float(detail))
        self.use_shadows = bool(shadows)

        # engine time accumulator (independent from Base)
        self.time = 0.0

        # State containers
        self.vehicles = []
        self.pedestrians = []
        self.ns_red_bulbs = []
        self.ns_green_bulbs = []
        self.ew_red_bulbs = []
        self.ew_green_bulbs = []

        # Core py3d objects
        self.renderer = Renderer()
        self.scene = Scene()

        # Cameras
        self.camera = Camera(aspect_ratio=self.aspect_ratio)
        self.rig = MovementRig(units_per_second=12)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 12, 45])
        self.camera.look_at([0, 0, 0])

        self.sky_camera = Camera(aspect_ratio=1.0)
        self.sky_camera.set_position([0, 80, 0])
        self.sky_camera.look_at([0, 0, 0])
        self.scene.add(self.sky_camera)

        # Lighting
        self.ambient_light = AmbientLight(color=[0.3, 0.3, 0.35])
        self.scene.add(self.ambient_light)

        self.sun_light = DirectionalLight(
            color=[1.0, 1.0, 0.9],
            direction=[-1, -1, -1],
        )
        self.scene.add(self.sun_light)

        if self.use_shadows:
            self.renderer.enable_shadows(self.sun_light, strength=0.85)

        # Traffic light cycle
        self.traffic_cycle = 14.0         # seconds per cycle
        self.traffic_ns_green_time = 7.0  # first half NS green, second half EW green

        # Road/crosswalk info
        self.road_width = 8.0
        self.road_height = 0.04
        self.crosswalk_width = 2.0
        self.road_x = []
        self.road_z = []
        self.intersections = []

        # Build everything
        self._build_world()

    # ==========================================================
    # World construction (from your original initialize())
    # ==========================================================
    def _build_world(self):
        random.seed(1)
        city_half = 100.0

        # Sky
        sky = Mesh(
            SphereGeometry(200),
            TextureMaterial(Texture(file_name="textures/sky.jpg")),
        )
        self.scene.add(sky)

        # Ground
        ground_material = PhongMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            number_of_light_sources=2,
            use_shadow=True,
        )
        ground = Mesh(
            RectangleGeometry(2 * city_half, 2 * city_half),
            ground_material,
        )
        ground.rotate_x(-math.pi / 2)
        ground.set_position([0, 0, 0])
        self.scene.add(ground)

        # Sun sphere (visual only)
        sun_geom = SphereGeometry(radius=3.0)
        vs_code = """
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        in vec3 vertexPosition;
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix
                          * vec4(vertexPosition, 1.0);
        }
        """
        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 0.9, 0.0, 1.0);
        }
        """
        sun_mat = Material(vs_code, fs_code)
        sun_mat.locate_uniforms()
        self.sun = Mesh(sun_geom, sun_mat)
        self.sun.set_position([0, 60, 0])
        self.scene.add(self.sun)

        # Label
        label_tex = TextTexture(
            text="City / Village Scene",
            system_font_name="Arial Bold",
            font_size=72,
            font_color=[1, 1, 1],
            image_width=1024,
            image_height=128,
            align_horizontal=0.5,
            align_vertical=0.5,
            image_border_width=4,
            image_border_color=[0, 0, 0],
        )
        self.label = Mesh(
            RectangleGeometry(6.0, 0.7),
            TextureMaterial(label_tex),
        )
        self.label.set_position([0, 18, -15])
        self.scene.add(self.label)

        # ========= Roads =========
        road_color = [0.12, 0.12, 0.12]

        # Road centers
        self.road_x = [-60, -30, 0, 30, 60]
        self.road_z = [-60, -30, 0, 30, 60]

        # North–south roads
        for x in self.road_x:
            road = Mesh(
                BoxGeometry(self.road_width, self.road_height, 2 * city_half),
                SurfaceMaterial(property_dict={"baseColor": road_color}),
            )
            road.set_position([x, self.road_height / 2, 0])
            self.scene.add(road)

        # East–west roads
        for z in self.road_z:
            road = Mesh(
                BoxGeometry(2 * city_half, self.road_height, self.road_width),
                SurfaceMaterial(property_dict={"baseColor": road_color}),
            )
            road.set_position([0, self.road_height / 2, z])
            self.scene.add(road)

        # Intersections
        self.intersections = [(rx, rz) for rx in self.road_x for rz in self.road_z]

        # Central plaza
        plaza = Mesh(
            BoxGeometry(18, 0.05, 18),
            SurfaceMaterial(property_dict={"baseColor": [0.32, 0.32, 0.35]}),
        )
        plaza.set_position([0, 0.05 / 2, 0])
        self.scene.add(plaza)

        # ---- Crosswalks at every intersection ----
        cw_w = self.crosswalk_width
        cw_len = self.road_width - 1.5
        zebra_mat = SurfaceMaterial(property_dict={"baseColor": [0.92, 0.92, 0.92]})

        for ix, iz in self.intersections:
            # across north–south road: west & east sides
            cw = Mesh(RectangleGeometry(cw_w, cw_len), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix - self.road_width / 2 - cw_w / 2, 0.051, iz])
            self.scene.add(cw)

            cw = Mesh(RectangleGeometry(cw_w, cw_len), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix + self.road_width / 2 + cw_w / 2, 0.051, iz])
            self.scene.add(cw)

            # across east–west road: south & north sides
            cw = Mesh(RectangleGeometry(cw_len, cw_w), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix, 0.051, iz - self.road_width / 2 - cw_w / 2])
            self.scene.add(cw)

            cw = Mesh(RectangleGeometry(cw_len, cw_w), zebra_mat)
            cw.rotate_x(-math.pi / 2)
            cw.set_position([ix, 0.051, iz + self.road_width / 2 + cw_w / 2])
            self.scene.add(cw)

        # ---- Lane markings for all roads (center dashed line) ----
        mark_mat = SurfaceMaterial(property_dict={"baseColor": [0.9, 0.9, 0.9]})
        # along every east–west road
        for z in self.road_z:
            for x in range(-90, 91, 8):
                dash = Mesh(RectangleGeometry(2.0, 0.4), mark_mat)
                dash.rotate_x(-math.pi / 2)
                dash.set_position([x, 0.051, z])
                self.scene.add(dash)
        # along every north–south road
        for x in self.road_x:
            for z in range(-90, 91, 8):
                dash = Mesh(RectangleGeometry(0.4, 2.0), mark_mat)
                dash.rotate_x(-math.pi / 2)
                dash.set_position([x, 0.051, z])
                self.scene.add(dash)

        # Traffic lights only at central intersection
        self.build_traffic_lights()

        # ========= Buildings per land plot (block) =========
        road_half = self.road_width / 2.0

        for i in range(len(self.road_x) - 1):
            rx0 = self.road_x[i]
            rx1 = self.road_x[i + 1]

            plot_xmin = rx0 + road_half
            plot_xmax = rx1 - road_half
            if plot_xmin >= plot_xmax:
                continue
            plot_w = plot_xmax - plot_xmin

            for j in range(len(self.road_z) - 1):
                rz0 = self.road_z[j]
                rz1 = self.road_z[j + 1]

                plot_zmin = rz0 + road_half
                plot_zmax = rz1 - road_half
                if plot_zmin >= plot_zmax:
                    continue
                plot_d = plot_zmax - plot_zmin

                # choose grid resolution for this block (2×2 or 3×2)
                grid_nx = 3 if plot_w > 25 else 2
                grid_nz = 3 if plot_d > 25 else 2

                cell_w = plot_w / grid_nx
                cell_d = plot_d / grid_nz

                for gx in range(grid_nx):
                    for gz in range(grid_nz):
                        # center of this cell
                        cx = plot_xmin + (gx + 0.5) * cell_w
                        cz = plot_zmin + (gz + 0.5) * cell_d

                        # jitter
                        jitter_x = (random.random() - 0.5) * 0.3 * cell_w
                        jitter_z = (random.random() - 0.5) * 0.3 * cell_d
                        cx += jitter_x
                        cz += jitter_z

                        dist = math.sqrt(cx * cx + cz * cz)

                        # leave some empty cells
                        if random.random() < 0.12:
                            continue

                        btype = self.pick_building_type(dist)

                        if btype == "skyscraper":
                            self.make_skyscraper(cx, cz, cell_w, cell_d)
                        elif btype == "apartment":
                            self.make_apartment(cx, cz, cell_w, cell_d)
                        else:
                            self.make_house(cx, cz, cell_w, cell_d)

        # ========= Trees along roads (boulevards) =========
        tree_offset = self.road_width / 2 + 1.6
        clear_margin = self.road_width  # no trees close to any intersection

        # along E–W roads
        for z in self.road_z:
            for x in range(-80, 81, 10):
                for sign in (+1, -1):
                    tx = x
                    tz = z + sign * tree_offset
                    if self.is_near_intersection(tx, tz, clear_margin):
                        continue
                    self.make_tree(tx, tz, small=True)

        # along N–S roads
        for x in self.road_x:
            for z in range(-80, 81, 10):
                for sign in (+1, -1):
                    tx = x + sign * tree_offset
                    tz = z
                    if self.is_near_intersection(tx, tz, clear_margin):
                        continue
                    self.make_tree(tx, tz, small=True)

        # ========= Vehicles & Pedestrians =========
        self.init_vehicles()
        self.init_pedestrians()

    # ==========================================================
    # Simulation step + rendering entry points
    # ==========================================================
    def step(self, dt: float, input_state=None):
        """
        Advance simulation by dt seconds.

        - dt: time since last step (from GUI / main loop)
        - input_state: py3d Input object (or None) for MovementRig camera control
        """
        # accumulate absolute time (for sun + traffic cycle)
        self.time += dt

        # Rotate label a bit
        self.label.rotate_y(0.2 * dt)

        # ---------- Sun movement ----------
        day_speed = 0.08
        theta = (self.time * day_speed) % math.pi

        sun_x = 120.0 * math.cos(theta)          # east (+x) -> west (-x)
        sun_y = 10.0 + 70.0 * math.sin(theta)   # low at horizon, high at midday
        sun_z = -60.0                           # fixed z

        self.sun.set_position([sun_x, sun_y, sun_z])

        # Direction of sun light
        target = [0.0, 0.0, 0.0]
        dir_x = target[0] - sun_x
        dir_y = target[1] - sun_y
        dir_z = target[2] - sun_z
        self.sun_light.set_direction([dir_x, dir_y, dir_z])

        # ---------- Traffic light state ----------
        cycle = self.time % self.traffic_cycle
        ns_green = cycle < self.traffic_ns_green_time
        ew_green = not ns_green

        red_on = [1.0, 0.1, 0.1]
        red_off = [0.2, 0.0, 0.0]
        green_on = [0.2, 1.0, 0.2]
        green_off = [0.0, 0.2, 0.0]

        for m in self.ns_red_bulbs:
            m.material.set_properties(
                {"baseColor": red_on if not ns_green else red_off}
            )
        for m in self.ns_green_bulbs:
            m.material.set_properties(
                {"baseColor": green_on if ns_green else green_off}
            )
        for m in self.ew_red_bulbs:
            m.material.set_properties(
                {"baseColor": red_on if not ew_green else red_off}
            )
        for m in self.ew_green_bulbs:
            m.material.set_properties(
                {"baseColor": green_on if ew_green else green_off}
            )

        # ---------- Camera, vehicles, pedestrians ----------
        smoothed_dt = min(dt, 0.033)  # max step ≈ 1/30 s
        self.update_vehicles(smoothed_dt, ns_green, ew_green)
        self.update_pedestrians(smoothed_dt)

        if input_state is not None:
            self.rig.update(input_state, smoothed_dt)

    def render_main(self):
        """Render scene from the main camera."""
        self.renderer.render(self.scene, self.camera)

    def render_sky(self):
        """Render scene from the top-down sky camera."""
        self.renderer.render(self.scene, self.sky_camera)

    # ==========================================================
    # --- Helpers copied from your original Example class ------
    # ==========================================================
    # ---------- helper: trees ----------
    def make_tree(self, x, z, small=False):
        trunk_h = 0.9 if small else 1.2
        crown_r = 0.6 if small else 0.8

        trunk = Mesh(
            BoxGeometry(0.25, trunk_h, 0.25),
            SurfaceMaterial(property_dict={"baseColor": [0.45, 0.28, 0.15]}),
        )
        trunk.set_position([x, trunk_h / 2, z])
        self.scene.add(trunk)

        crown = Mesh(
            SphereGeometry(crown_r),
            SurfaceMaterial(property_dict={"baseColor": [0.15, 0.65, 0.15]}),
        )
        crown.set_position([x, trunk_h + crown_r * 0.7, z])
        self.scene.add(crown)

    # ---------- helper: building type picker ----------
    def pick_building_type(self, dist_from_center):
        if dist_from_center < 30:
            probs = (0.6, 0.3, 0.1)   # skyscraper, apartment, house
        elif dist_from_center < 70:
            probs = (0.25, 0.45, 0.30)
        else:
            probs = (0.05, 0.25, 0.70)

        r = random.random()
        if r < probs[0]:
            return "skyscraper"
        elif r < probs[0] + probs[1]:
            return "apartment"
        else:
            return "house"

    # ---------- helper: skyscraper ----------
    def make_skyscraper(self, cx, cz, cell_w, cell_d):
        floor_h = 0.8
        floors = random.randint(14, 22)
        total_h = floors * floor_h

        min_side = 0.6 * min(cell_w, cell_d)
        base_w = min_side
        base_d = min_side

        tower_root = Object3D()
        tower_root.set_position([cx, 0, cz])
        self.scene.add(tower_root)

        base_color = [
            0.35,
            0.4 + 0.1 * random.random(),
            0.6 + 0.15 * random.random(),
        ]

        # lower body
        seg1_h = total_h * 0.6
        seg1 = Mesh(
            BoxGeometry(base_w, seg1_h, base_d),
            SurfaceMaterial(property_dict={"baseColor": base_color}),
        )
        seg1.set_position([0, seg1_h / 2, 0])
        tower_root.add(seg1)

        # horizontal floor bands
        band_count = int(floors * 0.6)
        if band_count > 0:
            step = seg1_h / band_count
            band_thick = step * 0.12
            for k in range(2, band_count, 2):
                y = k * step
                band = Mesh(
                    BoxGeometry(base_w * 1.01, band_thick, base_d * 1.01),
                    SurfaceMaterial(property_dict={"baseColor": [0.25, 0.3, 0.35]}),
                )
                band.set_position([0, y, 0])
                tower_root.add(band)

        # upper body
        seg2_w = base_w * 0.7
        seg2_d = base_d * 0.7
        seg2_h = total_h * 0.3
        seg2_color = [c * 0.9 for c in base_color]
        seg2 = Mesh(
            BoxGeometry(seg2_w, seg2_h, seg2_d),
            SurfaceMaterial(property_dict={"baseColor": seg2_color}),
        )
        seg2.set_position([0, seg1_h + seg2_h / 2, 0])
        tower_root.add(seg2)

        # top volume / penthouse
        top_w = seg2_w * 0.5
        top_d = seg2_d * 0.5
        top_h = total_h * 0.1
        top_color = [min(1.0, c * 1.1) for c in base_color]
        top = Mesh(
            BoxGeometry(top_w, top_h, top_d),
            SurfaceMaterial(property_dict={"baseColor": top_color}),
        )
        top.set_position([0, seg1_h + seg2_h + top_h / 2, 0])
        tower_root.add(top)

    # ---------- helper: apartment ----------
    def make_apartment(self, cx, cz, cell_w, cell_d):
        floor_h = 0.7
        floors = random.randint(5, 9)
        h = floors * floor_h

        body_w = 0.7 * cell_w
        body_d = 0.55 * cell_d

        color = [0.7, 0.7 - 0.1 * random.random(), 0.65]
        body = Mesh(
            BoxGeometry(body_w, h, body_d),
            SurfaceMaterial(property_dict={"baseColor": color}),
        )
        body.set_position([cx, h / 2, cz])
        self.scene.add(body)

        roof = Mesh(
            BoxGeometry(body_w * 0.98, 0.2, body_d * 0.98),
            SurfaceMaterial(property_dict={"baseColor": [c * 0.9 for c in color]}),
        )
        roof.set_position([cx, h + 0.1, cz])
        self.scene.add(roof)

        # balconies front/back
        balcony_depth = 0.6
        balcony_h = 0.15
        balcony_color = [0.85, 0.85, 0.88]
        for sign in (-1, 1):
            balcony = Mesh(
                BoxGeometry(body_w * 0.75, balcony_h, balcony_depth),
                SurfaceMaterial(property_dict={"baseColor": balcony_color}),
            )
            balcony.set_position(
                [cx, h * 0.45, cz + sign * (body_d / 2 + balcony_depth / 2)]
            )
            self.scene.add(balcony)

        # front glass strips (fake windows)
        strip_w = 0.2 * body_w
        for sx in (-0.35, 0.35):
            strip = Mesh(
                BoxGeometry(strip_w, h * 0.9, 0.04),
                SurfaceMaterial(property_dict={"baseColor": [0.5, 0.6, 0.75]}),
            )
            strip.set_position([
                cx + sx * body_w,
                h * 0.55,
                cz + body_d / 2 + 0.02,
            ])
            self.scene.add(strip)

    # ---------- helper: house ----------
    def make_house(self, cx, cz, cell_w, cell_d):
        body_w = 0.6 * cell_w
        body_d = 0.55 * cell_d
        h = random.uniform(1.6, 2.3)

        body_color = random.choice([
            [0.9, 0.75, 0.65],
            [0.82, 0.82, 0.7],
            [0.78, 0.86, 0.93],
        ])
        body = Mesh(
            BoxGeometry(body_w, h, body_d),
            SurfaceMaterial(property_dict={"baseColor": body_color}),
        )
        body.set_position([cx, h / 2, cz])
        self.scene.add(body)

        roof_h = 0.5
        roof_color = [0.6, 0.15, 0.15]
        roof = Mesh(
            BoxGeometry(body_w * 1.05, roof_h, body_d * 1.05),
            SurfaceMaterial(property_dict={"baseColor": roof_color}),
        )
        roof.set_position([cx, h + roof_h / 2, cz])
        self.scene.add(roof)

        # simple front windows
        win_w = body_w * 0.18
        win_h = h * 0.3
        for sx in (-0.3, 0.3):
            win = Mesh(
                BoxGeometry(win_w, win_h, 0.03),
                SurfaceMaterial(property_dict={"baseColor": [0.6, 0.75, 0.9]}),
            )
            win.set_position([
                cx + sx * body_w * 0.6,
                h * 0.6,
                cz + body_d / 2 + 0.02,
            ])
            self.scene.add(win)

        # two little trees in the yard
        self.make_tree(cx + body_w * 0.6, cz + body_d * 0.2, small=True)
        self.make_tree(cx - body_w * 0.6, cz - body_d * 0.2, small=True)

    # ---------- helper: vehicles ----------
    def add_vehicle(self, axis, lane_coord, start_pos, direction=1, vtype=None):
        if vtype is None:
            vtype = random.choice(["car", "car", "car", "truck", "bus"])

        if vtype == "car":
            length, width, height = 4.0, 2.0, 1.2
            body_color = random.choice([
                [0.9, 0.1, 0.1],
                [0.1, 0.1, 0.9],
                [0.1, 0.6, 0.2],
                [0.9, 0.8, 0.1],
            ])
            roof_color = [c * 0.8 for c in body_color]
        elif vtype == "truck":
            length, width, height = 7.0, 2.5, 2.0
            body_color = [0.8, 0.8, 0.82]
            roof_color = [0.7, 0.7, 0.72]
        else:  # bus
            length, width, height = 9.0, 2.7, 2.5
            body_color = [0.9, 0.85, 0.2]
            roof_color = [0.95, 0.95, 0.85]

        root = Object3D()
        y = height / 2 + self.road_height / 2 + 0.02

        if axis == "x":
            root.set_position([start_pos, y, lane_coord])
        else:
            root.set_position([lane_coord, y, start_pos])

        self.scene.add(root)

        # body segments
        lower_h = height * 0.6
        upper_h = height * 0.4

        if axis == "x":
            lower_geom = BoxGeometry(length, lower_h, width)
            upper_geom = BoxGeometry(length * 0.6, upper_h, width * 0.9)
        else:
            lower_geom = BoxGeometry(width, lower_h, length)
            upper_geom = BoxGeometry(width * 0.9, upper_h, length * 0.6)

        lower = Mesh(
            lower_geom,
            SurfaceMaterial(property_dict={"baseColor": body_color}),
        )
        upper = Mesh(
            upper_geom,
            SurfaceMaterial(property_dict={"baseColor": roof_color}),
        )

        lower.set_position([0.0, lower_h / 2, 0.0])
        upper.set_position([0.0, lower_h + upper_h / 2, 0.0])

        root.add(lower)
        root.add(upper)

        self.vehicles.append({
            "axis": axis,
            "lane": lane_coord,
            "pos": start_pos,
            "dir": direction,
            "speed": random.uniform(7.0, 11.0),
            "y": y,
            "node": root,
        })

    def init_vehicles(self):
        self.vehicles = []

        # central east–west road (z = 0)
        z_main = 0.0
        lane_offset = 1.8

        # eastbound: left -> right
        for offset in (-60, -30, 0):
            self.add_vehicle(
                axis="x",
                lane_coord=z_main - lane_offset,
                start_pos=-80.0 + offset,
                direction=1,
            )

        # westbound: right -> left
        for offset in (0, 30, 60):
            self.add_vehicle(
                axis="x",
                lane_coord=z_main + lane_offset,
                start_pos=80.0 - offset,
                direction=-1,
            )

        # central north–south road (x = 0)
        x_main = 0.0
        lane_offset = 1.8

        # southbound: -z -> +z
        for offset in (-60, -30, 0):
            self.add_vehicle(
                axis="z",
                lane_coord=x_main - lane_offset,
                start_pos=-80.0 + offset,
                direction=1,
            )

        # northbound: +z -> -z
        for offset in (0, 30, 60):
            self.add_vehicle(
                axis="z",
                lane_coord=x_main + lane_offset,
                start_pos=80.0 - offset,
                direction=-1,
            )

    # ---------- helper: pedestrians ----------
    def add_pedestrian(self, axis, lane_coord, start_pos, direction=1):
        root = Object3D()
        if axis == "x":
            root.set_position([start_pos, 0.0, lane_coord])
        else:
            root.set_position([lane_coord, 0.0, start_pos])
        self.scene.add(root)

        body_h = 1.1
        body = Mesh(
            BoxGeometry(0.4, body_h, 0.3),
            SurfaceMaterial(property_dict={"baseColor": [0.2, 0.3, 0.7]}),
        )
        body.set_position([0.0, body_h / 2, 0.0])
        root.add(body)

        head = Mesh(
            SphereGeometry(0.25),
            SurfaceMaterial(property_dict={"baseColor": [0.95, 0.8, 0.6]}),
        )
        head.set_position([0.0, body_h + 0.25, 0.0])
        root.add(head)

        self.pedestrians.append({
            "axis": axis,
            "lane": lane_coord,
            "pos": start_pos,
            "dir": direction,
            "speed": random.uniform(1.0, 1.8),
            "node": root,
        })

    def init_pedestrians(self):
        self.pedestrians = []
        sidewalk_offset = self.road_width / 2 + 0.9

        # along each east–west road: people walking east/west
        for z in self.road_z:
            for offset in (-70, -30, 10, 50):
                self.add_pedestrian("x", z - sidewalk_offset, offset, direction=1)
                self.add_pedestrian("x", z + sidewalk_offset, -offset, direction=-1)

        # along each north–south road: people walking north/south
        for x in self.road_x:
            for offset in (-70, -30, 10, 50):
                self.add_pedestrian("z", x - sidewalk_offset, offset, direction=1)
                self.add_pedestrian("z", x + sidewalk_offset, -offset, direction=-1)

    # ---------- helper: traffic lights ----------
    def build_traffic_lights(self):
        self.ns_red_bulbs = []
        self.ns_green_bulbs = []
        self.ew_red_bulbs = []
        self.ew_green_bulbs = []

        post_h = 5.0
        post_color = [0.2, 0.2, 0.2]
        bulb_size = 0.6

        # posts OUTSIDE crosswalks at the central intersection only
        r = self.road_width / 2 + self.crosswalk_width + 1.0
        y_post = post_h / 2
        y_bulb = post_h - 0.7

        corners = [
            (-r, -r),
            (r, -r),
            (-r, r),
            (r, r),
        ]

        for (x, z) in corners:
            # post
            post = Mesh(
                BoxGeometry(0.2, post_h, 0.2),
                SurfaceMaterial(property_dict={"baseColor": post_color}),
            )
            post.set_position([x, y_post, z])
            self.scene.add(post)

            # N–S bulbs (facing ±z)
            ns_red = Mesh(
                BoxGeometry(bulb_size, bulb_size, bulb_size),
                SurfaceMaterial(property_dict={"baseColor": [0.2, 0.0, 0.0]}),
            )
            ns_green = Mesh(
                BoxGeometry(bulb_size, bulb_size, bulb_size),
                SurfaceMaterial(property_dict={"baseColor": [0.0, 0.2, 0.0]}),
            )
            ns_red.set_position([x, y_bulb, z - 0.6])
            ns_green.set_position([x, y_bulb - bulb_size - 0.2, z - 0.6])
            self.scene.add(ns_red)
            self.scene.add(ns_green)
            self.ns_red_bulbs.append(ns_red)
            self.ns_green_bulbs.append(ns_green)

            # E–W bulbs (facing ±x)
            ew_red = Mesh(
                BoxGeometry(bulb_size, bulb_size, bulb_size),
                SurfaceMaterial(property_dict={"baseColor": [0.2, 0.0, 0.0]}),
            )
            ew_green = Mesh(
                BoxGeometry(bulb_size, bulb_size, bulb_size),
                SurfaceMaterial(property_dict={"baseColor": [0.0, 0.2, 0.0]}),
            )
            ew_red.set_position([x - 0.6, y_bulb, z])
            ew_green.set_position([x - 0.6, y_bulb - bulb_size - 0.2, z])
            self.scene.add(ew_red)
            self.scene.add(ew_green)
            self.ew_red_bulbs.append(ew_red)
            self.ew_green_bulbs.append(ew_green)

    # ---------- helper: vehicle update with queueing ----------
    def update_vehicles(self, dt, ns_green, ew_green):
        # group vehicles by lane+direction
        lanes = {}
        for v in self.vehicles:
            key = (v["axis"], v["lane"], v["dir"])
            lanes.setdefault(key, []).append(v)

        for (axis, lane, d), group in lanes.items():
            # sort front-to-back along movement direction
            group.sort(key=lambda v: v["pos"] * d, reverse=True)

            ahead_pos = None
            for v in group:
                pos = v["pos"]
                speed = v["speed"]

                new_pos = pos + d * speed * dt

                # which traffic signal applies?
                if axis == "x":
                    allowed = ew_green
                else:  # axis == "z"
                    allowed = ns_green

                stop = -4.0 if d > 0 else 4.0  # stop line (central intersection only)

                # red light: clamp at stop line near center
                if not allowed:
                    if abs(lane) < self.road_width:  # only lanes that cross center
                        if pos * d < stop * d and new_pos * d >= stop * d:
                            new_pos = stop
                        if abs(pos - stop) < 0.5 and new_pos * d > stop * d:
                            new_pos = stop

                # check if this step crosses map boundary
                wrapped = False
                if new_pos > 110.0:
                    new_pos = -110.0
                    wrapped = True
                elif new_pos < -110.0:
                    new_pos = 110.0
                    wrapped = True

                # keep safe distance from vehicle in front,
                # BUT only if this car did not just wrap around
                min_gap = 6.0  # center-to-center gap
                if ahead_pos is not None and not wrapped:
                    if d > 0:
                        max_pos = ahead_pos - min_gap
                        if new_pos > max_pos:
                            new_pos = max_pos
                    else:
                        min_pos = ahead_pos + min_gap
                        if new_pos < min_pos:
                            new_pos = min_pos

                v["pos"] = new_pos

                if axis == "x":
                    x, z = new_pos, lane
                else:
                    x, z = lane, new_pos

                v["node"].set_position([x, v["y"], z])

                # If this car wrapped, it is now at the *back* of the lane
                if not wrapped:
                    ahead_pos = new_pos

    # ---------- helper: pedestrians update ----------
    def update_pedestrians(self, dt):
        for p in self.pedestrians:
            p["pos"] += p["dir"] * p["speed"] * dt
            # wrap around
            if p["pos"] > 115.0:
                p["pos"] = -115.0
            elif p["pos"] < -115.0:
                p["pos"] = 115.0

            if p["axis"] == "x":
                x, z = p["pos"], p["lane"]
            else:
                x, z = p["lane"], p["pos"]
            p["node"].set_position([x, 0.0, z])

    # ---------- helper: tree–intersection proximity ----------
    def is_near_intersection(self, x, z, margin):
        for ix, iz in self.intersections:
            if abs(x - ix) <= margin and abs(z - iz) <= margin:
                return True
        return False
