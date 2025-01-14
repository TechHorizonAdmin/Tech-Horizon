import streamlit as st
from transformers import pipeline

# Ensure NumPy compatibility
import numpy as np
print(f"NumPy version: {np.__version__}")

# Load the GPT-2 model for chatbot functionality
chatbot = pipeline("text-generation", model="gpt2")

# Streamlit interface
st.title("Sakhi: Your Autonomous AI Companion")
user_input = st.text_input("Ask Sakhi anything:")

if st.button("Submit"):
    try:
        response = chatbot(
            user_input, 
            max_length=50, 
            num_return_sequences=1, 
            pad_token_id=50256
        )
        st.write(response[0]["generated_text"])
    except Exception as e:
        st.error(f"An error occurred: {e}")
