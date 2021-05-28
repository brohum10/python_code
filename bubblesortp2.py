import random

myList = [  ]


num_times = int( input("Enter any positive integer number for the size of the List: \n"))

if num_times <= 0:       
    print("You entered an incorrect number for the size of the List. Good Bye")
    exit()
if num_times > 0:
    for i in range(0, num_times):
        element = random.randint(1, 100)
        myList.append(element) 




print ("My Unsorted Random List is: \n   ", myList)

for i in range (len(myList)-1):
    for k in range (len(myList)-1):
        if myList[k] > myList[k+1]:
            cell = myList [k+1]
            myList [k+1] = myList[k]
            myList [k] = cell
        
print ("\n\n My List Sorted with the Bubble Sort is: \n      ", myList)

input ("\nPress the Enter Key to close the window")
