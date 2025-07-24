'''
Task 7: Practice Exception Handling and Debugging
Objective: Create a Python program that processes user input for a simple calculator, handling errors and debugging issues.

Instructions:

1. Define a function calculate(operation, a, b) that performs:
    Addition ("add": a + b).
    Subtraction ("subtract": a - b).
    Division ("divide": a / b).
    Return the result or None if an error occurs.
2. Use try-except to handle:
    ZeroDivisionError for division by zero.
    TypeError for invalid types (e.g., strings).
    Invalid operation (raise a ValueError).
3. Prompt the user for:
    Operation (add, subtract, divide).
    Two numbers (convert from strings to floats).
4. Use logging.debug to log the inputs and result, and logging.error for errors.
5. Print the result or an error message.
6. Bonus (Optional): Save the calculation history to a file (calc_history.txt) in the format:
2025-06-15 11:04: add(10.0, 5.0) = 15.0
2025-06-15 11:05: divide(10.0, 0.0) = Error: Division by zero

Enter operation (add, subtract, divide): add
Enter first number: 10
Enter second number: 5
Result: 15.0
DEBUG:root:Operation: add, a=10.0, b=5.0, result=15.0
Bonus: Saved to calc_history.txt

Enter operation (add, subtract, divide): divide
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
ERROR:root:ZeroDivisionError: division by zero
Bonus: Saved to calc_history.txt
'''
import logging
def calculate(operation, a, b):
    result = None
    error_message = None
    try:
        if operation == "add":
            result = a + b
        elif operation == "substract":
            result = a - b
        elif operation == "divide":
            result = a / b
            if b == 0:
                raise ZeroDivisionError("Error: Division by Zero")
        else:
            raise ValueError("Error: Invalid operation")

    except ZeroDivisionError as error:
        error_message = f"{error}"
    except ValueError as error:
        error_message = f"{error}"
    except TypeError as error:
        error_message = f"{error}"
    return result, error_message

while True:
    operation = input(f"Enter operation (add, substract, divide): ")
    if operation == "quit":
        break
    try:
        a = float(input(f"Enter first number: "))
        b = float(input(f"Enter second number: "))
    except ValueError:
        print("Please enter numeric values.")
        continue
    calculate_result, error = calculate(operation, a, b)

    if error:
        print(f"Result:{error}")
    else:
        print(f"Calulation Result: {calculate_result}")