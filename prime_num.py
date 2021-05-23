num = input("Enter any number.")
num = int(num)
print(type(num))


if num == 0:
    print("Zero is an even number, not prime.")
    exit()
if num == 1:
    print("This is not prime.(Odd)")
    exit()
if num == 2:
    print("This is A prime number.")
    exit()
if num == 3:
    print("This is A prime number.")
    exit()
if num < 0:
    print("Enter a positive number please.")
    exit()    

i = 2      
while i <= num/2:
    if num%i == 0:
        print("This is not prime.")
        exit()
    i = i + 1
print(num, "is a prime numner.")
     
