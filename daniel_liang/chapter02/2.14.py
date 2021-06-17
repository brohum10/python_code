x1, y1, x2, y2, x3, y3 = eval(input("Enter three points of a triangle: "))

side_1 = (((x1 - x2)**2)+((y1 - y2)**2))**(1 / 2)
side_2 = (((x1 - x3)**2)+((y1 - y3)**2))**(1 / 2)
side_3 = (((x3 - x2)**2)+((y3 - y2)**2))**(1 / 2)
s = (side_1 + side_2 + side_3)/2
area = (s*((s - side_1)*(s - side_2)*(s - side_3)))**(1 / 2)

print("The area of the triangle is %.2f" %area)
