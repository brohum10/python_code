import turtle
t = turtle.Turtle()
radius = eval(input("Enter the circles radius: "))
t.speed(0)

t.lt(180)

t.circle(radius)

t.rt(180)

t.circle(radius)

t.up()
t.fd(radius*2)
t.down()

t.circle(radius)

t.rt(180)

t.circle(radius)

t.hideturtle()
