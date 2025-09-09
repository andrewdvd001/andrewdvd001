'''Task 4: Practice Functions
Objective: Create a Python program that uses functions to manage a simple grade calculator.

Instructions:

1. Define a function calculate_average(grades) that takes a list of grades (numbers) and returns the average (sum of grades divided by count).
2. Define a function get_grade_status(average) that takes an average and returns:
    "Excellent" if average ≥ 90.
    "Good" if 70 ≤ average < 90.
    "Needs Improvement" if average < 70.
3. Create a list of grades (e.g., [85, 90, 95, 60]).
4. Use the functions to:
    Calculate the average of the grades.
    Determine the grade status based on the average.
    Print both the average and status.
5. Bonus (Optional): Define a function add_grade(grades, new_grade) that adds a new grade to the list and returns the updated list. Use it to add a new grade, then recalculate and print the new average and status.
'''

# Task 4
# Function
def calculate_average(grades):
    if not grades:
        return 0.0
    return sum(grades)/len(grades)

def get_grade_status(average):
    if average >= 90:
        return "Excellent"
    elif 70<= average <90:
        return "Good"
    else:
        return "Needs Improvement"

def add_grade(grades, new_grade):
    new_grades = grades.copy()
    new_grades.append(new_grade)
    return new_grades

# Print Grades
grades = [85, 90, 95, 60]
print(f"Grades: {grades}")
print(f"Average: {calculate_average(grades)}")
print(f"Status: {get_grade_status(calculate_average(grades))}")

# Print Updated Grades
updated_grades = add_grade(grades, 88)
new_average = calculate_average(updated_grades)
print(f"Bonus - New grade added: {updated_grades}")
print(f"New Average: {new_average}")
print(f"New Status: {get_grade_status(new_average)}")