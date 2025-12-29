#!/usr/bin/python3
import math
import OpenGL.GL as GL
from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform

class Example(Base):
    """Mode B — Compare T·R vs R·T (global vs local motion)"""
    def initialize(self):
        vs_code = """
        in vec3 position;
        uniform float angle;
        uniform vec2 translation;
        uniform bool applyTR; // true = T·R, false = R·T
        void main() {
            float c = cos(angle), s = sin(angle);
            mat2 R = mat2(c, -s, s, c);
            vec2 pos = position.xy;
            if (applyTR)
                pos = R * pos + translation;  // M1 = T·R (global)
            else
                pos = R * (pos + translation); // M2 = R·T (local)
            gl_Position = vec4(pos, position.z, 1.0);
        }
        """
        fs_code = "uniform vec3 baseColor; out vec4 fragColor; void main(){fragColor=vec4(baseColor,1.0);}"
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0,0,0,1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)
        self.position_data = [[0,0.2,0],[0.2,-0.2,0],[-0.2,-0.2,0]]
        self.vertex_count = len(self.position_data)
        Attribute('vec3', self.position_data).associate_variable(self.program_ref,'position')

        self.angle = Uniform('float', 0.0); self.angle.locate_variable(self.program_ref,'angle')
        self.translation = Uniform('vec2', [0,0]); self.translation.locate_variable(self.program_ref,'translation')
        self.applyTR = Uniform('bool', True); self.applyTR.locate_variable(self.program_ref,'applyTR')
        self.base_color = Uniform('vec3',[1,0,0]); self.base_color.locate_variable(self.program_ref,'baseColor')
        self.spin_speed = 2.0; self.move_radius = 0.4

    def update(self):
        t = self.time; θ = self.spin_speed * t
        GL.glClear(GL.GL_COLOR_BUFFER_BIT); GL.glUseProgram(self.program_ref)
        self.angle.data = θ

        # M1 = T·R (global)
        self.applyTR.data = True
        self.translation.data = [-0.6, 0.0]
        self.base_color.data = [1,0,0]
        self.angle.upload_data(); self.translation.upload_data()
        self.applyTR.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)

        # M2 = R·T (local)
        self.applyTR.data = False
        self.translation.data = [0.6, 0.0]
        self.base_color.data = [0,0.6,1]
        self.angle.upload_data(); self.translation.upload_data()
        self.applyTR.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)

        if int(self.time) != int(self.time - self.delta_time):
            print("Left: T·R = global motion (object moves in world coords)\n"
                  "Right: R·T = local motion (translation relative to object)")

Example().run()
