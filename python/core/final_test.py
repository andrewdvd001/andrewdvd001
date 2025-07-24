# 1. <class 'float'>#
#2. 32#
#.C#
#4.#
for number in range(11):
    if number % 3 != 0:
        print(number)
#5.#
def greet():
    return "Hello World!"
#6.#
coords = (9, 4)
x, y = coords
print(f"x = {x}, y = {y}")
#7.#
person = {"name": "Alice", "age": 30}
person["city"] = "Jakarta"
#8.#
print(" PyTHon Pro ".strip().lower())
#9.#
with open("notes.txt", "w") as file:
    file.write("Learning Python!")
with open("notes.txt", "r") as file:
    print(file.read())
#10.#
def safe_int(text):
    try:
        integer = int(text)
        print(integer)
    except ValueError:
        return "Invalid input"
    