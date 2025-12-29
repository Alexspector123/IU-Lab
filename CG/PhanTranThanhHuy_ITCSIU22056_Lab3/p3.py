from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# --- Pyramid and particles ---
s = 2.0        # base half-side
ay = 2.0       # apex height
N = 500        # number of particles
alpha = 0.999  # damping factor
dt = 1/60.0    # time step
MAX_V = 2.0    # clamp max velocity for stability

positions = np.zeros((N,3), dtype=np.float32)
velocities = np.zeros((N,3), dtype=np.float32)

# Initialize particles inside the pyramid
for i in range(N):
    y = np.random.uniform(0, ay)
    h = s * (1 - y/ay)
    x = np.random.uniform(-h, h)
    z = np.random.uniform(-h, h)
    positions[i] = [x, y, z]
    velocities[i] = np.random.uniform(-0.1, 0.1, size=3)

# Model matrix
M = np.identity(4, dtype=np.float32)

# --- Particle update ---
def update_particles():
    global positions, velocities
    for i in range(N):
        positions[i] += velocities[i] * dt

        # Bounce y walls
        if positions[i,1] < 0:
            positions[i,1] = 0
            velocities[i,1] *= -1
        elif positions[i,1] > ay:
            positions[i,1] = ay
            velocities[i,1] *= -1

        # Current half-width at y
        h_curr = s * (1 - positions[i,1]/ay)

        # Bounce x walls
        if positions[i,0] < -h_curr:
            positions[i,0] = -h_curr
            velocities[i,0] *= -1
        elif positions[i,0] > h_curr:
            positions[i,0] = h_curr
            velocities[i,0] *= -1

        # Bounce z walls
        if positions[i,2] < -h_curr:
            positions[i,2] = -h_curr
            velocities[i,2] *= -1
        elif positions[i,2] > h_curr:
            positions[i,2] = h_curr
            velocities[i,2] *= -1

        # Damping
        velocities[i] *= alpha

        # Clamp velocity for stability
        speed = np.linalg.norm(velocities[i])
        if speed > MAX_V:
            velocities[i] = velocities[i] / speed * MAX_V

# --- Pyramid drawing ---
def draw_pyramid():
    glColor3f(0,1,0)
    glLineWidth(2)
    apex = [0, ay, 0]
    v0 = [-s,0,-s]; v1 = [s,0,-s]; v2 = [s,0,s]; v3 = [-s,0,s]

    glBegin(GL_LINES)
    # Base
    glVertex3fv(v0); glVertex3fv(v1)
    glVertex3fv(v1); glVertex3fv(v2)
    glVertex3fv(v2); glVertex3fv(v3)
    glVertex3fv(v3); glVertex3fv(v0)
    # Sides
    for v in [v0,v1,v2,v3]:
        glVertex3fv(apex); glVertex3fv(v)
    glEnd()

# --- Particle drawing ---
def draw_particles():
    glColor3f(1,1,0)     # yellow
    glPointSize(10)       # bigger points
    glBegin(GL_POINTS)
    for p in positions:
        glVertex3fv(p)
    glEnd()

angle = 0.0
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera
    glTranslatef(0,0,-8)
    glRotatef(10,1,0,0)

    # Apply model matrix
    glMultMatrixf(M.T)

    draw_pyramid()
    draw_particles()
    glutSwapBuffers()

# --- Timer ---
def timer(value):
    update_particles()
    glutPostRedisplay()
    glutTimerFunc(int(dt*1000), timer, 0)

# --- Global / Local translation ---
def translate(tx,ty,tz):
    T = np.identity(4, dtype=np.float32)
    T[:3,3] = [tx,ty,tz]
    return T

def rotate_y(angle_deg):
    rad = np.radians(angle_deg)
    R = np.identity(4, dtype=np.float32)
    R[0,0] = np.cos(rad); R[0,2] = np.sin(rad)
    R[2,0] = -np.sin(rad); R[2,2] = np.cos(rad)
    return R

def keyboard(key,x,y):
    global M
    key = key.decode('utf-8').lower()
    delta = 0.2

    # Global (pre-multiply)
    if key == 'w': M = translate(0,delta,0) @ M
    elif key == 's': M = translate(0,-delta,0) @ M
    elif key == 'a': M = translate(-delta,0,0) @ M
    elif key == 'd': M = translate(delta,0,0) @ M
    elif key == 'z': M = translate(0,0,delta) @ M
    elif key == 'x': M = translate(0,0,-delta) @ M

    # Local (post-multiply)
    elif key == 'i': M = M @ translate(0,delta,0)
    elif key == 'k': M = M @ translate(0,-delta,0)
    elif key == 'j': M = M @ translate(-delta,0,0)
    elif key == 'l': M = M @ translate(delta,0,0)
    elif key == 'u': M = M @ translate(0,0,delta)
    elif key == 'o': M = M @ translate(0,0,-delta)

    elif key == 'q': M = rotate_y(5) @ M   
    elif key == 'e': M = M @ rotate_y(-5)

    glutPostRedisplay()

# --- Main ---
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,800)
    glutCreateWindow(b"Pyramid Particle Simulation - Part C")
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
    glClearColor(0,0,0,1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.0,0.1,50.0)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
