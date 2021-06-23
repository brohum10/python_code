import random

HEADS = 0
TAILS = 1


computer = random.randint(0,1)

user = int(input("Choose wisely. \nEnter 0 for HEADS,or 1 for TAILS: "))


if computer == HEADS:
    print("The computer flipped HEADS")
if computer == TAILS:
    print("The computer flipped TAILS")


if user == HEADS:
    if computer == HEADS:
        print("\nCorrect!")
    if computer == TAILS:
        print("\nWrong!")

 
if user == TAILS:
    if computer == HEADS:
        print("\nWrong!")
    if computer == TAILS:
        print("\nCorrect!")
