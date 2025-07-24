## Safe Division ##
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
 
## Input Parser ##
def ask_int():
    while True:
        try:
            number = int(input("Please input integer: "))
            return number
        except ValueError:
            print("Please enter a valid integer.")


## File Reader with Error ##
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"