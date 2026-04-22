import random
from .memory import Memory
from .reward import reward_function
from .schema_manager import SchemaManager

class LifeOSEnv:
    def __init__(self, scenarios):
        self.scenarios = scenarios
        self.memory = Memory()
        self.schema_manager = SchemaManager()

    def reset(self):
        self.current = random.choice(self.scenarios)
        self.state = self.schema_manager.apply_schema(self.current)
        return self.state

    def step(self, action):
        reward = reward_function(action, self.current)

        self.memory.add(self.current, action)

        done = True
        info = {"scenario": self.current, "action": action}

        return self.state, reward, done, info