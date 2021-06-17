import turtle
import math
t = turtle.Turtle()

x1, y1 = eval(input("Enter x and y coordinate for the center of the circle: "))
radius = eval(input("Enter the legnth of the rectangle: "))


area = (radius**2)*(math.pi)

t.penup()
t.goto(x1, y1)
t.write(area)
t.fd(radius)
t.lt(90)
t.pendown()

t.circle(radius)
t.hideturtle()
