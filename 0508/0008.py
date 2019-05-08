import turtle

t = turtle.Turtle()
t.speed(0)
t.right(180)

def sier(length):
    if length > 5:
        for i in range(3):
            sier(length/2)
            t.forward(length)
            t.right(120)

sier(200)

