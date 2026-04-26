# AetherMind Colab Notebook Flow (HF TRL PPO)

Use these cells directly in Google Colab to satisfy the "minimal training script in Colab" judging requirement.

## 1) Clone project

```python
!git clone <YOUR_REPO_URL>
%cd lifeos-v2
```

## 2) Install dependencies

```python
!pip -q install --upgrade pip
!pip -q install -r requirements.txt
```

## 3) Run minimal PPO training (fast mode)

```python
!python training/train_ppo_colab.py --mode fast --epochs 8
```

Optional stronger run:

```python
!python training/train_ppo_colab.py --mode default --epochs 20
```

## 4) Inspect reward logs

```python
import json
from pathlib import Path

log_path = Path("training_outputs/reward_log_colab.json")
data = json.loads(log_path.read_text(encoding="utf-8"))
data[:2], len(data)
```

## 5) Plot reward curve (for judging evidence)

```python
import matplotlib.pyplot as plt

epochs = [row["epoch"] for row in data]
rewards = [row["reward"] for row in data]

plt.figure(figsize=(8,4))
plt.plot(epochs, rewards, marker="o")
plt.title("AetherMind PPO Reward Curve (Colab)")
plt.xlabel("Epoch")
plt.ylabel("Reward")
plt.grid(alpha=0.25)
plt.show()
```

## 6) Export artifact files

```python
!ls -lh training_outputs
```

Expected outputs:
- `training_outputs/reward_log_colab.json`
- `training_outputs/reward_log_colab.csv`

You can attach the plot screenshot and these log files in your judging evidence.

