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

class Example(Base):
    """
    Render a textured skysphere and a textured grass floor.
    Move the camera: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.sky_camera = Camera(aspect_ratio=512/512) 
        self.sky_camera.set_position([0, 20, 0]) 
        self.sky_camera.look_at([0, 0, 0]) 
        self.rig = MovementRig() 
        self.rig.add(self.camera)
        self.rig.add(self.sky_camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 1, 4])
        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="textures/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)
        room_geometry = SphereGeometry(radius=20)
        room_material = TextureMaterial(texture=Texture(file_name="textures/empty_play_room.jpg"))
        room = Mesh(room_geometry, room_material)
        room.scale = [-1, 1, 1]
        room.set_position([0, 3, 0])
        self.scene.add(room)
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="textures/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi/2)
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

    def update(self):        
        for t in self.text_objects:
            t.rotate_y(0.3 * self.delta_time)
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.sky_camera) 
        self.renderer.render(self.scene, self.camera) 

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
