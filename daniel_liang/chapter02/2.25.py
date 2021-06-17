import turtle
t = turtle.Turtle()

x1, y1 = eval(input("Enter x and y coordinate for the center of the rectangle: "))
legnth = eval(input("Enter the legnth of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))

t.penup()

t.goto(x1, y1)
t.fd(width/2)
t.lt(90)
t.fd(legnth/2)

t.pendown()

for i in range(2):
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(legnth)

t.hideturtle()
