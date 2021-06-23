import math

a, b, c = eval(input("Enter a, b, c: "))
               
discriminant = (b**2) - (4 * a * c)


if discriminant == 0:
    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
    r1 = r2
    print ("The root is", r1)

elif discriminant > 0:
    r1 = (-b + math.sqrt(discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are", r1, "and", r2)

else:
    print("The equation has no real roots")
