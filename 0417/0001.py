import turtle
t = turtle.Turtle()

n = 6

deg = 360/n
while n>0:
    t.forward(100)
    t.right(deg)
    n -= 1