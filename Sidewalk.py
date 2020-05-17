import turtle

turtle.speed(0)
turtle.penup()
turtle.setposition(-200, -200)

def make_square():
    turtle.pendown()
    for i in range(8):
        for i in range(4):
            turtle.forward(50)
            turtle.left(90)
        turtle.forward(50)


def turn():
    turtle.left(90)
    turtle.forward(50)


make_square()
turn()
make_square()
turtle.setposition(200, 200)
turtle.left(90)
make_square()
turn()
make_square()

turtle.end