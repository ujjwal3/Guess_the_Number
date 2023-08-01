import random

print("Welcome to Guess the Number!")

print("Enter the range for the random number:")

min = int(input("Minimum: "))
max = int(input("Maximum: "))


bot_guess = random.randint(min, max)
while True:
    guessed_number = int(input("Guess the number: "))
    if guessed_number < bot_guess:
        print("Too low!")
    elif guessed_number > bot_guess:
        print("Too high!")
    elif guessed_number == bot_guess:
        print(f"Congratulations! You guessed the correct number {bot_guess}!")
        break