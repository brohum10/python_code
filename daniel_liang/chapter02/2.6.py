digits = eval(input("Enter a number between 0 and 1000: "))
sum=0

while digits >0:
    sum += digits % 10
    digits = int(digits/10)

ones_place = digits % 10
y_place = digits % 1000
z_place = y_place % 100
two_place = z_place % 10



print(sum)
