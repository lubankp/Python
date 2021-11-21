import turtle
t = turtle.Turtle()

# drow a square
def square(x):
    for _ in range(4):
        t.fd(x)
        t.rt(90)

# drow a star
for _ in range(10):
    square(100)
    t.rt(360/10)

t.home()
t.clear()

def star(l, a):
    for _ in range(a):
        t.fd(l)
        t.bk(l)
        t.rt(360/a)

star(300,60)