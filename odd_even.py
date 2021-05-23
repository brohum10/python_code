num = input("Enter any number.")
num = int(num)
print(type(num))
print( num%2)
if num == 0:
     print("This is zero. It is even.")
     exit()
if num%2 == 0:
    print("This is even")
else:
    print("This is odd")
