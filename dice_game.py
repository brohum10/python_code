import random
import sys

#global var
userscore = []
computerscore = []

#dice simulator
def dice_number(x):
    for i in range (x):
        user_value = random.randint(1, 6)
        computer_value = random.randint(1, 6)
        userscore.append(user_value)
        computerscore.append(computer_value)

#Mechanics
def fair_judge():
    if user_value > computer_value:
        print("\nUser wins!")
    if computer_value > user_value:
        print("\nComputer wins!")
    if computer_value == user_value:
        print("\nIt is a tie!")


c = 1
while c == 1:
    #initializing
    userscore = []
    computerscore = []

    #read user input
    x = input("Enter any number of dice: \n")

    #check if it is an integer
    if x.isdigit():
        x=int(x)
        if x <= 0:
            print("You entered an incorrect number of dice. Try again")
            #to restart loop
            continue

        else:
            #for x > 0
            input("Ready to start? Hit the \"Enter\" Key to continue\n")

            dice_number(x)
            print("User's turn to roll: ")
            print("User's roll: " , userscore)
            user_value = sum(userscore)
            print("\nUser's total: ", user_value)
            print("\nComputer's turn to roll: ")
            print("Computer's roll: ", computerscore)
            computer_value = sum(computerscore)
            print("\nComputer's total: ", computer_value)
            fair_judge()
            c = int(input("Do you want to play again? Press 1 for \"Yes\" and Enter or 2 for \"No\" and Enter:\n"))

            
    else:
        #x is other than an integer
        print("You entered an incorrect character for number of dice. Try again")
        #to restart loop
        continue


input ("Press the \"Enter\" Key to close the window")
sys.exit()
