todo_list = ["Buy groceries", "Study Python", "Call friend"]
task_detail = {"priority_task": "Study Python"}

print("Tasks:")
for todo in todo_list:
    print(todo)

todo_list.append("Exercise")
todo_list.remove("Study Python")

print(f"Updated list: {todo_list}")

print("Tasks details:")

task_detail["due_date"] = "2025-06-15"

for key, value in task_detail.items():
    print(f"{key}: {value}")

if "Study Python" not in todo_list:
    print("Bonus: Study Python is not in the list!")
else:
    print("Bonus: Study Python is in the list!")