import streamlit as st
from transformers import pipeline
import json
from helper_functions import save_feedback, load_tasks

# Load Fine-Tuned Model
model_name = "Mani0856/sakhi_fine_tuned_model"
sakhi_chatbot = pipeline("text-generation", model=model_name, tokenizer=model_name)

# Generate Response Function
def generate_response(user_input):
    prompt = f"The user is asking: {user_input}. You are an intelligent AI assistant helping them achieve their goals."
    response = sakhi_chatbot(prompt, max_length=100, num_return_sequences=1)
    return response[0]["generated_text"]

# Streamlit App
st.title("Sakhi: Your Intelligent AI Companion")

user_input = st.text_input("Ask Sakhi a question:")

if user_input:
    response = generate_response(user_input)
    st.write(f"Sakhi: {response}")

    # Feedback Section
    rating = st.radio("Rate Sakhi's Response:", [1, 2, 3, 4, 5])
    feedback = st.text_area("Additional Feedback:")
    if st.button("Submit Feedback"):
        save_feedback(user_input, response, rating, feedback)
        st.success("Thank you for your feedback!")

# Display Task Schedule
st.header("Task Schedule")
tasks = load_tasks("tasks_data.json")
st.write(tasks)
