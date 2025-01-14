import streamlit as st
from transformers import pipeline, set_seed

# Load the GPT-2 model with seed for consistent responses
set_seed(42)
chatbot = pipeline("text-generation", model="gpt2")

# Streamlit interface
st.title("Sakhi: Your Intelligent AI Companion")
st.subheader("Ask me anything!")

if "memory" not in st.session_state:
    st.session_state.memory = []

user_input = st.text_input("Your Question:", key="input")

if st.button("Submit"):
    if user_input:
        # Include session memory for better context
        context = " ".join(st.session_state.memory[-3:])  # Keep the last 3 exchanges
        prompt = f"{context} {user_input}"
        try:
            response = chatbot(prompt, max_length=50, num_return_sequences=1, pad_token_id=50256)
            answer = response[0]["generated_text"]
            st.session_state.memory.append(user_input)
            st.session_state.memory.append(answer)
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
