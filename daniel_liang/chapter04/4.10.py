import random

#Generate two random single-digit integers
number1 = random.randint(0, 100) 
number2 = random.randint(0, 100)
 
answer = eval(input("What is "+ str(number1) + " * " + str(number2) + "? "))

#Check the answer and display the result
if number1 * number2 == answer: 
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '-', number2, "is", number1 - number2, '.')
