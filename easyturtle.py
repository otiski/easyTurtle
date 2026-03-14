import turtle

t = turtle.Pen()

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
def done():
    turtle.done()