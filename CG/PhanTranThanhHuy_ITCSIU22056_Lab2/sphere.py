#!/usr/bin/python3
from math import pi, sin, cos
from py3d.core.base import Base
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.geometry.sphere import SphereGeometry
from py3d.material.material import Material
from py3d.core.matrix import Matrix


class Example(Base):
    """ Render a spinning sphere with gradient colors """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 7])
        vs_code = """
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        in vec3 vertexPosition;
        out vec3 position;
        void main()
        {
            vec4 pos = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
            position = vertexPosition;
        }
        """
        fs_code = """
        in vec3 position;
        out vec4 fragColor;
        void main()
        {
            vec3 color = mod(position, 1.0);
            fragColor = vec4(color, 1.0);
        }
        """
        material = Material(vs_code, fs_code)
        material.locate_uniforms()

        sun_geometry = SphereGeometry(radius=1.0)
        self.sun = Mesh(sun_geometry, material)
        self.scene.add(self.sun)

        earth_geometry = SphereGeometry(radius=0.5)
        self.earth = Mesh(earth_geometry, material)
        self.scene.add(self.earth)

        moon_geometry = SphereGeometry(radius=0.2)
        self.moon = Mesh(moon_geometry, material)
        self.scene.add(self.moon)

        self.orbit_radius = 3.0      
        self.moon_orbit_radius = 1.0
        self.orbit_angle = 0.0
        self.moon_orbit_angle = 0.0

    def update(self):
        self.sun.rotate_y(0.01)

        self.orbit_angle += 0.01
        x_earth = self.orbit_radius * cos(self.orbit_angle)
        z_earth = self.orbit_radius * sin(self.orbit_angle)
        self.earth.set_position([x_earth, 0, z_earth])

        self.earth.rotate_y(0.05)

        self.moon_orbit_angle += 0.05
        x_moon = x_earth + self.moon_orbit_radius * cos(self.moon_orbit_angle)
        z_moon = z_earth + self.moon_orbit_radius * sin(self.moon_orbit_angle)
        self.moon.set_position([x_moon, 0, z_moon])

        self.moon.rotate_y(0.1)

        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()