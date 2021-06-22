import math
n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side: "))

area = (n*(s**2))/(4*math.tan(math.pi/n))

print("The area of the polygon is ", area)
