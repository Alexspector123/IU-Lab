#!/usr/bin/python3
import math

import OpenGL.GL as GL

from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform


class Example(Base):
    """ Animate a triangle moving in a circular path around the origin """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            uniform vec3 center;
            uniform float angle;
            void main()
            {
                float c = cos(angle);
                float s = sin(angle);
                mat2 rotation = mat2(c, -s, s, c);

                vec2 local = position.xy - center.xy;
                vec2 rotated = rotation * local;
                vec2 world = rotated + center.xy + translation.xy;

                gl_Position = vec4(world.x, world.y, position.z + translation.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        self.position_data = [[ 0.0,  0.2,  0.0],
                         [ 0.2, -0.2,  0.0],
                         [-0.2, -0.2,  0.0]]
        self.vertex_count = len(self.position_data)
        position_attribute = Attribute('vec3', self.position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        cx = sum(v[0] for v in self.position_data) / self.vertex_count
        cy = sum(v[1] for v in self.position_data) / self.vertex_count
        cz = 0.0
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.center = Uniform('vec3', [cx, cy, cz])
        self.center.locate_variable(self.program_ref, 'center')

        self.angle = Uniform('float', 0.0)
        self.angle.locate_variable(self.program_ref, 'angle')

        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

        self.orbit_radius = 0.75
        self.orbit_speed = 1.0   # radians per second
        self.spin_speed = 2.0

    def update(self):
        """ Update data """
        t = self.time
        self.translation.data[0] = 0.75 * math.cos(self.time)
        self.translation.data[1] = 0.75 * math.sin(self.time)
        self.angle.data = self.spin_speed * t
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.center.upload_data()
        self.angle.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()