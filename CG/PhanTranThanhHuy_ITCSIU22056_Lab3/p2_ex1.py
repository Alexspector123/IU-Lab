from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

angle = 0
M = np.identity(4, dtype=np.float32)

def translate(tx, ty, tz):
    T = np.identity(4, dtype=np.float32)
    T[3, :3] = [tx, ty, tz]
    return T

def rotate_z(theta_deg):
    theta = np.radians(theta_deg)
    R = np.identity(4, dtype=np.float32)
    c, s = np.cos(theta), np.sin(theta)
    R[0,0], R[0,1] = c, s
    R[1,0], R[1,1] = -s, c
    return R

def draw_pyramid():
    global angle, M
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0, 0, -8)
    glRotatef(10, 1, 0, 0)  
    glRotatef(angle, 0, 1, 0)

    glMultMatrixf(M.T)

    glColor3f(0, 1, 0)
    glLineWidth(2)

    h = 2.0
    s = 2.0
    apex = [0.0, h, 0.0]   
    v0 = [-s, 0.0, -s]
    v1 = [ s, 0.0, -s]
    v2 = [ s, 0.0,  s]
    v3 = [-s, 0.0,  s]

    glBegin(GL_LINES)
    glVertex3fv(v0); glVertex3fv(v1)
    glVertex3fv(v1); glVertex3fv(v2)
    glVertex3fv(v2); glVertex3fv(v3)
    glVertex3fv(v3); glVertex3fv(v0)
    for v in [v0, v1, v2, v3]:
        glVertex3fv(apex); glVertex3fv(v)
    glEnd()

    glutSwapBuffers()

def keyboard(key, x, y):
    global M
    key = key.decode('utf-8').lower()
    delta = 0.2
    rot = 5

    if key == 'w':
        M = translate(0, delta, 0) @ M
    elif key == 's':
        M = translate(0, -delta, 0) @ M
    elif key == 'a':
        M = translate(-delta, 0, 0) @ M
    elif key == 'd':
        M = translate(delta, 0, 0) @ M
    elif key == 'z':
        M = translate(0, 0, delta) @ M
    elif key == 'x':
        M = translate(0, 0, -delta) @ M
    elif key == 'q':
        M = rotate_z(rot) @ M
    elif key == 'e':
        M = rotate_z(-rot) @ M

    elif key == 'i':
        M = M @ translate(0, delta, 0)
    elif key == 'k':
        M = M @ translate(0, -delta, 0)
    elif key == 'j':
        M = M @ translate(-delta, 0, 0)
    elif key == 'l':
        M = M @ translate(delta, 0, 0)
    elif key == 'u':
        M = M @ rotate_z(rot)
    elif key == 'o':
        M = M @ rotate_z(-rot)

    glutPostRedisplay()

def update(value):
    global angle
    angle += 0.5
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Wireframe Pyramid")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0,0,0,1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.0,0.1,50.0)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(draw_pyramid)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
