import turtle
t=turtle.Turtle()

t.color("yellow")

#yellowface/fillcircle
t.begin_fill()
t.circle(100)
t.end_fill()

#smile
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(60)
t.lt(90)
t.pensize(10)
t.color("red")
t.circle(60,180)

#nose
t.penup()
t.lt(90)
t.fd(50)
t.pendown()
t.color("black")
t.fd(30)
t.rt(120)
t.fd(30)

#lefteye
t.penup()
t.lt(30)
t.fd(20)
t.lt(90)
t.fd(30)
t.rt(90)
t.pendown()
t.color("blue")
t.circle(10)

#righteye
t.penup()
t.rt(90)
t.fd(84)
t.lt(90)
t.pendown()
t.circle(10)

t.hideturtle()
