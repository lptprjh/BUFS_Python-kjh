import turtle
import random

def initTurtle(shape,x,y):
    t = turtle.Turtle()
    t.shape(shape)
    t.pensize(5)
    t.penup()
    t.goto(x,y)
    return t

screen = turtle.Screen()
# image1 = ""
# image2 = ""
# image3 = ""
# screen.addshape(image1)
# screen.addshape(image2)
# screen.addshape(image3)

t1 = initTurtle("turtle",-300,+100)
t2 = initTurtle("turtle",-300,0)
t3 = initTurtle("turtle",-300,-100)

t1.pendown()
t2.pendown()
t3.pendown()
t1.speed(1)
t2.speed(1)
t3.speed(1)

for i in range(100):
    d1 = random.randint(1,6)
    t1.forward(d1)

    d2 = random.randint(1,6)
    t2.forward(d2)
    
    d3 = random.randint(1,6)
    t3.forward(d3)