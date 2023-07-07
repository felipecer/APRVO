import json

class Agent:
    @property
    def position(self):
        return self._position
    @property
    def name(self):
        return self._name
    @property
    def neighborDist(self):
        return self._neighborDist
    @property
    def maxNeighbors(self):
        return self._maxNeighbors
    @property
    def timeHorizon(self):
        return self._timeHorizon
    @property
    def timeHorizonObst(self):
        return self._timeHorizonObst
    @property
    def radius(self):
        return self._radius 
    @property
    def maxSpeed(self):
        return self._maxSpeed
    @property
    def velocity(self):
        return self._velocity
    @property
    def prefVelocity(self):
        return self._prefVelocity
    @property
    def goal(self):
        return self._goal

    def __init__(self, name, position, neighborDist, maxNeighbors, timeHorizon, timeHorizonObst, radius, maxSpeed, velocity, prefVelocity, goal):
        self._name = name
        self._position = position
        self._neighborDist = neighborDist
        self._maxNeighbors = maxNeighbors
        self._timeHorizon = timeHorizon
        self._timeHorizonObst = timeHorizonObst
        self._radius = radius
        self._maxSpeed = maxSpeed
        self._velocity = velocity
        self._prefVelocity = prefVelocity
        self._goal = goal

    def get_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "neighborDist": self.neighborDist,
            "maxNeighbors": self.maxNeighbors,
            "timeHorizon": self.timeHorizon,
            "timeHorizonObst": self.timeHorizonObst,
            "radius": self.radius,
            "maxSpeed": self.maxSpeed,
            "velocity": self.velocity,
            "prefVelocity" : self.prefVelocity,
            "goal": self.goal
        }

    def __iter__(self):
        yield from self.get_dict().items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()
    
    @classmethod
    def from_json(cls,json_dct):
        name = json_dct['name']  
        position = json_dct['position']
        if 'neighborDist' in json_dct.keys():
            neighborDist  = json_dct['neighborDist']
        if 'maxNeighbors' in json_dct.keys():
            maxNeighbors  = json_dct['maxNeighbors']
        if 'timeHorizon' in json_dct.keys():
            timeHorizon  = json_dct['timeHorizon']
        if 'timeHorizonObst' in json_dct.keys():
            timeHorizonObst  = json_dct['timeHorizonObst']
        if 'radius' in json_dct.keys():
            radius  = json_dct['radius']
        if 'maxSpeed' in json_dct.keys():
            maxSpeed  = json_dct['maxSpeed']
        if 'velocity' in json_dct.keys():
            velocity  = json_dct['velocity']
        prefVelocity = json_dct['prefVelocity']
        goal = json_dct['goal']
        if 'neighborDist' in json_dct.keys():
            return cls(name, position, neighborDist, maxNeighbors, timeHorizon, timeHorizonObst, radius, maxSpeed, velocity, prefVelocity, goal)
        else:
            return cls(name, position, 0,0,0,0,0,0,(0,0), prefVelocity, goal)

class Obstacle():
    def __init__(self, name, polygon):
        self.name = name
        self.polygon = polygon

    def get_dict(self):
        return {
            "name": self.name,
            "polygon": self.polygon
        }
    def __iter__(self):
        yield from self.get_dict().items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()
    
    @classmethod
    def from_json(cls,json_dct):
        name = json_dct['name']
        polygon = json_dct["polygon"]
        return cls(name, polygon)

class Environment:
    @property
    def name(self): 
        return self._name
    @property
    def agents(self): 
        return self._agents
    @property
    def obstacles(self): 
        return self._obstacles

    def __init__(self, name, agents, obstacles):
        self._name = name
        self._agents = agents
        self._obstacles = obstacles

    def get_dict(self):
        return {
            "name": self.name,
            "agents": self.agents,
            "obstacles": self.obstacles
        }

    def __iter__(self):
        yield from self.get_dict().items()

    def __str__(self):
        env = { 
            "environment": {
                "name": self.name, 
                "agents": [ agent.get_dict() for agent in self.agents], 
                "obstacles": [ obstacle.get_dict() for obstacle in self.obstacles]
                }
            }
        return json.dumps(env, ensure_ascii=False, indent=True)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    @classmethod
    def from_json(cls, json_data):
        name = json_data['environment']['name']
        agents = list(map(Agent.from_json, json_data['environment']["agents"]))
        obstacles = list(map(Obstacle.from_json, json_data['environment']["obstacles"]))
        return cls(name, agents, obstacles)