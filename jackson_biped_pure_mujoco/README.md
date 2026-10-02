# 🦾 Jackson Biped (Pure MuJoCo Framework)

A clean, standalone **MuJoCo + Gymnasium + PyTorch** framework for the **Jackson Bipedal Robot**.

> **Note**: This version has **ZERO dependencies on NVIDIA Isaac Lab / Omniverse**. It runs natively on any system (macOS, Linux, Windows) with standard Python and MuJoCo.

## 📁 Project Structure
```text
jackson_biped/
├── jackson_biped/
│   ├── models/
│   │   └── jackson_biped.xml     # MuJoCo MJCF physics model (12 DOFs)
│   ├── actuators/
│   │   └── actuator_pd.py        # Non-linear joint friction motor dynamics
│   ├── envs/
│   │   └── jackson_biped_env.py  # Pure Gymnasium wrapper for MuJoCo
│   └── algo/
│       └── ppo.py                # Standalone PyTorch Actor-Critic PPO architecture
├── scripts/
│   ├── train.py                  # Training pipeline entry point
│   └── simulate.py               # Interactive visual evaluation with native MuJoCo viewer
├── setup.py                      # Pure setup.py (MuJoCo, Gymnasium, PyTorch)
└── README.md
```

## 🚀 Quick Start

### 1. Installation
```bash
pip install -e .
```

### 2. Verify Gymnasium Environment & Run Test Step
```bash
python scripts/train.py
```

### 3. Open Interactive MuJoCo Visualizer
```bash
python scripts/simulate.py
```
