import turtle
import math

def snowFlakeSide(turtle, length, level):
    """Draw a side of the snowflake curve with side length length and recursion
    depth of level"""
    if (level != 1):
        snowFlakeSide(turtle, length/3, level-1)
        turtle.lt(60)
        snowFlakeSide(turtle, length/3, level-1)
        turtle.rt(120)
        snowFlakeSide(turtle, length/3, level-1)
        turtle.lt(60)
        snowFlakeSide(turtle, length/3, level-1)
    else:
        turtle.fd(length)
        turtle.lt(60)
        turtle.fd(length)
        turtle.rt(120)
        turtle.fd(length)
        turtle.lt(60)
        turtle.fd(length)
        return

def snowFlake(turtle, length, level):
    snowFlakeSide(turtle, length, level)
    turtle.rt(120)
    snowFlakeSide(turtle, length, level)
    turtle.rt(120)
    snowFlakeSide(turtle, length, level)
    turtle.hideturtle()

def moveTurtle(turtle, x, y):
    turtle.pu()
    turtle.setposition(x,y)
    turtle.pd()

if __name__ == "__main__":
    franklin = turtle.Turtle()
    franklin.speed(0)
    moveTurtle(franklin, -180, 130)
    snowFlake(franklin, 120, 5)
    turtle.mainloop()
