import turtle

def triangle(length):
    for i in range(3):
        t.forward(length)
        t.right(360/3)

t = turtle.Turtle()
t.speed(10)
for i in range(6):
    for j in range(100,300+1,100):
        triangle(j)
    t.right(360 / 6)