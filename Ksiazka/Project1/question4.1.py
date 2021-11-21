import turtle
import math
import random

t = turtle.Turtle()

def circle(radius, number):
    t.penup()
    t.fd(radius)
    t.pendown()
    b = 360/number
    a = (180-b)/2
    c = radius*(math.sin(math.radians(b)))/(math.sin(math.radians(a)))
    t.rt(90+90-a)

    for _ in range(number):
        t.fd(c)
        t.rt(180-2*a)

t.hideturtle()
t.speed(0)

for _ in range(20):
    x = 100 * random.randint(0,5)
    y = 100 * random.randint(0,5)
    t.penup()
    t.goto(x,y)
    t.pendown()
    circle(50, 100)

t.showturtle()