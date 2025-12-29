#!/usr/bin/python3
import math

from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry
from py3d.material.texture import TextureMaterial
from py3d.extras.movement_rig import MovementRig
from py3d.extras.text_texture import TextTexture
from py3d.material.surface import SurfaceMaterial
from py3d.geometry.box import BoxGeometry
from py3d.core_ext.object3d import Object3D

class Example(Base):
    """
    Render a textured skysphere and a textured grass floor.
    Move the camera: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        room_w, room_h, room_d = 6.0, 3.0, 6.0
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.sky_camera = Camera(aspect_ratio=512/512) 
        self.sky_camera.set_position([0, 20, 0]) 
        self.sky_camera.look_at([0, 0, 0]) 
        self.rig = MovementRig(units_per_second=50, degrees_per_second=60) 
        self.rig.add(self.camera)
        self.rig.add(self.sky_camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 1, 6])
        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="textures/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
        grass.set_position([0, -0.05, 0]) 
        self.scene.add(grass)

        text1 = TextTexture(text="This is a room")
        text1_material = TextureMaterial(texture=text1)
        text1_geo = RectangleGeometry(width=3.0, height=0.5)
        text1_mesh = Mesh(text1_geo, text1_material)
        text1_mesh.set_position([0, 5, 0])
        text1_mesh.rotate_y(math.pi)
        self.scene.add(text1_mesh)

        text2 = TextTexture(text="Move inside to view it!")
        text2_material = TextureMaterial(texture=text2)
        text2_geo = RectangleGeometry(width=3.0, height=0.5)
        text2_mesh = Mesh(text2_geo, text2_material)
        text2_mesh.set_position([0, 4.5, 0])
        text2_mesh.rotate_y(math.pi)
        self.scene.add(text2_mesh)

        self.text_objects = [text1_mesh, text2_mesh]

        floor_geometry = RectangleGeometry(width=room_w, height=room_d)
        floor_material = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.5, 0.5],})
        floor = Mesh(floor_geometry, floor_material)
        floor.rotate_x(-math.pi / 2)
        floor.set_position([0, 0, 0])
        self.scene.add(floor)

        ceiling_geometry = RectangleGeometry(width=room_w, height=room_d)
        ceiling_material = SurfaceMaterial(property_dict={"baseColor": [1.0, 1.0, 1.0],})
        ceiling = Mesh(ceiling_geometry, ceiling_material)
        ceiling.rotate_x(math.pi / 2)
        ceiling.set_position([0, room_h, 0])
        self.scene.add(ceiling)

        back_geometry = RectangleGeometry(width=room_w, height=room_h)
        back_material = SurfaceMaterial(property_dict={"baseColor": [0, 0, 1],})
        back = Mesh(back_geometry, back_material)
        back.set_position([0, room_h / 2, -room_d / 2])
        self.scene.add(back)

        front_geometry = RectangleGeometry(width=room_w, height=room_h)
        front_material = SurfaceMaterial(property_dict={"baseColor": [0, 1, 0],})
        front = Mesh(front_geometry, front_material)
        front.rotate_y(math.pi)
        front.set_position([0, room_h / 2, room_d / 2])
        self.scene.add(front)

        left_geometry = RectangleGeometry(width=room_d, height=room_h)
        left_material = SurfaceMaterial(property_dict={"baseColor": [1, 0, 0],})
        left = Mesh(left_geometry, left_material)
        left.rotate_y(math.pi / 2)
        left.set_position([-room_w / 2, room_h / 2, 0])
        self.scene.add(left)

        right_geometry = RectangleGeometry(width=room_d, height=room_h)
        right_material = SurfaceMaterial(property_dict={"baseColor": [0.9, 0.8, 0.2],})
        right = Mesh(right_geometry, right_material)
        right.rotate_y(-math.pi / 2)
        right.set_position([room_w / 2, room_h / 2, 0])
        self.scene.add(right)

        table_geo = BoxGeometry(1.5, 0.1, 1.0)
        table_mat = SurfaceMaterial(property_dict={"baseColor": [0.36, 0.20, 0.09]})
        table = Mesh(table_geo, table_mat)
        table.set_position([0, 0.6, 0])
        self.scene.add(table)
        leg_geo = BoxGeometry(0.1, 0.6, 0.1)
        leg_mat = SurfaceMaterial(property_dict={"baseColor": [0.36, 0.20, 0.09]})
        leg_positions = [
            [0.65, 0.3, 0.45],   
            [-0.65, 0.3, 0.45], 
            [0.65, 0.3, -0.45],  
            [-0.65, 0.3, -0.45]  
        ]
        for pos in leg_positions:
            leg = Mesh(leg_geo, leg_mat)
            leg.set_position(pos)
            self.scene.add(leg)

        tv_geo = RectangleGeometry(width=1.6, height=0.9) 
        tv_mat = SurfaceMaterial(property_dict={"baseColor": [0, 0, 0]})
        tv = Mesh(tv_geo, tv_mat) 
        tv.set_position([0, 1.6, -room_d/2 + 0.05])
        self.scene.add(tv)

        self.fan_hub = Mesh(BoxGeometry(0.15, 0.15, 0.15), SurfaceMaterial(property_dict={"baseColor": [0.5, 0.5, 0.5],})) 
        self.fan_hub.set_position([0, 2.8, 0])
        self.scene.add(self.fan_hub)
        blade = Mesh(RectangleGeometry(width=1.2, height=0.15), SurfaceMaterial(property_dict={"baseColor": [0.5, 0.5, 0.5],}))
        blade.rotate_x(math.pi / 2)
        blade.set_position([0.6, 0, 0])
        for i in range(4):
            pivot = Object3D()
            pivot.rotate_y(i * math.pi / 2.0)
            self.fan_hub.add(pivot)

            blade = Mesh(
                RectangleGeometry(width=1.2, height=0.15),
                SurfaceMaterial(property_dict={"baseColor": [0.5, 0.5, 0.5]})
            )
            blade.rotate_x(math.pi / 2)
            blade.set_position([0.6, 0, 0]) 
            pivot.add(blade)

        self.scene.add(self.make_chair(1.2, 0, -math.pi/2))
        self.scene.add(self.make_chair(-1.2, 0, math.pi/2))
        self.scene.add(self.make_sofa(room_w))

        picture_geo = RectangleGeometry(1.2, 0.9)
        picture_tex = Texture(file_name="textures/chelsea.jpg")
        picture_mat = TextureMaterial(texture=picture_tex)
        picture = Mesh(picture_geo, picture_mat)
        picture.rotate_y(math.pi / 2)
        picture.set_position([-room_w / 2 + 0.05, 1.6, 0.5])
        self.scene.add(picture)

        self.scene.add(self.make_window(0, 1.5, room_d/2 - 0.01, inside=False))
        self.scene.add(self.make_window(0, 1.5, room_d/2 - 0.01, inside=True))

        self.make_fence(7, 7)
        self.make_gate(7)

        self.make_garden(7)

    def make_chair(self, x, z, rot_y):
        chair = Object3D()
        chair.set_position([x, 0, z])
        chair.rotate_y(rot_y)

        seat_geo = BoxGeometry(0.6, 0.05, 0.6)
        seat_mat = SurfaceMaterial(property_dict={"baseColor": [0.596, 0.596, 0.596]})
        seat = Mesh(seat_geo, seat_mat)
        seat.set_position([0, 0.45, 0])
        chair.add(seat)

        leg_geo = BoxGeometry(0.05, 0.45, 0.05)
        leg_mat = SurfaceMaterial(property_dict={"baseColor": [0.396, 0.396, 0.396]})
        leg_positions = [
            [0.25, 0.225, 0.25],
            [-0.25, 0.225, 0.25],
            [0.25, 0.225, -0.25],
            [-0.25, 0.225, -0.25]
        ]
        for pos in leg_positions:
            leg = Mesh(leg_geo, leg_mat)
            leg.set_position(pos)
            chair.add(leg)

        back_geo = BoxGeometry(0.6, 0.5, 0.05)
        back_mat = SurfaceMaterial(property_dict={"baseColor": [0.596, 0.596, 0.596]})
        back = Mesh(back_geo, back_mat)
        back.set_position([0, 0.70, -0.275])
        chair.add(back)
        return chair
        
    def make_sofa(self, room_w):
        sofa = Object3D()
        
        sofa.set_position([room_w / 2 - 0.3, 0, 0])
        sofa.rotate_y(-math.pi / 2)

        base_geo = BoxGeometry(1.8, 0.4, 0.7)
        base_mat = SurfaceMaterial(property_dict={"baseColor": [0.16, 0.16, 0.16]})
        base = Mesh(base_geo, base_mat)
        base.set_position([0, 0.2, 0])
        sofa.add(base)

        back_geo = BoxGeometry(1.8, 0.6, 0.15)
        back_mat = SurfaceMaterial(property_dict={"baseColor": [0.16, 0.16, 0.16]})
        back = Mesh(back_geo, back_mat)
        back.set_position([0, 0.6, -0.25])
        sofa.add(back)

        return sofa

    def make_window(self, x, y, z, inside=False):
        outer_w, outer_h = 1.6, 1.6
        gap = 0.05
        inner_w = (outer_w - gap) / 2
        inner_h = (outer_h - gap) / 2

        group = Object3D()

        # backing
        backing_geo = RectangleGeometry(width=outer_w, height=outer_h)
        backing_mat = SurfaceMaterial(property_dict={"baseColor": [0, 1, 0]})
        backing = Mesh(backing_geo, backing_mat)
        backing.set_position([0, 0, 0])
        group.add(backing)

        # frame
        frame_geo = RectangleGeometry(width=outer_w, height=outer_h)
        frame_mat = SurfaceMaterial(property_dict={"baseColor": [0.3, 0.3, 0.3]})
        frame = Mesh(frame_geo, frame_mat)
        frame.set_position([0, 0, 0.005])
        group.add(frame)

        # 4 panes
        pane_mat = SurfaceMaterial(property_dict={"baseColor": [0.8, 0.9, 1.0]})
        offsets = [
            [-inner_w/2 - gap/4,  inner_h/2 + gap/4],
            [ inner_w/2 + gap/4,  inner_h/2 + gap/4],
            [-inner_w/2 - gap/4, -inner_h/2 - gap/4],
            [ inner_w/2 + gap/4, -inner_h/2 - gap/4]
        ]
        for ox, oy in offsets:
            pane_geo = RectangleGeometry(width=inner_w, height=inner_h)
            pane = Mesh(pane_geo, pane_mat)
            pane.set_position([ox, oy, 0.01])
            group.add(pane)

        # nếu là bản copy bên trong, xoay Y 180°
        if inside:
            group.rotate_y(math.pi)
            group.set_position([x, y, z - 0.15])  # lùi vào trong
        else:
            group.set_position([x, y, z])  # phía ngoài

        return group
    def make_fence(self, fence_x, fence_z):
        fence_h = 1.0
        thickness = 0.1
        gate_width = 2.5

        back_geo = BoxGeometry(2*fence_x, fence_h, thickness)
        back_mat = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.3, 0.1]})
        back_fence = Mesh(back_geo, back_mat)
        back_fence.set_position([0, fence_h/2, -fence_z])
        self.scene.add(back_fence)

        left_width = fence_x - gate_width/2
        right_width = fence_x - gate_width/2

        left_geo = BoxGeometry(left_width, fence_h, thickness)
        left_mat = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.3, 0.1]})
        left_box = Mesh(left_geo, left_mat)
        left_box.set_position([-(fence_x + gate_width/2)/2, fence_h/2, fence_z])
        self.scene.add(left_box)

        right_geo = BoxGeometry(right_width, fence_h, thickness)
        right_mat = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.3, 0.1]})
        right_box = Mesh(right_geo, right_mat)
        right_box.set_position([(fence_x + gate_width/2)/2, fence_h/2, fence_z])
        self.scene.add(right_box)

        left_geo = BoxGeometry(thickness, fence_h, 2*fence_z)
        left_mat = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.3, 0.1]})
        left_fence = Mesh(left_geo, left_mat)
        left_fence.set_position([-fence_x, fence_h/2, 0])
        self.scene.add(left_fence)

        right_geo = BoxGeometry(thickness, fence_h, 2*fence_z)
        right_mat = SurfaceMaterial(property_dict={"baseColor": [0.5, 0.3, 0.1]})
        right_fence = Mesh(right_geo, right_mat)
        right_fence.set_position([fence_x, fence_h/2, 0])
        self.scene.add(right_fence)
    def make_gate(self, fence_z):
        gate_width=2.5
        post_height=1.0
        post_thickness=0.1

        left_post_geo = BoxGeometry(post_thickness, post_height, post_thickness)
        left_post_mat = SurfaceMaterial(property_dict={"baseColor": [0.6, 0.3, 0.1]})
        left_post = Mesh(left_post_geo, left_post_mat)
        left_post.set_position([-gate_width/2, post_height/2, fence_z])
        self.scene.add(left_post)
    
        right_post_geo = BoxGeometry(post_thickness, post_height, post_thickness)
        right_post_mat = SurfaceMaterial(property_dict={"baseColor": [0.6, 0.3, 0.1]})
        right_post = Mesh(right_post_geo, right_post_mat)
        right_post.set_position([gate_width/2, post_height/2, fence_z])
        self.scene.add(right_post)

        beam_geo = BoxGeometry(gate_width + post_thickness, post_thickness, post_thickness)
        beam_mat = SurfaceMaterial(property_dict={"baseColor": [0.6, 0.3, 0.1]})
        beam = Mesh(beam_geo, beam_mat)
        beam.set_position([0, post_height + post_thickness/2, fence_z])
        self.scene.add(beam)

        door_geo = BoxGeometry(gate_width - post_thickness, post_height, 0.05)
        door_mat = SurfaceMaterial(property_dict={"baseColor": [0.8, 0.6, 0.4]})
        door = Mesh(door_geo, door_mat)
        door.set_position([0, post_height/2, fence_z - 0.05])
        self.scene.add(door)

    def make_tree(self, x, z):
        # Trunk
        trunk_geo = BoxGeometry(0.25, 1.0, 0.25)
        trunk_mat = SurfaceMaterial(property_dict={"baseColor": [0.55, 0.27, 0.07]})
        trunk = Mesh(trunk_geo, trunk_mat)
        trunk.set_position([x, 0.5, z])
        self.scene.add(trunk)

        # Crown
        crown_geo = SphereGeometry(0.65)
        crown_mat = SurfaceMaterial(property_dict={"baseColor": [0.0, 0.6, 0.0]})
        crown = Mesh(crown_geo, crown_mat)
        crown.set_position([x, 1.4, z])
        self.scene.add(crown)

    def make_flower(self, x, z, color):
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

    def make_garden(self, fence_z):
        tree_positions = [-2.0, 0.0, 2.0]
        for x in tree_positions:
            self.make_tree(x, fence_z - 2.0)

        flower_colors = [[1,0,0], [1,1,0], [1,0.5,0]]
        for i, x in enumerate(range(-3, 4)):
            color = flower_colors[i % len(flower_colors)]
            self.make_flower(x, fence_z - 1.0, color)

    def update(self):        
        for t in self.text_objects:
            t.rotate_y(0.3 * self.delta_time)
        self.rig.update(self.input, self.delta_time)
        self.fan_hub.rotate_y(4.0 * self.delta_time)
        self.renderer.render(self.scene, self.sky_camera) 
        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
