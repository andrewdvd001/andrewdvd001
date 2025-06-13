'''Task 1: Practice Variables, Data Types, and Operations
Objective: Write a Python program that uses variables, different data types, and basic operations to create a simple personal info card.
Instructions:

1. Create variables for:
    Your name (string`)
    Your age (integer)
    Your height in meters (float)
    Whether you’re learning Python (boolean, e.g., True)
2. Perform these operations:
    Calculate your age plus 5 years.
    Calculate your height in centimeters (height * 100).
    Create a greeting message by concatenating your name with " is learning Python!".
3. Print:
    The greeting message.
    Your age in 5 years.
    Your height in centimeters.
    Whether you’re learning Python.
4. Bonus (Optional): Try converting your age to a string and concatenate it with a message like "My age is ".
'''
#Variables
name = "Andrew David Subally"
age = 29
height = 1.73
learning_python = True

# Operations
age_in_5_years = age + 5
height_in_cm = int(height * 100)
greeting_message = name + " is learning Python!"

# Print Statements
print(greeting_message)
print(f"In 5 years, I will be {age_in_5_years} years old.")
print(f"My height in centimeters is {height_in_cm} cm.")
print("Am I learning Python?", learning_python)
# Bonus
age_str = str(age)
print(f"My age is {age_str}.")

# End of Task 1
# Task 1 completed successfully