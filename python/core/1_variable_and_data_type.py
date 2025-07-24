name = "Andrew"
age = 29
height = 1.73
learningPython = True
nothing = None

print(type(name))
print(type(age))
print(type(height))
print(type(learningPython))
print(type(nothing))

print("Before :", name, age , height)
name, age, height = height, name, age
print("After :", name, age, height)