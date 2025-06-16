'''Task 5: Practice File Handling
Objective: Create a Python program that manages a to-do list by saving it to a file and reading from it.

Instructions:

1. Create a list of tasks (e.g., ["Buy groceries", "Study Python", "Call friend"]).
2. Define a function save_tasks(filename, tasks) that saves each task to a file (one task per line).
3. Define a function read_tasks(filename) that reads the tasks from the file and returns them as a list.
4. Write a program that:
    Saves the task list to a file (e.g., todo.txt).
    Reads the tasks from the file and prints them.
    Appends a new task (e.g., "Exercise") to the file.
    Reads and prints the updated task list.
5. Bonus (Optional): Add error handling to read_tasks to handle FileNotFoundError and return an empty list if the file doesn’t exist.
'''
# Function
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"- {task}\n")
        return f"Saving tasks to {filename}..."

def read_tasks(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().lstrip("- ") for line in file.readlines()]
    except FileNotFoundError:
        return []

def update_task(filename, new_task):
    with open(filename, "a") as file:
        file.write(f"- {new_task}\n")
    return "Appending new task..."

# Variable
tasks = ["Buy groceries", "Study Python", "Call friend"]
filename = "todo.txt"
new_tasks = "Exercise"

# Print
print(save_tasks(filename, tasks))
print("Tasks read from file:")
for task in read_tasks(filename):
    print(f"- {task}")
print(f"{update_task(filename, new_tasks)}")
print("Updated Tasks:")
for task in read_tasks(filename):
    print(f"- {task}")
