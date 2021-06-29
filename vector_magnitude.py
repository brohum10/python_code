import math

x1, y1 = eval(input("Enter first x and y coordinates to calculate vector distace : "))
x2, y2 = eval(input("Enter second x and y coordinates to calculate vector distace : "))

d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
print(d)
