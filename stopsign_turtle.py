import turtle

t=turtle.Turtle()
t.speed(0)
t.color("red")
t.begin_fill()
for i in range (8):
    t.forward(100)
    t.left(45)

t.end_fill()

  
t.left(135)
t.up()
t.forward(90)
t.down()
t.color("white")
t.width(10)
t.write("STOP", font=("Highway Gothic", 90, "bold"))

t.hideturtle()
