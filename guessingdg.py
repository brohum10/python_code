import random

input("Ready to start? Hit the 'Enter' Key to continue\n") 

user_score = 0
computer_score = 0



#Random numbers between 1 and 10
user_value = random.randint(1, 6)
computer_value = random.randint(1, 6)


print("User's turn to roll: ")
print("User first roll: [", user_value, "]\n")
print("Computer's turn to roll: ")
print("Computer first roll: [", computer_value, "]")

print("\nComputer total: ", computer_value)
print("User total: ", user_value)


#Mechanics
if user_value > computer_value:
    print("\nUser wins!")
    user_score = user_score + 1 
elif computer_value > user_value:
    print("\nComputer wins!")
    computer_score = user_score + 1
else:
    print("\nIt is a tie!")

    

exit()
