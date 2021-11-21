import turtle
import random

t = turtle.Turtle()

def star(x, y, l, n):
    t.penup()
    t.goto(x,y)
    t.setheading(random.randint(0,359))
    t.pendown()
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360/n)

for _ in range(10):
    star(random.randint(-300,300),random.randint(-300,300),random.randint(10,150), random.randint(3,20))
