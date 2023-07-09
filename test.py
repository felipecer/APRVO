#!/usr/bin/env python3
import rvo2
import time
import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import json
from serialization.objects import Environment, Agent, Obstacle
import serialization.utils as ser_utils
print("Imports successful!") # If you see this printed to the console then installation was successful





environment = ser_utils.make_prebuilt_env("square")

def InitGL():
    glShadeModel(GL_SMOOTH);                            # Enable Smooth Shading
    glClearColor(0.5, 0.5, 0.5, 0.5);               # Black Background
    glClearDepth(1.0);                                 # Depth Buffer Setup
    glEnable(GL_DEPTH_TEST);                            # Enables Depth Testing
    glDepthFunc(GL_LEQUAL);                             # The Type Of Depth Testing To Do
    glEnable ( GL_COLOR_MATERIAL );
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    q = width/height
    gluOrtho2D(-10, 10, 20, 40)
    #gluOrtho2D(-q*10, q*10, 10, 50 )
    glMatrixMode(GL_MODELVIEW)

def idle():
    glutPostRedisplay()

def renderBitmapString(x,y, font, nombre):    
    glRasterPos2f(x,y)
    for c in range (nombre):
        glutBitmapCharacter(font, *c)

def showScreen():
    glLineWidth(2)
    glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

    for step in range(2000):
        sim.doStep()
        time.sleep(0.01)

        positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
                 for agent_no in range(len(agents))]
        print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

        glMatrixMode(GL_MODELVIEW)
        

        for agent_no in range(len(agents)):
            glPushMatrix()
            glTranslatef(*sim.getAgentPosition(agent_no),0)
            glColor3f(0.4,0.9,0.0)
            glutSolidSphere(0.4,8,8)
            glDisable( GL_LIGHTING )
            glColor3f(0,0,0)       
            #glBegin(GL_LINES)
            #glVertex3f(0,0,1.0)
            #RVO::Vector2 pfrev=  sim->getAgentPrefVelocity(i);
            #glVertex3f(pfrev.x(),pfrev.y(),1.0)
            #glEnd()
            glColor3f(0,0,0)
            glPopMatrix()
        
        glMatrixMode(GL_MODELVIEW)

        glPushMatrix();
        glTranslatef(0, 0, 0.0);
        glColor3f(0.0, 0.0, 0.0);

        for i in range(number_obstacles):
            glBegin(GL_QUADS);
            for j in range(len(environment.obstacles[i].polygon)):
                glVertex2f(environment.obstacles[i].polygon[j][0],environment.obstacles[i].polygon[j][1]);
            glEnd();
                
        glPopMatrix();
        glutSwapBuffers()
        glutPostRedisplay()  

    
    glutLeaveMainLoop()     



sim = rvo2.PyRVOSimulator(1/50., 15, 10, 5, 1.3, 0.4, 1.5)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
agents = []
for data in environment.agents:
    if data.neighborDist == 0:
        agent = sim.addAgent(tuple(data.position))
    else:
        agent = sim.addAgent(tuple(data.position), data.neighborDist, data.maxNeighbors, data.timeHorizon, data.timeHorizonObst, data.radius, data.maxSpeed, data.velocity)
    agents.append(agent)



# Obstacles are also supported.
#o1 = sim.addObstacle([(0.1, 0.1), (-0.1, 0.1), (-0.1, -0.1)])
number_obstacles = 0
for vertices in environment.obstacles:
    obstacle = sim.addObstacle(vertices.polygon)
    number_obstacles = number_obstacles + 1


sim.processObstacles()

for i in range(len(environment.agents)):
    sim.setAgentPrefVelocity(agents[i], tuple(environment.agents[i].prefVelocity))



print('Simulation has %i agents and %i obstacle vertices in it.' %
      (sim.getNumAgents(), sim.getNumObstacleVertices()))

print('Running simulation')


glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # Set the display mode to be colored
glutInitWindowSize(1024, 768)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("MRS2023") # Give your window a title
glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)
InitGL();
glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glutReshapeFunc(reshape)
glutIdleFunc(idle)     #showScreen Draw any graphics or shapes in the showScreen function at all times
glutMainLoop()
print("Each agent has ", sim.getAgentRadius(1))

#for step in range(20):
#    sim.doStep()

#    positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
#                 for agent_no in (agen[0], agen[1], agen[2], agen[3])]
#    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))

