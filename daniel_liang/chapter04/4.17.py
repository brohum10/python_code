import random
ROCK = 0
PAPER = 1
SCISSORS = 2
user_score = 0
computer_score = 0
while True:


    computer = random.randint(0,2)

    user = int(input("Choose wisely. \nEnter 0 for ROCK, 1 for PAPER, or 2 for SCISSORS.\n"))


    if computer == ROCK:
        print("The computer throws ROCK")
    if computer == PAPER:
        print("The computer throws PAPER")
    if computer == SCISSORS:
        print("The computer throws SCISSORS")

    if user == ROCK:
        if computer == ROCK:
            print("\nIt's a tie, we both have ROCK!")
            user_score=user_score + 1
            computer_score=computer_score + 1
        if computer == PAPER:
            print("\nYou lose, PAPER covers ROCK!")
            computer_score=computer_score + 1
        if computer == SCISSORS:
            print("You win, ROCK breaks SCISSORS!")
            user_score=user_score + 1

    if user == PAPER:
        if computer == PAPER:
            print("\nIt's a tie, we both have PAPER!")
            computer_score=computer_score + 1
            user_score=user_score + 1
        if computer == SCISSORS:
            print("\nYou lose, SCISSORS cuts PAPER!")
            computer_score=computer_score + 1
        if computer == ROCK:
            print("You win, PAPER covers ROCK!")
            user_score=user_score + 1

    if user == SCISSORS:
        if computer == SCISSORS:
            print("\nIt's a tie, we both have SCISSORS!")
            computer_score=computer_score + 1
            user_score=user_score + 1
        if computer == PAPER:
            print("\nYou win, SCISSORS cuts PAPER!")
            user_score=user_score + 1
        if computer == ROCK:
            print("You lose, ROCK breaks SCISSORS!")
            computer_score=computer_score + 1
            
    print("Your total score is: ", user_score )
    print("Computer's total score is: ", computer_score ,"\n" )
    play_again = input("Do you want to try again? Press 5 for 'Yes' or Any Number Key for 'No'\n")
    if play_again.lower() != "5":
        print("\nGood Bye")
        break
