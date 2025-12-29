# Exercise 4B Starter - Pentagram (Complete) + Labels
import math
from OpenGL.GL import *
from OpenGL.GLUT import glutMainLoop
from window_glut import Simple2DApp

def star_points_regular(cx, cy, R):
    # TODO: compute outer[5] and inner[5] with r = R * sin(18deg)/sin(54deg)
    r = R * math.sin(math.radians(18)) / math.sin(math.radians(54))
    outer, inner = [], []

    for i in range(5):
        angle_outer = math.radians(90 + i*72)
        angle_inner = math.radians(90 + i*72 + 36)
        ox = cx + R * math.cos(angle_outer)
        oy = cy + R * math.sin(angle_outer)
        ix = cx + r * math.cos(angle_inner)
        iy = cy + r * math.sin(angle_inner)
        outer.append((ox, oy))
        inner.append((ix, iy))
    return outer, inner

class App(Simple2DApp):
    def draw(self):
        W,H = self.width, self.height
        cx, cy = W*0.5, H*0.55
        R = min(W, H) * 0.32

        # TODO: get outer, inner = star_points_regular(cx, cy, R)
        outer, inner = star_points_regular(cx, cy, R)
        # TODO: build ring and fill with GL_TRIANGLE_FAN
        glPushMatrix()
        glTranslatef(cx, cy, 0)        
        glRotatef(180, 0, 0, 1)         
        glTranslatef(-cx, -cy, 0)
        glColor3f(1, 1, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        for i in range(5):
            glVertex2f(*outer[i])
            glVertex2f(*inner[i])
        glVertex2f(*outer[0])
        glEnd()
        # TODO: draw pentagram outline using order = [0,2,4,1,3,0]
        glColor3f(0, 0, 0)
        glLineWidth(2)
        order = [0,2,4,1,3,0]
        glBegin(GL_LINE_STRIP)
        for i in order:
            glVertex2f(*outer[i])
        glEnd()
        glFlush()
        # TODO: label p1..p5 near the outer vertices, and add caption
        glColor3f(1, 1, 0)
        for i, (x,y) in enumerate(outer, start=1):
            label = f"p{i} ({x:.0f}, {y:.0f})"
            self.draw_text(x+10, y+10, label, color=(1, 0, 0))

if __name__ == "__main__":
    App(800, 600, b"Ex4B - Pentagram Complete")
    glutMainLoop()
