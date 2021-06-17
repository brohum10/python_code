import math
radius, legnth = eval(input("Enter the radius and length of a cylinder:\n"))

area = (radius**2)*(math.pi)
volume = area*legnth

print("The area is %5.3f" % area)
print("The volume is %5.3f" % volume)
