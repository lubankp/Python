import turtle

t = turtle.Turtle()
t.penup()
t.speed(0)

def squere(r, g, b):
    t.color(r, g, b)
    t.begin_fill()
    for _ in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()


for x in range(10):

    squere(x/10,0,0)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    squere(0,x / 10, 0)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    squere(0, 0, x / 10)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)