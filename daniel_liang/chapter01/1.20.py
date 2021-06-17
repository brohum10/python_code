import turtle
t = turtle.Pen()
t.speed(0)
    
length = 400
width = 200
slant = 100

# Front Rectangle
t.goto(0, width)
t.goto(length, width)
t.goto(length, 0)
t.goto(0, 0)

# Back Rectangle
t.goto(slant, slant)
t.goto(length+slant, slant)
t.goto(length+slant, width+slant)
t.goto(slant, width+slant)

# Slants
t.goto(slant, slant)
t.penup()
t.goto(0, width)
t.pendown()
t.goto(slant, width+slant)
t.penup()
t.goto(length, width)
t.pendown()
t.goto(length+slant, width+slant)
t.penup()
t.goto(length, 0)
t.pendown()
t.goto(length+slant, slant)

t.hideturtle()

