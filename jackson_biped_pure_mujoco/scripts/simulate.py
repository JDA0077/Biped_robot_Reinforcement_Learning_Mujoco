# Copyright (c) 2026, Jackson Bipedal Research Project.
# Interactive Visualizer for Jackson Biped in MuJoCo.

import gymnasium as gym
import mujoco
import mujoco.viewer
import jackson_biped.envs

def main():
    print("[INFO] Launching MuJoCo interactive viewer...")
    env = gym.make("JacksonBiped-v0")
    obs, _ = env.reset()
    
    # Launch native MuJoCo passive viewer window
    with mujoco.viewer.launch_passive(env.unwrapped.model, env.unwrapped.data) as viewer:
        while viewer.is_running():
            action = env.action_space.sample()
            obs, reward, terminated, truncated, _ = env.step(action)
            
            if terminated:
                obs, _ = env.reset()
                
            viewer.sync()

if __name__ == "__main__":
    main()
