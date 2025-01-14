from datetime import datetime

def generate_task():
    """
    Generate a sample task for automation.
    """
    task = f"Automated task generated on {datetime.now()}"
    with open("task_log.txt", "a") as file:
        file.write(task + "\n")
    print(task)

# Example execution
if __name__ == "__main__":
    generate_task()
