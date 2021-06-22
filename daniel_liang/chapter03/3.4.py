import math

side_len = float(input("Enter the side legnth to calculate the area of the pentagon: "))

#for pi/5 so tan can calculate
a = math.pi / 5

area =((5*(side_len**2))/(4*(math.tan(a)) ))

print("The area of the pentagon is ", area)
