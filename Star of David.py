from time import sleep
import turtle

pen = turtle.Turtle()

size = 300

# Centering
pen.up()
pen.backward(size/2)
pen.right(90)
pen.forward(size/6*(3**0.5))
pen.left(90)
pen.down()

# Drawing
for i in range(7):
    if i == 3:
        pen.up()
        pen.goto(pen.pos()[0], pen.pos()[1]+size/3*(3**0.5))
        pen.down()
    elif i > 3:
        pen.forward(size)
        pen.right(120)
    else:
        pen.forward(size)
        pen.left(120)
