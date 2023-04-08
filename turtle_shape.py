import turtle
import random
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)

for i in range(200):
    t.pencolor(random.random(),random.random(),random.random())
    t.forward(i*4)
    t.right(91)

turtle.done()

