# Copyright (c) 2026, Jackson Bipedal Research Project.
# Standalone Gymnasium Environment using Pure MuJoCo.

import os
import numpy as np
import gymnasium as gym
from gymnasium import spaces
import mujoco

from jackson_biped.actuators.actuator_pd import IdentifiedActuatorPD

class JacksonBipedEnv(gym.Env):
    """
    Native MuJoCo Bipedal Locomotion Environment 
    """
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 50}

    def __init__(self, render_mode=None):
        super().__init__()
        
        # Load MuJoCo Model
        model_path = os.path.join(os.path.dirname(__file__), "../models/jackson_biped.xml")
        self.model = mujoco.MjModel.from_xml_path(model_path)
        self.data = mujoco.MjData(self.model)
        
        self.render_mode = render_mode
        self.dt = self.model.opt.timestep * 10  # 50 Hz control loop (decimation = 10)
        self.actuator = IdentifiedActuatorPD()
        
        # Default joint targets (12 DOFs)
        self.default_dof_pos = np.zeros(12)
        
        # Target velocity command [vx_cmd, vy_cmd, yaw_rate_cmd]
        self.command = np.array([0.5, 0.0, 0.0])
        
        # Action space: 12 motor target positions relative to default
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(12,), dtype=np.float32)
        
        # Observation space: base lin vel (3), base ang vel (3), gravity proj (3), target cmd (3), joint pos (12), joint vel (12), prev actions (12)
        num_obs = 3 + 3 + 3 + 3 + 12 + 12 + 12
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(num_obs,), dtype=np.float32)
        
        self.last_action = np.zeros(12)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        mujoco.mj_resetData(self.model, self.data)
        
        # Initial torso pose
        self.data.qpos[2] = 0.85  # Z height
        self.data.qpos[7:] = self.default_dof_pos  # Joint positions
        
        mujoco.mj_forward(self.model, self.data)
        self.last_action = np.zeros(12)
        
        # Resample command
        self.command = np.array([
            np.random.uniform(-0.5, 1.0),
            np.random.uniform(-0.3, 0.3),
            np.random.uniform(-0.5, 0.5)
        ])
        
        return self._get_obs(), {}

    def step(self, action):
        scaled_action = action * 0.5 + self.default_dof_pos
        
        # Step physics with PD actuator control
        for _ in range(10):
            current_qpos = self.data.qpos[7:]
            current_qvel = self.data.qvel[6:]
            torques = self.actuator.compute_torques(scaled_action, current_qpos, current_qvel)
            self.data.ctrl[:] = torques
            mujoco.mj_step(self.model, self.data)
            
        self.last_action = action.copy()
        
        obs = self._get_obs()
        reward = self._compute_reward(action)
        terminated = self._check_terminated()
        
        return obs, reward, terminated, False, {}

    def _get_obs(self):
        base_lin_vel = self.data.qvel[0:3]
        base_ang_vel = self.data.qvel[3:6]
        
        # Joint states
        qpos = self.data.qpos[7:]
        qvel = self.data.qvel[6:]
        
        # Simple projected gravity placeholder [0, 0, -1]
        proj_gravity = np.array([0.0, 0.0, -1.0])
        
        obs = np.concatenate([
            base_lin_vel,
            base_ang_vel,
            proj_gravity,
            self.command,
            qpos,
            qvel,
            self.last_action
        ]).astype(np.float32)
        
        return obs

    def _compute_reward(self, action):
        base_lin_vel = self.data.qvel[0:2]  # XY velocity
        target_lin_vel = self.command[0:2]
        
        # 1. Velocity tracking reward
        vel_err = np.sum(np.square(target_lin_vel - base_lin_vel))
        r_vel = np.exp(-vel_err / 0.25)
        
        # 2. Base Z velocity penalty
        r_z_vel = -2.0 * np.square(self.data.qvel[2])
        
        # 3. Action rate / torque penalty
        r_action = -0.01 * np.sum(np.square(action - self.last_action))
        
        return float(r_vel + r_z_vel + r_action)

    def _check_terminated(self):
        # Terminate if torso falls below 0.4 meters
        torso_z = self.data.qpos[2]
        return bool(torso_z < 0.4 or torso_z > 1.3)
