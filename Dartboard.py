import turtle

turtle.speed = 5

def move_down():
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()


def radius(i):
    return ((i * 25) + 25)


for i in range(0, 4, 1):
    turtle.circle(radius(i))
    move_down()

turtle.done