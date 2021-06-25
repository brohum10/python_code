x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))

# Prompt the user to enter circle2 's center x-, y-coordinates, and radius
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

# Calculate the distance between tow centers
distance = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# Circle2(the smallest circle) is inside circle1
if distance <= abs(r1 - r2):
    print("circle2 is inside circle1")

# Circle2 overlaps circle1
elif distance <= abs(r1 + r2):
    print("circle2 overlaps circle1")

# otherwise circle2 does not overlap circle1
else:
    print("circle2 does not overlap circle1")
