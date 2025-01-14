import os
from datetime import datetime, timedelta
from transformers import pipeline

def generate_blog(topic):
    """
    Generate a blog using GPT-2.
    """
    generator = pipeline("text-generation", model="gpt2")
    content = generator(f"Write a blog about {topic}", max_length=200, num_return_sequences=1)[0]["generated_text"]
    file_name = f"{topic.replace(' ', '_').lower()}_blog.md"
    with open(file_name, "w") as file:
        file.write(content)
    return file_name

def organize_outputs(outputs):
    """
    Organize generated outputs in a folder.
    """
    folder_name = f"Sakhi_Outputs_{datetime.now().strftime('%Y%m%d')}"
    os.makedirs(folder_name, exist_ok=True)
    for file in outputs:
        os.rename(file, os.path.join(folder_name, file))
    return folder_name

# Example Workflow
if __name__ == "__main__":
    topic = "AI in Healthcare"
    blog = generate_blog(topic)
    outputs = [blog]
    organized_folder = organize_outputs(outputs)
    print(f"Workflow completed. Outputs organized in: {organized_folder}")
