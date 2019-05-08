import turtle

def n_polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.right(360//n)

t = turtle.Turtle()
t.speed(0)
deg = 30
for x in range(0,360,deg):
    n_polygon(8,60)
    t.left(deg)