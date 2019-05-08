import turtle

def n_polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.right(360//n)

def ninja(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t = turtle.Turtle()
ninja(-200,0)
for x in range(4):
    n_polygon(5,60)
    ninja(-200 + (x+1)*120,0)