'''
import turtle
t = turtle.Turtle()

banghyang = 1 # -1:left | 1:right
while True:
    t.forward(100)
    t.right(90*banghyang)
    t.forward(10)
    t.right(90*banghyang)
    banghyang *= -1
'''

import turtle
t = turtle.Turtle()

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
turtle.bgcolor('black')

t.speed(0)
t.width(3)

length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5