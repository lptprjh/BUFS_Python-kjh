import turtle
import random

def draw_fillmode(t,col,x,y):
    t.penup()
    t.fillcolor(col)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()

def draw_circle(t,col,x,y,rad):
    draw_fillmode(t,col,x,y)
    t.circle(rad)
    t.end_fill()

def draw_rectangle(t,col,x,y,w,h):
    draw_fillmode(t,col,x,y)

    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def draw_trapezoid(t,col,x,y,w,h):
    draw_fillmode(t,col,x,y)
    t.forward(w)
    t.right(60)
    t.forward(h)
    t.right(120)
    t.forward(w+20)
    t.right(120)
    t.forward(h)
    t.right(60)
    t.end_fill()

def draw_star(t,col,x,y,size):
    draw_fillmode(t,col,x,y)
    for i in range(10):
        t.forward(size)
        t.right(144)
    t.end_fill()

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)

x,y = (0,0)

#트리의 줄기
draw_rectangle(t,'brown',x-20,y-50,30,50)

#트리의 잎
w = 240
h = 20
for i in range(10):
    w -= 20
    x = 0 - w/2
    draw_trapezoid(t,'green',x,y,w,h)
    draw_circle(t,'red',
        x+random.randint(0,w),y+random.randint(-h,0), 10)
    y += h

draw_star(t,'yellow', 4,y,100)

Kojin_teki_na_kotomi = ("Arial", 24, 'italic')

t.penup()
t.color('red')
t.goto(-200,250)
t.write("Merry Christmas", font=Kojin_teki_na_kotomi)
t.goto(-200,220)
t.write("Happy New Year!", font=Kojin_teki_na_kotomi)

input("Merry Christmas, Happy New Year! Press Enter to exit...")