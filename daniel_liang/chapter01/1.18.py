import turtle
t=turtle.Turtle()
t.speed(0)
t.width(5)
t.color("red")

t.lt(72)
t.fd(300)
for i in range (4):
    t.rt(144)
    t.fd(300)
    
turtle.bgcolor("green")
t.hideturtle()
