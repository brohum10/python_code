x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter the points x1, y1, x2, y2, x3, y3, x4, y4: ")) 

a, b, e = (y1 - y2), (x1 - x2), ((y1 - y2) * x1) - ((x1 - x2) * y1)
c, d, f = (y3 - y4), (x3 - x4), ((y3 - y4) * x3) - ((x3 - x4) * y3)

form = ((a * -d) - (-b * c))

if form == 0:
    print("The two line are parallel")
    exit()
else:
    x = ((e * -d) - (-b * f)) / form
    y = ((a * f) - (e * c)) / form

    print("The point of intersection is at (" + str(format(x, "0.5f")) + ", " + str(format(y, "0.5f")) + ")")
 

