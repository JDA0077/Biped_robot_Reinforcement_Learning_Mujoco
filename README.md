# 🦾 Jackson Biped (Pure MuJoCo Framework)

A clean, standalone **MuJoCo + Gymnasium + PyTorch** framework for the **Jackson Bipedal Robot**.

> **Note**: This version has **ZERO dependencies on NVIDIA Isaac Lab / Omniverse**. It runs natively on any system (macOS, Linux, Windows) with standard Python and MuJoCo.

## 📁 Project Structure
<img width="768" height="1024" alt="WhatsApp Image 2026-10-02 at 12 18 42 AM" src="https://github.com/user-attachments/assets/f81c5e5e-9d32-45f4-ba21-98343b5657e4" />


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



https://github.com/user-attachments/assets/1cbc2045-13b8-4080-8ae3-42adb99dd7f8



TensorBoard
<img width="512" height="341" alt="image" src="https://github.com/user-attachments/assets/2655bb4e-1ac3-41a1-9e2a-be9c4b491277" />
<img width="500" height="353" alt="Screenshot 2026-10-02 014525" src="https://github.com/user-attachments/assets/986d11bf-afb8-4b2a-a2f4-f829830e933d" />
<img width="1092" height="372" alt="Screenshot 2026-10-02 014500" src="https://github.com/user-attachments/assets/a231acd9-792e-4229-afc2-d84dc9e37dc8" />
<img width="977" height="355" alt="Screenshot 2026-10-02 014321" src="https://github.com/user-attachments/assets/824ae0e8-a6ee-412d-bdbd-aae14993291b" />
<img width="952" height="361" alt="Screenshot 2026-10-02 014353" src="https://github.com/user-attachments/assets/ab7f39ba-e65d-46d3-b61f-bd778a42e831" />
<img width="1127" height="395" alt="Screenshot 2026-10-02 014417" src="https://github.com/user-attachments/assets/b02d5016-79d3-441c-bccd-ff253f5ab908" />
<img width="502" height="370" alt="Screenshot 2026-10-02 014434" src="https://github.com/user-attachments/assets/7a1dc4a0-a50c-46c9-aaad-38afea6b69fa" />
