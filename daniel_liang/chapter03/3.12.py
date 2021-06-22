import turtle
t=turtle.Turtle()

len = float(input("Enter length of star sides: "))


t.lt(72)
t.fd(len)
for i in range (4):
    t.rt(144)
    t.fd(len)
    
