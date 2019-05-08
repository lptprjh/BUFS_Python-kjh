import turtle

def drawTriangle(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()
    t.color("green")
    for i in range(3):
        t.forward(100)
        t.right(360/3)
    t.end_fill()

t = turtle.Turtle()
s = turtle.Screen()

s.onscreenclick(drawTriangle)

input("종료하시려면 Enter를 누르십시오")