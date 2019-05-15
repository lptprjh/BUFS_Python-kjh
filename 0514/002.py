import turtle
import random

def initTurtle(shape,color,x,y):
    t = turtle.Turtle()
    t.color(color)
    t.shape(shape)
    t.pensize(5)
    t.shapesize(5)
    t.penup()
    t.goto(x,y)
    return t

screen = turtle.Screen()

t1 = initTurtle("turtle","pink",-300,0)
t2 = initTurtle("turtle","blue",-300,-100)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(100):
    d1 = random.randint(1,6)
    t1.forward(d1)

    d2 = random.randint(1,6)
    t2.forward(d2)
