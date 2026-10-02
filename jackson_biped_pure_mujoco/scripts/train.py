# Copyright (c) 2026, Jackson Bipedal Research Project.
# Pure MuJoCo Training Script (Zero Isaac / Omniverse Dependencies).

import gymnasium as gym
import torch
import jackson_biped.envs
from jackson_biped.algo import ActorCritic

def main():
    print("[INFO] Creating pure MuJoCo Gymnasium environment: JacksonBiped-v0")
    env = gym.make("JacksonBiped-v0")
    
    obs_dim = env.observation_space.shape[0]
    act_dim = env.action_space.shape[0]
    
    print(f"[INFO] Observation space dimension: {obs_dim}")
    print(f"[INFO] Action space dimension:      {act_dim}")
    
    policy = ActorCritic(obs_dim, act_dim)
    print("[INFO] Policy network initialized successfully!")
    
    obs, _ = env.reset()
    print(f"[INFO] Environment reset successful. Initial obs shape: {obs.shape}")
    
    # Run a test dummy rollout step
    action = env.action_space.sample()
    next_obs, reward, terminated, truncated, _ = env.step(action)
    print(f"[INFO] Test step executed! Reward: {reward:.4f}, Terminated: {terminated}")
    
    env.close()
    print("[INFO] MuJoCo simulation environment shut down cleanly.")

if __name__ == "__main__":
    main()
