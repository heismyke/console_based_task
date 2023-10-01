import uuid
import json

# Load existing tasks or initialize an empty list
server_path = "https://tasksjson.vercel.app/tasks.json"
try:
    with open(server_path, "r") as json_file:
        tasks = json.load(json_file)
except FileNotFoundError:
    tasks = []

while True:
    input_value = input("Enter a task (or 'quit' to exit): ")

    if input_value.strip() == "quit":
        input_yes = input("Are you sure you want to quit? (yes/no): ")
        if input_yes.lower() == "yes":
            break
    elif input_value:
        task = {
            "id": str(uuid.uuid4()),
            "title": input_value
        }
        tasks.append(task)

# Save the updated tasks to the JSON file
with open(server_path, "w") as json_file:
    json.dump(tasks, json_file)

# Print the tasks
def load_tasks(server_path):
    with open(server_path, "r") as json_file:
        data = json.load(json_file)
        for task in data:
            print(f'The id is {task["id"]} and task is {task["title"]}')
        return data

loaded_tasks = load_tasks(server_path)
