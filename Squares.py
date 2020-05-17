import turtle

def initial():
    turtle.penup()
    turtle.setposition(-150,0)

length = 10


initial()
for i in range(5):
    for i in range(4):
        turtle.pendown()
        turtle.forward(length)
        turtle.left(90)
    turtle.penup()
    turtle.forward(length * 2)
    length = length + 10

turtle.done