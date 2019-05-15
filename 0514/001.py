import turtle
import random

Geobugi = turtle.Turtle()
s = turtle.Screen()

def Geuryeora_Miro(x,y,Geobugi=Geobugi):
    for i in range(2):
        Geobugi.penup()
        if i==1: Geobugi.goto(x+100, y+100)
        else:    Geobugi.goto(x,y)
        Geobugi.pendown()
        Geobugi.forward(300)
        Geobugi.right(90)
        Geobugi.forward(300)
        Geobugi.left(90)
        Geobugi.forward(300)

def Dorara_Oenjjok(Geobugi=Geobugi):
    Geobugi.left(10)
    Geobugi.forward(10)

def Dorara_Oreunjjok(Geobugi=Geobugi):
    Geobugi.right(10)
    Geobugi.forward(10)

Geobugi.shape("turtle")
Geobugi.speed(0)
Geuryeora_Miro(-300,200)

Geobugi.penup()
Geobugi.goto(-300,250)
Geobugi.speed(1)
Geobugi.pendown()

s.onkey(Dorara_Oenjjok,"Left")
s.onkey(Dorara_Oreunjjok,"Right")
s.listen()
s.mainloop()
