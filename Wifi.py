import turtle

def rectangle(i):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward((i * 10) + 10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward((i * 10) + 10)
    turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


for i in range(0, 5, 1):
    turtle.pendown()
    rectangle(i)
    turtle.penup()
    turtle.forward(25)

turtle.end