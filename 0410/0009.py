import turtle
t = turtle.Turtle()
t.speed(0)

n = int(turtle.textinput("","몇 개의 원을 그릴까요?"))

for count in range(n):
    t.circle(100)
    t.left(360/n)

