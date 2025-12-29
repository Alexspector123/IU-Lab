#!/usr/bin/python3
import math
import numpy as np
import OpenGL.GL as GL
from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform

# ===== Helper functions =====
def rigid_fit_2d(P, Q):
    """2D rigid fitting (Kabsch, no scale)"""
    P = np.array(P)
    Q = np.array(Q)
    cP = P.mean(axis=0)
    cQ = Q.mean(axis=0)
    P0 = P - cP
    Q0 = Q - cQ
    H = P0.T @ Q0
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[1,:] *= -1
        R = Vt.T @ U.T
    t = cQ - R @ cP
    P_fit = (R @ P.T).T + t
    rmse = np.sqrt(np.mean(np.sum((P_fit - Q)**2, axis=1)))
    return R, t, P_fit, rmse

class Example(Base):
    """3 tam giác có animation xoay + dịch chuyển"""
    def initialize(self):
        # Vertex shader
        vs_code = """
        in vec3 position;
        uniform float angle;
        uniform vec2 translation;
        void main(){
            float c = cos(angle);
            float s = sin(angle);
            mat2 R = mat2(c, -s, s, c);
            vec2 pos = position.xy;
            pos = R * pos + translation;
            gl_Position = vec4(pos, position.z, 1.0);
        }
        """
        fs_code = "uniform vec3 baseColor; out vec4 fragColor; void main(){fragColor=vec4(baseColor,1.0);}"
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0,0,0,1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)

        # Tam giác gốc P
        self.P = np.array([[0,0,0],[0.2,-0.2,0],[-0.2,-0.2,0]])
        # Tam giác mục tiêu Q
        self.Q = np.array([[0.1,0.1,0],[0.3,-0.1,0],[-0.1,-0.3,0]])
        # Rigid fit
        self.R, self.t, self.P_fit, self.rmse = rigid_fit_2d(self.P[:,:2], self.Q[:,:2])
        self.P_fit = np.hstack([self.P_fit, np.zeros((3,1))])

        print("Rigid fit RMSE:", self.rmse)

        # Attribute
        self.attr_P = Attribute('vec3', self.P); self.attr_P.associate_variable(self.program_ref,'position')
        self.attr_Q = Attribute('vec3', self.Q); self.attr_Q.associate_variable(self.program_ref,'position')
        self.attr_fit = Attribute('vec3', self.P_fit); self.attr_fit.associate_variable(self.program_ref,'position')

        # Uniforms
        self.angle = Uniform('float', 0.0); self.angle.locate_variable(self.program_ref,'angle')
        self.translation = Uniform('vec2',[0,0]); self.translation.locate_variable(self.program_ref,'translation')
        self.base_color = Uniform('vec3',[1,0,0]); self.base_color.locate_variable(self.program_ref,'baseColor')

        # Animation params
        self.spin_speed = 2.0
        self.move_radius = 0.5

    def update(self):
        t = self.time
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)

        # Tính angle và translation cho animation
        theta = self.spin_speed * t
        tx = self.move_radius * math.sin(t)
        ty = self.move_radius * math.cos(t)
        self.angle.data = theta
        self.translation.data = [tx, ty]

        # ---- Draw tam giác P (red) ----
        self.base_color.data = [1.0, 0.6, 0.0]
        self.translation.data = [-0.6, 0.0]
        Attribute('vec3', self.P).associate_variable(self.program_ref,'position')
        self.angle.data = theta  # có thể giữ xoay
        self.angle.upload_data(); self.translation.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES,0,3)

        # ---- Draw tam giác Q (green) ----
        self.base_color.data = [0.5, 1.0, 0.5]
        self.translation.data = [0.0, 0.0]
        Attribute('vec3', self.Q).associate_variable(self.program_ref,'position')
        self.angle.data = 0.0  # không xoay
        self.angle.upload_data(); self.translation.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES,0,3)

        # ---- Draw tam giác P_fit (blue) ----
        self.base_color.data = [0.5, 0.8, 1.0]
        self.translation.data = [0.6, 0.0]
        Attribute('vec3', self.P_fit).associate_variable(self.program_ref,'position')
        self.angle.data = theta
        self.angle.upload_data(); self.translation.upload_data(); self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLES,0,3)

Example().run()
