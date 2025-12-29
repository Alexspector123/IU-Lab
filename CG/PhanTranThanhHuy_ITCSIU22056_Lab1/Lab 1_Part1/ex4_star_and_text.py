# Exercise 4A Starter - Star + Caption
import math
from OpenGL.GL import *
from OpenGL.GLUT import glutMainLoop
from window_glut import Simple2DApp

def star_points(cx, cy, R_outer=120, R_inner=50, start_angle_deg=-90):
    # TODO: compute 5 outer and 5 inner points (alternating ring)
    points = []
    for i in range(10):
        ang = math.radians(start_angle_deg + i*36.0)
        R = R_outer if i % 2 == 0 else R_inner
        points.append((cx + R*math.cos(ang), cy + R*math.sin(ang)))
    # return list_of_10_vertices
    return points

class App(Simple2DApp):
    def draw(self):
        W,H = self.width, self.height
        cx, cy = W*0.35, H*0.6

        # TODO: call star_points and build the alternating ring
        points = star_points(cx,cy)
        # TODO: fill star with GL_TRIANGLE_FAN (glBegin/glEnd)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(cx, cy)
        for (x, y) in points:
            glVertex2f(x, y)
        glVertex2f(*points[0])
        glEnd()
        glFlush()
        # TODO: draw outline-only star with self.draw_polyline(..., loop=True)
        self.draw_polyline(points, color=(0,0,0), width=2, loop=True)

        points = star_points(2*cx,cy)
        self.draw_polyline(points, color=(0,0,255), width=4, loop=True)
        # TODO: caption with self.draw_text(..., "This is a star")
        self.draw_text(cx-50, cy-150, "This is a star")
        self.draw_text(2*cx-50, cy-150, "This is a star")

if __name__ == "__main__":
    App(900, 600, b"Ex4A - Star + Text")
    glutMainLoop()
