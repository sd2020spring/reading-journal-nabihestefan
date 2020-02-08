import turtle
import math

# Create the world, and a turtle to put in it
bob = turtle.Turtle()


#Makes a square with length length
def square(t, length):
    """
    Draw a square using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don)
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

#Makes a polygon with length length and n sides
def polygon(t, n, length):
    """
    Draw a square using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don)
    """
    angle = 360 / n
    for i in range(int(n)):
        t.fd(length)
        t.lt(angle)


#Makes a circle gives radius
def circle(t, r):
    circ = 2 * math.pi * r
    n = int(circ/3) + 3
    length = circ / n
    print(n, length)
    polygon(t, n, length)


def pie(t, n, r):
    angle = 360 / n
    for i in range(n):
        triangle(t, r, angle/2)
        t.lt(angle)

def triangle(t, r, angle):
    x = r * math.sin(angle * math.pi / 180) * 2

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(x)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)


bob.pu()
bob.bk(400)
bob.pd()
square(bob, 50)

bob.pu()
bob.fd(150)
bob.pd()
polygon(bob, 6, 100)

bob.pu()
bob.fd(250)
bob.pd()
circle(bob, 70)

bob.pu()
bob.fd(150)
bob.lt(90)
bob.fd(50)
bob.rt(90)
bob.pd()
pie(bob, 5, 50)

bob.pu()
bob.fd(200)
bob.lt(90)
bob.fd(50)
bob.rt(90)
bob.pd()
pie(bob, 10, 100)


bob.hideturtle()

turtle.mainloop()
