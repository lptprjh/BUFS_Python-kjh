import turtle
import math

player = turtle.Turtle()
player.color('blue')
player.shape("turtle")
player.speed(0)
screen = player.getscreen()

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def fire():
    x,y,velocity = (0,0,50)
    angle = player.heading()
    vx = velocity * math.cos(angle/180.0 *3.14)
    vy = velocity * math.sin(angle/180.0 *3.14)
    while player.ycor() >= 0:
        vy -= 5
        x += vx
        y += vy
        player.goto(x,y)

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(fire, "space")
screen.listen()

input("엔터를 누르면 종료합니다.")