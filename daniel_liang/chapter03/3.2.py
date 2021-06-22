import math
x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees:\n"))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees:\n"))
radius = 6371.01

rx1= math.radians(x1)
rx2= math.radians(x2)
ry1= math.radians(y1)
ry2= math.radians(y2)

crx1 =  math.cos(rx1)
srx1 =  math.sin(rx1)

crx2 =  math.cos(rx2)
srx2 =  math.sin(rx2)

cry =  math.cos(ry1-ry2)

d = radius * math.acos(srx1 * (srx2) + ((crx1) * (crx2) * (cry)))
print("The distance between the two points is ", d , " km")
