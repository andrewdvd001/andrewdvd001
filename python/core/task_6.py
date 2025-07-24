'''Task 6: Practice Modules and Libraries
Objective: Create a Python program that uses random and datetime modules to generate a random task schedule.

Instructions:

1. Create a list of tasks (e.g.,  ).
2. Use the random module to:
    Select a random task with random.choice().
    Shuffle the task list with random.shuffle().
3. Use the datetime module to get the current date, formatted as YYYY-MM-DD.
4. Define a function generate_schedule(tasks) that returns a dictionary with:
    "date": Current date (string).
    "random_task": A randomly selected task.
    "shuffled_tasks": The shuffled task list
5. Print the schedule dictionary in a formatted way.
6. Bonus (Optional): Save the schedule to a file (schedule.txt) with the format:
    Schedule for 2025-06-15:
    Random Task: Study
    Shuffled Tasks: Read, Exercise, Study

Example Output:
Schedule:
Date: 2025-06-15
Random Task: Exercise
Shuffled Tasks: ['Read', 'Study', 'Exercise']
Bonus: Schedule saved to schedule.txt

'''
#Task 
import random
import datetime

def generate_schedule(tasks):
    schedule = {}
    schedule["date"] = datetime.datetime.now().strftime('%Y-%m-%d')
    schedule["random_task"] = random.choice(tasks)
    task_list = tasks.copy()
    random.shuffle(task_list)
    schedule["shuffled_tasks"] = task_list
    return schedule

def save_schedule(filename, schedule):
    try:
        with open(filename, "w") as file:
            file.write(f"Schedule for {schedule['date']}:\n")
            file.write(f"Random Task: {schedule['random_task']}\n")
            file.write(f"Shuffled Tasks: {', '.join(schedule['shuffled_tasks'])}")
            return f"Bonus: Schedule saved to {filename}"
    except IOError:
        return "Error: Could not save to file"    

tasks = ["Study", "Exercise", "Read"]
filename = "schedule.txt"
schedule = generate_schedule(tasks)

print("Schedule:")
print(f"Date: {schedule['date']}")
print(f"Random Task: {schedule['random_task']}")
print(f"Shuffled Tasks: {schedule['shuffled_tasks']}")
print(save_schedule(filename, schedule))


