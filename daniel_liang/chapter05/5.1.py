total = 0  # The total of integers
count = 0  # Count the number of integers
positveNumbers = 0  # The number of positive integers
negativeNumbers = 0  # The number of negative integers

# Prompt the user to enter an integer
number = int(input("Enter an integer, the input ends if it is 0: "))

while number != 0:
    total += number  # Calculate the total
    count += 1  # Increase count
    if number > 0:
        positveNumbers += 1  # Increase positives number
    else:
        negativeNumbers += 1  # Increase negatives number

    # Prompt the user to enter an integer
    number = eval(input("Enter an integer, the input ends if it is 0: "))

if (count == 0):  # If the user entered 0 only
    print("You didn't enter any number")

else:  # Otherwise display the results
    print("The number of positives is", positveNumbers)
    print("The number of negatives is", negativeNumbers)
    print("The total is", total)
    print("The average is", total / count)
