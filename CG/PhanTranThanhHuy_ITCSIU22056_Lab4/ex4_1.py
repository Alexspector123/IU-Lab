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
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 5, 12])
        sky_geometry = SphereGeometry(radius=5)
        sky_material = TextureMaterial(texture=Texture(file_name="textures/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="textures/grid.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.set_position([0,10,0])
        self.scene.add(grass)

    def update(self):
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.delta_time)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
