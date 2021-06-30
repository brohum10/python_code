import math

def mag_comp():
    x1, y1 = eval(input("Enter first x and y coordinates to calculate vector distace : "))
    x2, y2 = eval(input("Enter second x and y coordinates to calculate vector distace : "))

    x_disc = x2 - x1

    y_disc = y2 - y1

    d = math.sqrt(((x_disc)**2) + ((y_disc)**2))
    print(d, " is the magnitude, and", x_disc, ",", y_disc, "are the components.")

def speed_velocity():
    x1, y1 = eval(input("Enter first x and y coordinates to calculate velocity/speed : "))
    v = math.sqrt(((x1)**2) + ((y1)**2))
    print("The speed is", v)

def new_vector():
    x1, y1 = eval(input("Enter first x and y coordinates to add vector : "))
    x2, y2 = eval(input("Enter second x and y coordinates to add vector : "))
    x = x1 + x2
    y = y1 + y2
    print("The new vector is", x, ",", y)
    
def dot_product():
    x1, y1 = eval(input("Enter first x and y coordinates to add vector : "))
    x2, y2 = eval(input("Enter second x and y coordinates to add vector : "))
    x = x1 * x2
    y = y1 * y2
    z = x + y
    print("The dot product is", z)

def angle_between():
    x1, y1 = eval(input("Enter first x and y coordinates to add vector : "))
    x2, y2 = eval(input("Enter second x and y coordinates to add vector : "))
    
    x = x1 * x2
    y = y1 * y2
    z = x + y
    print(z, "is the dot product")
    d1 = math.sqrt(((x1)**2) + ((y1)**2))
    d2 = math.sqrt(((x2)**2) + ((y2)**2))
    print(d1)
    print(d2)
    a = (z / (d1*d2))

    b = math.acos(a)
    c = math.radians(math.acos(b))
    print(c)

    
def main():
    choice = int(input("Choose 1 for magnitude/component, 2 for velocity/degrees, 3 for adding vectors, 4 for dot product, 5 for degrees in between: "))

    if choice == 1:
        mag_comp()

    if choice == 2:
        speed_velocity()

    if choice == 3:
        new_vector()
        
    if choice == 4:
        dot_product()

    if choice == 5:
        angle_between()
main()
