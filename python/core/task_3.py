'''Task 3: Practice Lists, Tuples, and Dictionaries
Objective: Create a Python program to manage a simple to-do list using lists and dictionaries.

Instructions:

1. Create a list called todo_list containing at least 3 tasks (strings, e.g., ["Buy groceries", "Study Python", "Call friend"]).
2. Create a dictionary called task_details with at least one key-value pair (e.g., {"priority_task": "Study Python"}).
3. Write a program that:
    Prints all tasks in todo_list using a for loop.
    Adds a new task to todo_list using append().
    Removes a task from todo_list using remove() (choose one task).
    Updates task_details to include a new key-value pair (e.g., due_date: "2025-06-15").
    Prints the updated todo_list and all key-value pairs in task_details.
4. Bonus (Optional): Check if a specific task (e.g., "Study Python") is in todo_list using in, and print a message like "Study Python is in the list!" if found.
'''

# Task 3
# Variable
todo_list = ["Buy groceries", "Study Python", "Call friend"]
task_detail = {"priority_task": "Study Python"}

# Print Variable
print("Tasks:")
for todo in todo_list:
    print(todo)

# Update Variable
todo_list.append("Exercise")
todo_list.remove("Study Python")
print()
print(f"Updated list: {todo_list}")
print("Tasks details:")
task_detail["due_date"] = "2025-06-15"

# Print Updated Variable
for key, value in task_detail.items():
    print(f"{key}: {value}")

# Bonus
if "Study Python" not in todo_list:
    print("Bonus: Study Python is not in the list!")
else:
    print("Bonus: Study Python is in the list!")