import turtle
import colorsys

t = turtle.Pen()

def bgcolor(col):
    turtle.bgcolor(col)

def circle(col, size):
    t.color(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def square(col, size):
    t.color(col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()
def triangle(col, size):
    t.color(col)
    t.begin_fill()
    for x in range(3):
        t.fd(size)
        t.rt(120)
    t.end_fill()


def patternCircle(num):
    h = 0.0

    t.speed(0)



    for i in range(num):
        t.hideturtle()
        c = colorsys.hsv_to_rgb(h, 1, 1)

        t.color(c)

        t.pendown()
        
        t.begin_fill()
        t.fillcolor(c)

        t.circle(i)

        t.end_fill()   

        t.penup()

        t.lt(170)
        t.fd(i*2)




        h += 0.05


def done():
    turtle.done()