# Copyright (c) 2026, Jackson Bipedal Research Project.
# Pure MuJoCo Actuator Model with Non-Linear Friction Dynamics.

import numpy as np

class IdentifiedActuatorPD:
    """
    PD Motor Controller with non-linear joint friction model.
    Tau = Kp * (q_des - q) - Kd * q_dot - (tau_static * tanh(q_dot / v_act) + tau_dynamic * q_dot)
    """
    def __init__(self, kp=40.0, kd=2.5, friction_static=0.8, friction_dynamic=0.1, activation_vel=0.1):
        self.kp = kp
        self.kd = kd
        self.friction_static = friction_static
        self.friction_dynamic = friction_dynamic
        self.activation_vel = activation_vel

    def compute_torques(self, target_pos: np.ndarray, current_pos: np.ndarray, current_vel: np.ndarray) -> np.ndarray:
        # Standard PD Torque
        pd_torque = self.kp * (target_pos - current_pos) - self.kd * current_vel
        
        # Non-linear static & dynamic joint friction subtraction
        friction_torque = (self.friction_static * np.tanh(current_vel / self.activation_vel) + 
                           self.friction_dynamic * current_vel)
        
        applied_torque = pd_torque - friction_torque
        return applied_torque
