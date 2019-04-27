import turtle

def drawShape(t, n, length=100):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

def ninja(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t = turtle.Turtle()

drawShape(t,6)
ninja(t, 200,0)
drawShape(t,8)