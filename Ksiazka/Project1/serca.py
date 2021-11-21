import turtle
import math
import random

t = turtle.Turtle()


def serce(radius, number):
    t.penup()
    t.fd(radius)
    t.rt(180)
    t.pendown()
    b = 360/number
    a = (180-b)/2
    c = radius*(math.sin(math.radians(b)))/(math.sin(math.radians(a)))
    t.rt(90+90-a)

    for _ in range(60):
        t.fd(c)
        t.rt(180-2*a)
    t.rt(180)
    for _ in range(60):
        t.fd(c)
        t.rt(180-2*a)

    d = radius * 3
    t.fd(d)
    t.rt(105)
    t.fd(d)


t.hideturtle()
t.speed(0)

for _ in range(15):
    t.pensize(random.randint(1,20))
    r = random.randint(0,10)/10
    g = random.randint(0, 10) / 10
    b = random.randint(0, 10) / 10
    t.color(r,g,b)
    x = 100 * random.randint(-5,5)
    y = 100 * random.randint(-5,5)
    t.penup()
    t.goto(x,y)
    t.pendown()
    serce(50, 100)

t.showturtle()