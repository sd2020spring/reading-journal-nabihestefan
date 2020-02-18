import turtle


def recTree(turtle, length, level):
    if(level == 1):
        turtle.pencolor("green")
        turtle.fd(length)
    else:
        turtle.pencolor("brown")
        turtle.fd(length)
        newTurtle = clone(turtle)
        newTurtle.lt(30)
        recTree(newTurtle, length*0.6, level - 1)
        newTurtle.hideturtle()
        turtle.bk(length/3)
        otherTurtle = clone(turtle)
        otherTurtle.right(40)
        recTree(otherTurtle, length*0.64, level-1)
        otherTurtle.hideturtle()


def clone(leo):
    don = turtle.Turtle()
    don.penup()
    don.setx(leo.xcor())
    don.sety(leo.ycor())
    don.setheading(leo.heading())
    if leo.isdown():
        don.pendown()

    return don

if __name__ == "__main__":
    tChala = turtle.Turtle()
    tChala.speed(0)
    tChala.lt(90)
    tChala.pu()
    tChala.setposition(0, -200)
    tChala.pd()
    tChala.speed(0)
    recTree(tChala, 150, 10)
    tChala.hideturtle()
    turtle.mainloop()
