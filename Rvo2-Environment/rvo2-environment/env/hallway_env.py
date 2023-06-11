import rvo2
import random
import math
import numpy as np

class HallwayEnv():
    def __init__(self) -> None:
        random.seed()
        self.M_PI = 3.14159265358979323846
        self.RAND_MAX = 32767
        self.sim = rvo2.PyRVOSimulator(1/50., 15, 10, 5, 1.3, 0.4, 1.5)       
        self.agents = {
            'Agent0': self.sim.addAgent((-10, 28)),
            'Agent1': self.sim.addAgent((10, 28), 15, 10, 5, 1.3, 0.4, 1.5, (0, 0))
        }

        self.obstacles = { 
            'O1': self.sim.addObstacle([(8.0, 29.0), (-8.0, 29.0), (-8.0, 28.42),(8.0, 28.42)]),
            'O2': self.sim.addObstacle([(8.0, 27.58), (-8.0, 27.58), (-8.0, 27.0),(8.0, 27.0)]),
            'O3': self.sim.addObstacle([(8, 40), (7.5, 40), (7.5, 29), (8,29)]),
            'O4': self.sim.addObstacle([(8, 27), (7.5, 27), (7.5, 0), (8,0)]),
            'O5': self.sim.addObstacle([(-7.5, 40), (-8, 40), (-8, 29), (-7.5,29)]),
            'O6': self.sim.addObstacle([(-7.5, 27), (-8, 27), (-8, 0), (-7.5,0)])
        }
        self.sim.processObstacles()
        self.goal = 0        
   
    def setup_agents(self):        
        ## resetear las posiciones
        pert_agent_0= random.random() * self.RAND_MAX
        pert_agent_1= random.random() * self.RAND_MAX        
        angle_0 = -0.5 + pert_agent_0 * 2.0 * self.M_PI / self.RAND_MAX
        dist_0 = pert_agent_0 * 0.01 / self.RAND_MAX
        angle_1 = -0.5+pert_agent_1 * 2.0 * self.M_PI / self.RAND_MAX
        dist_1 = pert_agent_1 * 0.01 / self.RAND_MAX
        self.sim.setAgentPrefVelocity(self.agents['Agent0'], (1 + dist_0 * math.cos(angle_0), 0 + dist_0 * math.sin(angle_0)))
        self.sim.setAgentPrefVelocity(self.agents['Agent1'], (-1 + dist_1 * math.cos(angle_1), 0 + dist_1 * math.sin(angle_1)))
    
    def set_agents_pref_velocity(self, velocities):
        pert_agent_0 = random.random() * self.RAND_MAX
        pert_agent_1 = random.random() * self.RAND_MAX        
        angle_0 = -0.5 + pert_agent_0 * 2.0 * self.M_PI / self.RAND_MAX
        dist_0 = pert_agent_0 * 0.01 * velocities[0] / self.RAND_MAX
        angle_1 = -0.5 + pert_agent_1 * 2.0 * self.M_PI / self.RAND_MAX
        dist_1 = pert_agent_1 * 0.01 * velocities[1] / self.RAND_MAX
        self.sim.setAgentPrefVelocity(self.agents['Agent0'], (1 + dist_0 * math.cos(angle_0), 0 + dist_0 * math.sin(angle_0)))
        self.sim.setAgentPrefVelocity(self.agents['Agent1'], (-1 + dist_1 * math.cos(angle_1), 0 + dist_1 * math.sin(angle_1)))      

    def get_env_state(self):  
        # posición relativa agentes
        agent_positions = []
        # velocidad relativa
        agent_rel_vel = []
        # posición relativa de obstaculos
        obst_positions = []
        # distancia al objetivo        
        distance_to_goal = []
        # distancia al inicio
        distance_to_start = []
        return np.concatenate(agent_positions, agent_rel_vel, obst_positions, distance_to_goal, distance_to_start)
    
    def get_rewards(self):
        pass                        

    def monitor_agents(self):        
        print("Agent 0 preferred velocity: ", self.sim.getAgentPrefVelocity(self.agents['Agent0']))
        print("Agent 1 preferred velocity: ", self.sim.getAgentPrefVelocity(self.agents['Agent1']))
        print('Simulation has %i agents and %i obstacle vertices in it.' % (self.sim.getNumAgents(), self.sim.getNumObstacleVertices()))
        print('Running simulation')


