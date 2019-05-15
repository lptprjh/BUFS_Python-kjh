import turtle
import random

player = turtle.Turtle()
player.color('blue')
player.shape("turtle")
player.penup()
player.speed(0)
screen = player.getscreen()

enemies = list()
enemiesN = 3

for i in range(enemiesN):
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    enemy.right(random.randint(0,359))
    enemy.goto(random.randint(-300,300), random.randint(-300,300))
    enemies.append(enemy)

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

def play():
    player.forward(3)
    for enemy in enemies:
        enemy.forward(2)
    screen.ontimer(play, round(30 / enemiesN))

screen.ontimer(play, round(30 / enemiesN))

input("엔터를 누르면 종료합니다.")