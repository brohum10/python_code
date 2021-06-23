import random

#Step 1:    
num1, num2, num3 = eval(input("Enter 3 integers to sort: "))
myList = [num1, num2, num3]


for i in range (len(myList)-1):
    for k in range (len(myList)-1):
        if myList[k] > myList[k+1]:
            cell = myList [k+1]
            myList [k+1] = myList[k]
            myList [k] = cell
        
print ("\nMy List After: ", myList)
