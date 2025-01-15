import json

# Save Feedback
def save_feedback(user_input, response, rating, feedback, file_name="feedback_data.json"):
    data = {
        "user_input": user_input,
        "response": response,
        "rating": rating,
        "feedback": feedback,
    }
    try:
        with open(file_name, "r") as file:
            feedback_data = json.load(file)
    except FileNotFoundError:
        feedback_data = []
    feedback_data.append(data)
    with open(file_name, "w") as file:
        json.dump(feedback_data, file, indent=4)

# Load Tasks
def load_tasks(file_name):
    try:
        with open(file_name, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {"No tasks found": "Add tasks to manage them here"}
    return tasks
