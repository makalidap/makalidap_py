import turtle

t = turtle.Turtle()

size = 100
side = 7

for i in range(side):
    t.forward(size)
    t.left(360/side)

