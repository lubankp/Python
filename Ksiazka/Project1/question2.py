import turtle
t = turtle.Turtle()

def polygon(sides, lenght):
    for _ in range(sides):
        t.fd(lenght)
        t.rt(360/sides)

#polygon(5, 100)

def pattern(number):
    for _ in range(number):
        polygon(5,100)
        t.rt(360/number)

pattern(20)