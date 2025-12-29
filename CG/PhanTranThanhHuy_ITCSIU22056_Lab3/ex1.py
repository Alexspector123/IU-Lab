#!/usr/bin/python3
import math
import numpy as np
import OpenGL.GL as GL
from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform

class Example(Base):
    """Mode A — Rotation about an arbitrary pivot"""
    def initialize(self):
        print("Initializing Mode A ...")
        vs_code = """
            in vec3 position;
            uniform vec3 center;
            uniform vec3 translation;
            uniform float angle;
            void main() {
                float c = cos(angle);
                float s = sin(angle);
                mat2 R = mat2(c, -s, s, c);
                vec2 local = position.xy - center.xy;
                vec2 rotated = R * local;
                vec2 world = rotated + center.xy + translation.xy;
                gl_Position = vec4(world, position.z + translation.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main() {
                fragColor = vec4(baseColor, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0, 0, 0, 1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)
        self.position_data = [[0.0,0.2,0.0],[0.2,-0.2,0.0],[-0.2,-0.2,0.0]]
        self.vertex_count = len(self.position_data)
        Attribute('vec3', self.position_data).associate_variable(self.program_ref, 'position')

        cx = sum(v[0] for v in self.position_data)/self.vertex_count
        cy = sum(v[1] for v in self.position_data)/self.vertex_count
        self.center = Uniform('vec3', [cx, cy, 0.0]); self.center.locate_variable(self.program_ref,'center')
        self.translation = Uniform('vec3', [0,0,0]); self.translation.locate_variable(self.program_ref,'translation')
        self.angle = Uniform('float', 0.0); self.angle.locate_variable(self.program_ref,'angle')
        self.base_color = Uniform('vec3',[1,0,0]); self.base_color.locate_variable(self.program_ref,'baseColor')

        self.spin_speed = 2.0
        self.center_speed = 0.5

    def update(self):
        t = self.time
        self.angle.data = self.spin_speed * t

        # move pivot
        dist = self.center_speed * self.delta_time
        if self.input.is_key_pressed('j'): self.center.data[0] -= dist
        if self.input.is_key_pressed('l'): self.center.data[0] += dist
        if self.input.is_key_pressed('i'): self.center.data[1] += dist
        if self.input.is_key_pressed('k'): self.center.data[1] -= dist
        if self.input.is_key_pressed('h'): self.spin_speed += 0.5 * self.delta_time
        if self.input.is_key_pressed('n'): self.spin_speed = max(0.5, self.spin_speed - 0.5 * self.delta_time)

        # Diagnostics every ~1s
        if int(self.time) != int(self.time - self.delta_time):
            θ = self.angle.data
            R = np.array([[math.cos(θ), -math.sin(θ)], [math.sin(θ), math.cos(θ)]])
            err = np.max(np.abs(R.T @ R - np.identity(2)))
            detR = np.linalg.det(R)
            print(f"θ={math.degrees(θ):.1f}°, ||RᵀR−I||∞={err:.2e}, det(R)={detR:.2f}")

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.center.upload_data(); self.translation.upload_data()
        self.angle.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)

Example().run()
