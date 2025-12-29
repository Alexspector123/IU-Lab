#!/usr/bin/python3
import OpenGL.GL as GL
import math

from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform


class Example(Base):
    """ Animate a triangle moving across screen """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            uniform float angle;
            void main()
            {
                // rotation matrix
                float c = cos(angle);
                float s = sin(angle);
                mat2 R = mat2(c, -s, s, c);

                // apply rotation + translation
                vec2 rotated = R * position.xy;
                vec2 world = rotated + translation.xy;

                gl_Position = vec4(world, position.z, 1.0);
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
        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        position_data = [[ 0.0,  0.2,  1],
                         [ 0.2, -0.2,  0.0],
                         [-0.2, -0.2,  0.0]]
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.angle = Uniform('float', 0.0)
        self.angle.locate_variable(self.program_ref, 'angle')

        self.linear_pos = -1
        self.orbit_radius = 0.75

    def update(self):
        """ Update data """
        t = self.time
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)

        # --- Triangle 1: moves linearly across screen ---
        self.linear_pos += 0.02
        if self.linear_pos > 1.2:
            self.linear_pos = -1.2

        self.translation.data = [self.linear_pos, 0.0, 0.0]
        self.angle.data = t * 3.0
        self.base_color.data = [1.0, 0.0, 0.0]  # Red
        self.translation.upload_data()
        self.angle.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)

        # --- Triangle 2: orbits around origin ---
        tx = self.orbit_radius * math.cos(t)
        ty = self.orbit_radius * math.sin(t)
        self.translation.data = [tx, ty, 0.0]
        self.angle.data = 0.0
        self.base_color.data = [0.0, 0.5, 1.0]  # Blue
        self.translation.upload_data()
        self.angle.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()
