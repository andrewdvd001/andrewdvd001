## Greeting Function ##
def greet_user(name):
    return f"Hello, {name}! Welcome to Python"


## Odd or Even ##
def is_even(n):
    return n % 2 == 0


## Calculator ##
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"