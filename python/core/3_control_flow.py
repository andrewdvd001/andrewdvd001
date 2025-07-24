## Grade Checker ##
score = int(input("Input : "))

if score >= 90:
    print("A")
elif 75 <= score <90:
    print("B")
elif 60 <= score <75:
    print("C")
elif 40 <= score <60:
    print("D")
else:
    print("F")

## Number Type ##
n = int(input("Input : "))

if n < 0:
    print("Negative")
elif n > 0:
    print("Positive")
else:
    print("Zero")

## Odd or Even ##

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("odd")
else:
    print("even")