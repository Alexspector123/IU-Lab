#!/usr/bin/python3
import math

from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.core_ext.object3d import Object3D
from py3d.geometry.box import BoxGeometry
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry
from py3d.material.surface import SurfaceMaterial
from py3d.material.texture import TextureMaterial
from py3d.extras.movement_rig import MovementRig
from py3d.extras.text_texture import TextTexture
from py3d.light.ambient import AmbientLight
from py3d.light.directional import DirectionalLight
from py3d.material.phong import PhongMaterial
from py3d.material.material import Material

class SurfaceMaterial(PhongMaterial):
    def __init__(self, *args, **kwargs):
        # Default to 2 lights (ambient + directional) and enable shadows
        kwargs.setdefault("number_of_light_sources", 2)
        kwargs.setdefault("use_shadow", True)
        super().__init__(*args, **kwargs)

class Example(Base):
    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()

        # camera
        self.camera = Camera(aspect_ratio=800 / 600)
        self.rig = MovementRig(units_per_second=10)
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 1, 14])
        self.camera.look_at([0, 1.5, 0])

        # sky
        sky = Mesh(SphereGeometry(50), TextureMaterial(Texture("textures/sky.jpg")))
        self.scene.add(sky)

        # ground
        ground_geometry = RectangleGeometry(width=100, height=100)
        ground_material = PhongMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            number_of_light_sources=2,
            use_shadow=True
        )
        ground = Mesh(ground_geometry, ground_material)
        ground.rotate_x(-math.pi / 2)
        ground.set_position([0, -0.05, 0])
        self.scene.add(ground)

        # labels
        title_tex = TextTexture(
            text="This is a room,",
            system_font_name="Arial Bold",
            font_size=80,
            font_color=[1, 1, 1],
            image_width=1024,
            image_height=128,
            align_horizontal=0.5,
            align_vertical=0.5,
            image_border_width=4,
            image_border_color=[255, 0, 0]
        )
        self.title = Mesh(RectangleGeometry(3.0, 0.5), TextureMaterial(title_tex))
        self.title.set_position([0, 5, 0])
        self.scene.add(self.title)

        sub_tex = TextTexture(
            text="move inside to view it!",
            system_font_name="Arial Bold",
            font_size=80,
            font_color=[1, 1, 1],
            image_width=1024,
            image_height=128,
            align_horizontal=0.5,
            align_vertical=0.5,
            image_border_width=4,
            image_border_color=[255, 0, 0]
        )
        self.sub = Mesh(RectangleGeometry(3.5, 0.5), TextureMaterial(sub_tex))
        self.sub.set_position([0, 4.5, 0])
        self.scene.add(self.sub)

        # ========= ROOM =========
        room_w, room_h, room_d = 6.0, 3.0, 6.0

        # floor
        floor = Mesh(
            RectangleGeometry(room_w, room_d),
            SurfaceMaterial(property_dict={"baseColor": [0.75, 0.75, 0.75]})
        )
        floor.rotate_x(-math.pi/2)
        floor.set_position([0, 0, 0])
        self.scene.add(floor)

        # ceiling
        ceil = Mesh(
            RectangleGeometry(room_w, room_d),
            SurfaceMaterial(property_dict={"baseColor": [1, 1, 1]})
        )
        ceil.rotate_x(math.pi/2)
        ceil.set_position([0, room_h, 0])
        self.scene.add(ceil)

        # walls
        back = Mesh(
            RectangleGeometry(room_w, room_h),
            SurfaceMaterial(property_dict={"baseColor": [0.2, 0.2, 1.0]})
        )
        back.set_position([0, room_h/2, -room_d/2])
        self.scene.add(back)

        front = Mesh(
            RectangleGeometry(room_w, room_h),
            SurfaceMaterial(property_dict={"baseColor": [0.2, 1.0, 0.2]})
        )
        front.rotate_y(math.pi)
        front.set_position([0, room_h/2, room_d/2])
        self.scene.add(front)

        left = Mesh(
            RectangleGeometry(room_d, room_h),
            SurfaceMaterial(property_dict={"baseColor": [1.0, 0.2, 0.2]})
        )
        left.rotate_y(math.pi/2)
        left.set_position([-room_w/2, room_h/2, 0])
        self.scene.add(left)

        right = Mesh(
            RectangleGeometry(room_d, room_h),
            SurfaceMaterial(property_dict={"baseColor": [1.0, 1.0, 0.2]})
        )
        right.rotate_y(-math.pi/2)
        right.set_position([room_w/2, room_h/2, 0])
        self.scene.add(right)

        # ========= furniture =========
        table = Mesh(
            BoxGeometry(1.5, 0.1, 1.0),
            SurfaceMaterial(property_dict={"baseColor": [0.5, 0.35, 0.2]})
        )
        table.set_position([0, 0.6, 0])
        self.scene.add(table)

        leg_geo = BoxGeometry(0.1, 0.6, 0.1)
        leg_mat = SurfaceMaterial(property_dict={"baseColor": [0.4, 0.25, 0.1]})
        for x in (0.65, -0.65):
            for z in (0.45, -0.45):
                leg = Mesh(leg_geo, leg_mat)
                leg.set_position([x, 0.3, z])
                self.scene.add(leg)
        
        self.ambient_light = AmbientLight(color=[0.3, 0.3, 0.35])
        self.scene.add(self.ambient_light)
        self.sun_light = DirectionalLight(color=[1.0, 1.0, 0.9], direction=[-1, -1, -1])
        self.scene.add(self.sun_light)
        self.renderer.enable_shadows(
            self.sun_light,
            strength = 0.8
        )

        # --- Sun sphere (always yellow, not shaded) ---
        sun_geometry = SphereGeometry(radius=2.0)
        vs_code = """
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        in vec3 vertexPosition;
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
        }
        """
        fs_code = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 0.9, 0.0, 1.0); // pure yellow
        }
        """
        sun_material = Material(vs_code, fs_code)
        sun_material.locate_uniforms()
        self.sun = Mesh(sun_geometry, sun_material)
        self.sun.set_position([0, 8, 0])
        self.scene.add(self.sun)

        def make_chair(px, pz, rot=0.0):
            root = Object3D()
            self.scene.add(root)
            root.set_position([px, 0, pz])
            root.rotate_y(rot)

            seat = Mesh(
                BoxGeometry(0.5, 0.08, 0.5),
                SurfaceMaterial(property_dict={"baseColor": [0.7, 0.7, 0.7]})
            )
            seat.set_position([0, 0.45, 0])
            root.add(seat)

            for lx in (0.2, -0.2):
                for lz in (0.2, -0.2):
                    leg = Mesh(
                        BoxGeometry(0.05, 0.45, 0.05),
                        SurfaceMaterial(property_dict={"baseColor": [0.4, 0.4, 0.4]})
                    )
                    leg.set_position([lx, 0.225, lz])
                    root.add(leg)

            backrest = Mesh(
                BoxGeometry(0.5, 0.5, 0.05),
                SurfaceMaterial(property_dict={"baseColor": [0.6, 0.6, 0.6]})
            )
            backrest.set_position([0, 0.75, -0.22])
            root.add(backrest)

        make_chair(1.2, 0, -math.pi/2)
        make_chair(-1.2, 0, math.pi/2)

        # sofa
        sofa = Object3D()
        self.scene.add(sofa)
        sofa.set_position([room_w/2 - 0.3, 0, -1.0])
        sofa.rotate_y(-math.pi/2)

        sofa_base = Mesh(
            BoxGeometry(1.8, 0.4, 0.7),
            SurfaceMaterial(property_dict={"baseColor": [0.2, 0.2, 0.2]})
        )
        sofa_base.set_position([0, 0.2, 0])
        sofa.add(sofa_base)

        sofa_back = Mesh(
            BoxGeometry(1.8, 0.6, 0.15),
            SurfaceMaterial(property_dict={"baseColor": [0.25, 0.25, 0.25]})
        )
        sofa_back.set_position([0, 0.6, -0.25])
        sofa.add(sofa_back)

        # TV
        tv = Mesh(
            RectangleGeometry(1.6, 0.9),
            SurfaceMaterial(property_dict={"baseColor": [0, 0, 0]})
        )
        tv.set_position([0, 1.6, -room_d/2 + 0.05])
        self.scene.add(tv)

        # picture
        picture = Mesh(
            RectangleGeometry(1.2, 0.9),
            TextureMaterial(Texture("textures/chelsea.jpg"))
        )
        picture.rotate_y(math.pi/2)
        picture.set_position([-room_w/2 + 0.05, 1.6, 0.5])
        self.scene.add(picture)

        # window (2x2, both sides)
        room_color = [0.2, 1.0, 0.2]
        frame_color = [0.9, 0.9, 0.9]
        pane_color = [1.0, 1.0, 1.0]
        outer_w = 1.6
        outer_h = 1.6
        gap = 0.05
        inner_w = (outer_w - gap) / 2.0
        inner_h = (outer_h - gap) / 2.0
        off = (inner_w/2 + gap/2, inner_h/2 + gap/2)

        def add_pane(parent, ox, oy):
            pane = Mesh(
                RectangleGeometry(inner_w, inner_h),
                SurfaceMaterial(property_dict={"baseColor": pane_color})
            )
            pane.set_position([ox, oy, 0.002])
            parent.add(pane)

        # outside
        win_out = Object3D(); self.scene.add(win_out)
        win_out.set_position([1.8, 1.6, room_d/2 - 0.01])
        win_out.add(Mesh(
            RectangleGeometry(outer_w, outer_h),
            SurfaceMaterial(property_dict={"baseColor": room_color})
        ))
        frame_out = Mesh(
            RectangleGeometry(outer_w, outer_h),
            SurfaceMaterial(property_dict={"baseColor": frame_color})
        )
        frame_out.set_position([0, 0, 0.001])
        win_out.add(frame_out)
        add_pane(win_out, -off[0],  off[1])
        add_pane(win_out,  off[0],  off[1])
        add_pane(win_out, -off[0], -off[1])
        add_pane(win_out,  off[0], -off[1])

        # inside
        win_in = Object3D(); self.scene.add(win_in)
        win_in.set_position([1.8, 1.6, room_d/2 - 0.15])
        win_in.rotate_y(math.pi)
        win_in.add(Mesh(
            RectangleGeometry(outer_w, outer_h),
            SurfaceMaterial(property_dict={"baseColor": room_color})
        ))
        frame_in = Mesh(
            RectangleGeometry(outer_w, outer_h),
            SurfaceMaterial(property_dict={"baseColor": frame_color})
        )
        frame_in.set_position([0, 0, 0.001])
        win_in.add(frame_in)
        add_pane(win_in, -off[0],  off[1])
        add_pane(win_in,  off[0],  off[1])
        add_pane(win_in, -off[0], -off[1])
        add_pane(win_in,  off[0], -off[1])

        # ceiling fan
        self.fan_hub = Mesh(
            BoxGeometry(0.15, 0.15, 0.15),
            SurfaceMaterial(property_dict={"baseColor": [0.9, 0.9, 0.9]})
        )
        self.fan_hub.set_position([0, 2.8, 0])
        self.scene.add(self.fan_hub)

        blade_geo = RectangleGeometry(1.2, 0.15)
        blade_mat = SurfaceMaterial(property_dict={"baseColor": [0.8, 0.8, 0.8]})
        for i in range(4):
            pivot = Object3D()
            self.fan_hub.add(pivot)
            pivot.rotate_y(i * math.pi/2)
            blade = Mesh(blade_geo, blade_mat)
            blade.rotate_x(math.pi/2)
            blade.set_position([0.6, 0, 0])
            pivot.add(blade)

        # ========= FENCE (fixed, axis-aligned) =========
        fence_color = [0.7, 0.7, 0.7]
        fence_h = 1.1
        margin = 4.0  # distance from room to fence
        fence_x = room_w/2 + margin   # left/right
        fence_z = room_d/2 + margin   # front/back

        # back fence (behind room)
        back_fence = Mesh(
            BoxGeometry(2*fence_x, fence_h, 0.15),
            SurfaceMaterial(property_dict={"baseColor": fence_color})
        )
        back_fence.set_position([0, fence_h/2, -fence_z])
        self.scene.add(back_fence)

        # front fence (we will split for gate)
        # left part
        gate_width = 2.5
        front_left = Mesh(
            BoxGeometry(2*fence_x - gate_width, fence_h, 0.15),
            SurfaceMaterial(property_dict={"baseColor": fence_color})
        )
        # this left part is centered from -fence_x to -(gate_width/2)
        left_len = 2*fence_x - gate_width
        left_center_x = -(gate_width/2) - (left_len/2 - fence_x)
        # easier: place by hand
        front_left.set_position([-(gate_width/2) - (left_len/2), fence_h/2, fence_z])
        self.scene.add(front_left)

        # right part
        front_right = Mesh(
            BoxGeometry(2*fence_x - gate_width, fence_h, 0.15),
            SurfaceMaterial(property_dict={"baseColor": fence_color})
        )
        front_right.set_position([(gate_width/2) + (left_len/2), fence_h/2, fence_z])
        self.scene.add(front_right)

        # left side fence
        left_fence = Mesh(
            BoxGeometry(0.15, fence_h, 2*fence_z),
            SurfaceMaterial(property_dict={"baseColor": fence_color})
        )
        left_fence.set_position([-fence_x, fence_h/2, 0])
        self.scene.add(left_fence)

        # right side fence
        right_fence = Mesh(
            BoxGeometry(0.15, fence_h, 2*fence_z),
            SurfaceMaterial(property_dict={"baseColor": fence_color})
        )
        right_fence.set_position([fence_x, fence_h/2, 0])
        self.scene.add(right_fence)

        # ========= GATE (boxes) at z = fence_z =========
        gate_post_h = fence_h + 0.3
        post_thick = 0.2

        left_post = Mesh(
            BoxGeometry(post_thick, gate_post_h, 0.18),
            SurfaceMaterial(property_dict={"baseColor": [0.6, 0.4, 0.2]})
        )
        left_post.set_position([-gate_width/2, gate_post_h/2, fence_z])
        self.scene.add(left_post)

        right_post = Mesh(
            BoxGeometry(post_thick, gate_post_h, 0.18),
            SurfaceMaterial(property_dict={"baseColor": [0.6, 0.4, 0.2]})
        )
        right_post.set_position([gate_width/2, gate_post_h/2, fence_z])
        self.scene.add(right_post)

        top_beam = Mesh(
            BoxGeometry(gate_width, 0.15, 0.18),
            SurfaceMaterial(property_dict={"baseColor": [0.6, 0.4, 0.2]})
        )
        top_beam.set_position([0, gate_post_h, fence_z])
        self.scene.add(top_beam)

        # gate panel (door)
        gate_panel = Mesh(
            BoxGeometry(gate_width - 0.3, fence_h*0.85, 0.12),
            SurfaceMaterial(property_dict={"baseColor": [0.8, 0.6, 0.3]})
        )
        gate_panel.set_position([0, (fence_h*0.85)/2, fence_z - 0.05])
        self.scene.add(gate_panel)

        # ========= GARDEN =========
        def make_tree(x, z):
            trunk = Mesh(
                BoxGeometry(0.25, 1.0, 0.25),
                SurfaceMaterial(property_dict={"baseColor": [0.45, 0.28, 0.15]})
            )
            trunk.set_position([x, 0.5, z])
            self.scene.add(trunk)

            crown = Mesh(
                SphereGeometry(0.65),
                SurfaceMaterial(property_dict={"baseColor": [0.1, 0.5, 0.1]})
            )
            crown.set_position([x, 1.4, z])
            self.scene.add(crown)

        # inside fence, between house and fence
        make_tree(-3.5, fence_z - 2.5)
        make_tree(3.5, fence_z - 2.5)
        make_tree(-5.0, 2.0)

        def make_flower(x, z, color):
            stem = Mesh(
                BoxGeometry(0.05, 0.25, 0.05),
                SurfaceMaterial(property_dict={"baseColor": [0.1, 0.5, 0.1]})
            )
            stem.set_position([x, 0.125, z])
            self.scene.add(stem)

            bud = Mesh(
                SphereGeometry(0.15),
                SurfaceMaterial(property_dict={"baseColor": color})
            )
            bud.set_position([x, 0.3, z])
            self.scene.add(bud)

        for i in range(-3, 4):
            make_flower(i * 0.4, fence_z - 1.0, [1.0, 0.4, 0.6])

        # top camera
        self.sky_camera = Camera(aspect_ratio=512/512)
        self.sky_camera.set_position([0, 25, 0])
        self.scene.add(self.sky_camera)

    def update(self):
        self.title.rotate_y(0.3 * self.delta_time)
        self.sub.rotate_y(0.3 * self.delta_time)

        self.rig.update(self.input, self.delta_time)

        self.fan_hub.rotate_y(4.0 * self.delta_time)

        self.renderer.render(self.scene, self.sky_camera)
        self.renderer.render(self.scene, self.camera)

        # Animate the Sun across the sky
        day_speed = 0.05
        theta = (self.time * day_speed) % math.pi # from 0 to pi
        sun_x = 30.0 * math.cos(theta)
        sun_y = 5.0 + 25.0 * math.sin(theta)
        sun_z =-40.0
        # east-> west
        # low-> high-> low
        # fixed distance in front
        self.sun.set_position([sun_x, sun_y, sun_z])
        # Light direction follows the Sun sphere position
        target = [0, 0, 0]
        dir_x = target[0] - sun_x
        dir_y = target[1] - sun_y
        dir_z = target[2] - sun_z
        self.sun_light.set_direction([dir_x, dir_y, dir_z])


Example(screen_size=[800, 600]).run()
