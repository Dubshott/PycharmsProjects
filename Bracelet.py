import turtle

turtle.speed(0)


def make_bead():
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.backward(100)
    turtle.left(10)


for i in range(36):
    make_bead()

turtle.done