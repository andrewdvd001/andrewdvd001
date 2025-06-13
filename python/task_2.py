secret_number = 5
guess_count = 0
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
    