import torch
import numpy as np
from transformers import pipeline

print(f"NumPy version: {np.__version__}")
print(f"Torch version: {torch.__version__}")

try:
    chatbot = pipeline("text-generation", model="gpt2")
    print("GPT-2 model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
