import gym
from collections import namedtuple
import numpy as np

e = gym.make("FrozenLake-v1")

print(e.observation_space)
print(e.action_space)

e.reset()
e.render()