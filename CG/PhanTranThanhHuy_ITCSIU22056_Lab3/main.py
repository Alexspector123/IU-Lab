#!/usr/bin/python3
import math
import numpy as np
import OpenGL.GL as GL
from py3d.core.base import Base
from py3d.core.utils import Utils
from py3d.core.attribute import Attribute
from py3d.core.uniform import Uniform

# ================= Helper =================
def rigid_fit_2d(P, Q):
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

# ================= Main App =================
class MainApp(Base):
    def initialize(self):
        print("Press 1/2/3 to switch mode: 1=ModeA, 2=ModeB, 3=ModeC")
        self.mode = 1

        self.setup_modeA()
        self.setup_modeB()
        self.setup_modeC()

    # ---------------- Mode A ----------------
    def setup_modeA(self):
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
        self.programA = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0, 0, 0, 1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)
        self.posA = [[0.0,0.2,0.0],[0.2,-0.2,0.0],[-0.2,-0.2,0.0]]
        Attribute('vec3', self.posA).associate_variable(self.programA,'position')

        cx = sum(v[0] for v in self.posA)/len(self.posA)
        cy = sum(v[1] for v in self.posA)/len(self.posA)
        self.centerA = Uniform('vec3', [cx, cy, 0.0]); self.centerA.locate_variable(self.programA,'center')
        self.translationA = Uniform('vec3', [0,0,0]); self.translationA.locate_variable(self.programA,'translation')
        self.angleA = Uniform('float', 0.0); self.angleA.locate_variable(self.programA,'angle')
        self.base_colorA = Uniform('vec3',[1,0,0]); self.base_colorA.locate_variable(self.programA,'baseColor')

        self.spin_speedA = 2.0
        self.center_speedA = 0.5

    # ---------------- Mode B ----------------
    def setup_modeB(self):
        vs_code = """
        in vec3 position;
        uniform float angle;
        uniform vec2 translation;
        uniform bool applyTR;
        void main() {
            float c = cos(angle), s = sin(angle);
            mat2 R = mat2(c, -s, s, c);
            vec2 pos = position.xy;
            if (applyTR)
                pos = R * pos + translation;
            else
                pos = R * (pos + translation);
            gl_Position = vec4(pos, position.z, 1.0);
        }
        """
        fs_code = "uniform vec3 baseColor; out vec4 fragColor; void main(){fragColor=vec4(baseColor,1.0);}"
        self.programB = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0,0,0,1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)
        self.posB = [[0,0.2,0],[0.2,-0.2,0],[-0.2,-0.2,0]]
        Attribute('vec3', self.posB).associate_variable(self.programB,'position')

        self.angleB = Uniform('float',0.0); self.angleB.locate_variable(self.programB,'angle')
        self.translationB = Uniform('vec2',[0,0]); self.translationB.locate_variable(self.programB,'translation')
        self.applyTR = Uniform('bool', True); self.applyTR.locate_variable(self.programB,'applyTR')
        self.base_colorB = Uniform('vec3',[1,0,0]); self.base_colorB.locate_variable(self.programB,'baseColor')

        self.spin_speedB = 2.0
        self.move_radiusB = 0.4

    # ---------------- Mode C ----------------
    def setup_modeC(self):
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
        self.programC = Utils.initialize_program(vs_code, fs_code)
        GL.glClearColor(0,0,0,1)

        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)

        # Tam giác
        self.P = np.array([[0,0,0],[0.2,-0.2,0],[-0.2,-0.2,0]])
        self.Q = np.array([[0.1,0.1,0],[0.3,-0.1,0],[-0.1,-0.3,0]])
        self.R, self.t, self.P_fit, self.rmse = rigid_fit_2d(self.P[:,:2], self.Q[:,:2])
        self.P_fit = np.hstack([self.P_fit, np.zeros((3,1))])
        print("Rigid fit RMSE:", self.rmse)

        self.attrP = Attribute('vec3', self.P); self.attrP.associate_variable(self.programC,'position')
        self.attrQ = Attribute('vec3', self.Q); self.attrQ.associate_variable(self.programC,'position')
        self.attrFit = Attribute('vec3', self.P_fit); self.attrFit.associate_variable(self.programC,'position')

        self.angleC = Uniform('float',0.0); self.angleC.locate_variable(self.programC,'angle')
        self.translationC = Uniform('vec2',[0,0]); self.translationC.locate_variable(self.programC,'translation')
        self.base_colorC = Uniform('vec3',[1,0,0]); self.base_colorC.locate_variable(self.programC,'baseColor')

        self.spin_speedC = 2.0
        self.move_radiusC = 0.5

    # ---------------- Update ----------------
    def update(self):
        # Switch mode
        if self.input.is_key_pressed('1'): self.mode=1
        if self.input.is_key_pressed('2'): self.mode=2
        if self.input.is_key_pressed('3'): self.mode=3

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        t = self.time

        # --- Mode A ---
        if self.mode==1:
            GL.glUseProgram(self.programA)
            theta = self.spin_speedA * t
            self.angleA.data = theta
            # Move pivot
            dist = self.center_speedA * self.delta_time
            if self.input.is_key_pressed('j'): self.centerA.data[0] -= dist
            if self.input.is_key_pressed('l'): self.centerA.data[0] += dist
            if self.input.is_key_pressed('i'): self.centerA.data[1] += dist
            if self.input.is_key_pressed('k'): self.centerA.data[1] -= dist
            if self.input.is_key_pressed('h'): self.spin_speedA += 0.5*self.delta_time
            if self.input.is_key_pressed('n'): self.spin_speedA = max(0.5, self.spin_speedA-0.5*self.delta_time)
            self.centerA.upload_data(); self.translationA.upload_data()
            self.angleA.upload_data(); self.base_colorA.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)

        # --- Mode B ---
        elif self.mode==2:
            GL.glUseProgram(self.programB)
            theta = self.spin_speedB * t
            self.angleB.data = theta
            # M1
            self.applyTR.data = True
            self.translationB.data = [-0.6,0.0]
            self.base_colorB.data = [1,0,0]
            self.angleB.upload_data(); self.translationB.upload_data()
            self.applyTR.upload_data(); self.base_colorB.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES,0,3)
            # M2
            self.applyTR.data = False
            self.translationB.data = [0.6,0.0]
            self.base_colorB.data = [0,0.6,1]
            self.angleB.upload_data(); self.translationB.upload_data()
            self.applyTR.upload_data(); self.base_colorB.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES,0,3)

        # --- Mode C ---
        elif self.mode==3:
            GL.glUseProgram(self.programC)
            theta = self.spin_speedC * t
            tx = self.move_radiusC * math.sin(t)
            ty = self.move_radiusC * math.cos(t)
            self.angleC.data = theta
            self.translationC.data = [tx,ty]
            # P
            self.base_colorC.data = [1.0,0.6,0.0]
            self.translationC.data = [-0.6,0.0]
            self.attrP.associate_variable(self.programC,'position')
            self.angleC.upload_data(); self.translationC.upload_data(); self.base_colorC.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES,0,3)
            # Q
            self.base_colorC.data = [0.5,1.0,0.5]
            self.translationC.data = [0.0,0.0]
            self.attrQ.associate_variable(self.programC,'position')
            self.angleC.data = 0.0
            self.angleC.upload_data(); self.translationC.upload_data(); self.base_colorC.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES,0,3)
            # P_fit
            self.base_colorC.data = [0.5,0.8,1.0]
            self.translationC.data = [0.6,0.0]
            self.attrFit.associate_variable(self.programC,'position')
            self.angleC.data = theta
            self.angleC.upload_data(); self.translationC.upload_data(); self.base_colorC.upload_data()
            GL.glDrawArrays(GL.GL_TRIANGLES,0,3)

# ================= Run =================
if __name__ == "__main__":
    MainApp().run()
