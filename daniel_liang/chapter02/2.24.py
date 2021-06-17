import turtle
t = turtle.Turtle()

t.lt(30)
for i in range(6):
    t.fd(100)
    t.lt(60)

t.rt(180)

for i in range(6):
    t.fd(100)
    t.lt(60)
    
t.lt(150)
t.up()
t.fd(200)
t.down()
t.lt(30)
for i in range(6):
    t.fd(100)
    t.lt(60)

t.rt(180)

for i in range(6):
    t.fd(100)
    t.lt(60)
t.hideturtle()
