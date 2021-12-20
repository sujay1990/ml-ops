
import gym
import collections

from numpy_torch import Y

ENV_NAME = "FrozenLake-v1"
GAMMA = 0.9
ALPHA = 0.2
TEST_EPISODES = 20

env = gym.make(ENV_NAME)
state = env.reset()
values = collections.defaultdict(float).get[(1,1)]
action_space = env.action_space
print(values)
print(state)
print(env)
print(action_space)