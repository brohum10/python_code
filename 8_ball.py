import random

array = ["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.",  "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

len_array = len(array)-1

eight_ball = int(input("Enter number 8 to start!"))

if eight_ball != 8:
    print("You had one job.")
if eight_ball == 8:
    word = array[random.randint(0, len_array)]
    print(word)
    
