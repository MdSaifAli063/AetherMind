from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import PPOTrainer, PPOConfig
import torch
import json

from openenv_env.env import LifeOSEnv
from utils.prompt_builder import build_prompt

# Load scenarios
with open("demo_scenarios.json") as f:
    scenarios = json.load(f)

env = LifeOSEnv(scenarios)

model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

config = PPOConfig(
    learning_rate=1e-5,
    batch_size=2
)

ppo_trainer = PPOTrainer(config, model, tokenizer)

for epoch in range(50):
    state = env.reset()
    memory = env.memory.get_context()

    prompt = build_prompt(state, memory)

    inputs = tokenizer(prompt, return_tensors="pt")
    output_ids = model.generate(**inputs, max_new_tokens=60)

    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    _, reward, _, _ = env.step(output)

    ppo_trainer.step([prompt], [output], [reward])

    print(f"Epoch {epoch} | Reward: {reward}")