import math

r = eval(input("Enter the legnth from the center to a vertex: "))
s = 2*(r)*(math.sin(math.pi/5))
area = (3*(math.sqrt(3))*(s**2))/2

print("The area of the pentagon is %.2f" %area)
