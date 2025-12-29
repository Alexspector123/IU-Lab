#!/usr/bin/python3
import math

from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.texture import Texture
from py3d.extras.movement_rig import MovementRig
from py3d.geometry.rectangle import RectangleGeometry
from py3d.geometry.sphere import SphereGeometry
from py3d.light.ambient import AmbientLight
from py3d.light.directional import DirectionalLight
from py3d.material.phong import PhongMaterial
from py3d.material.texture import TextureMaterial
from py3d.material.material import Material


class Example(Base):
    """
    Scene with:
    - Textured sky and grass
    - Sun sphere that is pure yellow (not shaded by lighting)
    - A shaded Earth sphere on the ground lit by the Sun
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)

        # Camera rig
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.set_position([0, 2, 12])

        # --- Sky ---
        sky_geometry = SphereGeometry(radius=50)
        sky_material = TextureMaterial(texture=Texture(file_name="py3d/images/sky.jpg"))
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)

        # --- Grass ---
        grass_geometry = RectangleGeometry(width=100, height=100)
        grass_material = TextureMaterial(
            texture=Texture(file_name="py3d/images/grass.jpg"),
            property_dict={"repeatUV": [50, 50]}
        )
        grass = Mesh(grass_geometry, grass_material)
        grass.rotate_x(-math.pi / 2)
        self.scene.add(grass)

        # --- Lighting ---
        self.ambient_light = AmbientLight(color=[0.3, 0.3, 0.3])
        self.scene.add(self.ambient_light)

        self.sun_light = DirectionalLight(color=[1.0, 1.0, 0.9], direction=[-1, -1, -1])
        self.scene.add(self.sun_light)

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

        # --- Earth sphere (shaded by lights) ---
        earth_geometry = SphereGeometry(radius=1.0)
        earth_material = PhongMaterial(
            property_dict={"baseColor": [0.2, 0.4, 0.8]},
            number_of_light_sources=2  # ambient + directional
        )
        self.earth_object = Mesh(earth_geometry, earth_material)
        self.earth_object.set_position([0, 1, 0])
        self.scene.add(self.earth_object)
        

    def update(self):
        # Animate the Sun across the sky
        sun_x = 6 * math.cos(0.3 * self.time)
        sun_y = 8
        sun_z = 6 * math.sin(0.3 * self.time)
        self.sun.set_position([sun_x, sun_y, sun_z])

        # Light direction follows the Sun sphere position
        target = [0, 1, 0]
        dir_x = target[0] - sun_x
        dir_y = target[1] - sun_y
        dir_z = target[2] - sun_z
        self.sun_light.set_direction([dir_x, dir_y, dir_z])

        # Rotate Earth sphere slowly
        self.earth_object.rotate_y(0.01)

        # Camera movement
        self.rig.update(self.input, self.delta_time)

        # Render scene
        self.renderer.render(self.scene, self.camera)


# Run the program
Example(screen_size=[800, 600]).run()
