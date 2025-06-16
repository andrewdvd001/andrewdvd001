'''Task 2: Practice Control Flow
Objective: Write a Python program that uses conditionals and loops to create a simple number guessing game.

Instructions:

1. Create a variable secret_number with a value between 1 and 10 (e.g., 7).
2. Ask the user for input using input("Guess the number (1-10): ") and store it in a variable guess. Convert guess to an integer using int().
3. Use an if-elif-else structure to check:
    If guess equals secret_number, print "Congratulations, you guessed it!".
    If guess is too high, print "Too high! Try again.".
    If guess is too low, print "Too low! Try again.".
4. Use a while loop to allow the user to keep guessing until they get the correct number.
5. Add a guess_count variable to track how many guesses it takes.
6. When the user guesses correctly, print "It took you X guesses!" (replace X with guess_count).
7. Bonus (Optional): Add a condition to check if the input is not between 1 and 10, and print "Please enter a number between 1 and 10." if invalid.
'''

# Task 2
#Variable
secret_number = 5
guess_count = 0

# Flow
while True:
    try:
        guess = int(input("Guess the number (1-10): "))
    except ValueError:
        print("Please enter a valid number")
        continue
    guess_count += 1
    if guess == secret_number:
        print("Congratulations, you guessed it!")
        print(f"It took you {guess_count} guess{"es" if guess_count != 1 else ""}!")
        break
    elif guess > secret_number and 0 < guess <= 10:
        print("Too high! Try again.")
    elif guess < secret_number and 0 < guess <= 10:
        print("Too low! Try again.")
    else:
        print("Please enter a number between 1 and 10.")
    