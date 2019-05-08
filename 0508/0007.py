import turtle

def move(x,y):
    t.goto(x,y)

t = turtle.Turtle()
s = turtle.Screen()

t.shape("turtle")
t.pensize(10)
s.onscreenclick(move)
input("종료하시려면 Enter를 입력하세요")