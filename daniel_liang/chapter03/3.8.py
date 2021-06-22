amount = eval(input("Enter an amount, for example, 11.56: "))


# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount // 1
remainingAmount = remainingAmount % 1


# Display the results
print("Your amount", amount, "consists of\n",
"\t", numberOfOneDollars, "dollars\n",
"\t", numberOfPennies, "pennies")
