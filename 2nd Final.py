import random

#initializing variables
user_age_score = 0
user_subject_score = 0
age = (random.randint(14, 18))
subject = ["English", "Math", "History", "Science", "Art and Music", "Computers", "PE"]


#part 1
#taking age input from user and comparing against random

guess_age = int(input("My age is from 14 to 18. Guess what my age is:\n"))

if guess_age  == age:
    print("\nYour Answer Is Correct. My age is " + str(age))
    user_age_score = user_age_score +1
    print("Your score is: " + str(user_age_score))
if guess_age  != age:
    print("\nYour Answer Is Incorrect. My age is " + str(age))
    print("Your score is: " + str(user_age_score))


#part 2
#taking subject input from user and comparing against random

fav_subject = random.choice(subject)

sub  = input("\nGuess what my favorite subject is:\nPrint e for English, m for Math, h for History, s for Science, a for Art and Music, c for Computers, p for PE:\n")

if sub == "e":
    guess_subject = "English"
if sub == "m":
    guess_subject = "Math"
if sub == "h":
    guess_subject = "History"
if sub == "s":
    guess_subject = "Science"
if sub == "a":
    guess_subject = "Art and Music"
if sub == "c":
    guess_subject = "Computers"
if sub == "p":
    guess_subject = "PE"

    
if guess_subject  == fav_subject:
    print("\nYour Answer Is Correct. \nMy favorite subject is " + fav_subject)
    user_subject_score = user_subject_score +1
    print("Your score is: " + str(user_subject_score))
if guess_subject  != fav_subject:
    print("\nYour Answer Is Incorrect. \nMy favorite subject is " + fav_subject)
    print("Your score is: " + str(user_subject_score))


#part 3
#adding both part 1 and part 2 scores and closing window
    
total_score = user_subject_score + user_age_score
print("\n\nYour Total Score is: " + str(total_score))
print("Press Enter to close the window")
