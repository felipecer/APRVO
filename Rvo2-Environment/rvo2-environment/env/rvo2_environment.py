from pettingzoo.utils.env import ParallelEnv
import functools
from hallway_env import HallwayEnv

class Rvo2Environment(ParallelEnv):
    metadata = {
        "name": "rvo2_environment_v0",
    }

    def __init__(self):
        self.env = HallwayEnv()
        self.env.setup_agents()

    def reset(self, seed=None, options=None):
        self.env.setup_agents()
        observations = self.env.get_env_state()
        return observations, {}

    def step(self, actions):
        self.env.set_agents_pref_velocity(actions)
        self.env.sim.doStep()        
        observations = self.env.get_env_state()        
        return observations, rewards, terminations, truncations, infos

    def render(self): 
        self.env.monitor_agents()

    @functools.lru_cache(maxsize=None)    
    def observation_space(self, agent):
        return self.observation_spaces[agent]

    @functools.lru_cache(maxsize=None)
    def action_space(self, agent):
        return self.action_spaces[agent]