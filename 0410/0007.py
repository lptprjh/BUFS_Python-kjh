import turtle
t = turtle.Turtle()
t.speed(0)

n = 100

for count in range(n):
    t.circle(100)
    t.left(360/n)

