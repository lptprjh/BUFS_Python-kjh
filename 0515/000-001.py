import t
import random

### 이미지 설정
# 이미지가 포함된 폴더의 경로를 입력하세요
pathPrefix = "C:/Users/user/Desktop/20191767 류종헌/0515/"

###
image1 = pathPrefix + "rabbit.gif"
image2 = pathPrefix + "turtle.gif"


def initTurtle(shape,x,y):
    t = t.Turtle()
    t.shape(shape)
    t.pensize(5)
    t.penup()
    t.goto(x,y)
    return t

screen = t.Screen()

screen.addshape(image1)
screen.addshape(image2)

t1 = initTurtle(image1,-300,+100)
t2 = initTurtle(image2,-300,0)

t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(100):
    d1 = random.randint(1,6)
    t1.forward(d1)

    d2 = random.randint(1,6)
    t2.forward(d2)