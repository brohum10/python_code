import random

num = int(random.randint(1, 100))

guess = input("Guess my number between 1-100:\n")

while guess != num:
    if int(guess) < 0:
        print("Invalid number")
        break
    if int(guess) > 100:
        print("Invalid number")
        break
    if int(guess) > num:
        print("Too high")
    if int(guess) < num:
        print("Too low")
    if int(guess) == num:
        print("Correct!")
        break
    guess = input("\nGuess again:\n")
