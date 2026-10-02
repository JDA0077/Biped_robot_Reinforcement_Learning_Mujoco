import gymnasium as gym
from jackson_biped.envs.jackson_biped_env import JacksonBipedEnv

gym.register(
    id="JacksonBiped-v0",
    entry_point="jackson_biped.envs:JacksonBipedEnv",
)
