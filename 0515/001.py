import turtle
import random

#환경 변수
turtlesN = 3 # 거북이의 마리수를 설정합니다.


turtles = list()
colors = ("red", "orange", "yellow", "green", "blue", "purple")

def initTurtle(shape,x,y):
    t = turtle.Turtle()
    t.shape(shape)
    t.pensize(5)
    t.penup()
    t.goto(x,y)
    return t

screen = turtle.Screen()

for i in range(turtlesN):
    t = initTurtle("turtle",-300,i*70-turtlesN/2*70)
    t.pendown()
    t.speed(1)
    t.color(random.choice(colors))
    turtles.append(t)

for i in range(100):
    for t in turtles:
        d = random.randint(1,6)
        t.forward(d)