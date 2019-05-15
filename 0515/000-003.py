import turtle, random

t = turtle.Turtle()

def draw_circle(t=t, color, x, y, rad):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    t.fillcolor(color)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

def draw_rectangle(t, color, x, y, w, h):
    t.penup()
    t.goto(x,y)
    t.pendown()

    t.fillcolor()