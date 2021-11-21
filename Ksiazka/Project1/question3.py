import turtle
import math

t = turtle.Turtle()

def circle(radius, number):
    t.fd(radius)
    b = 360/number
    a = (180-b)/2
    c = radius*(math.sin(math.radians(b)))/(math.sin(math.radians(a)))
    t.rt(90+90-a)

    for _ in range(number):
        t.fd(c)
        t.rt(180-2*a)

circle(100, 100)