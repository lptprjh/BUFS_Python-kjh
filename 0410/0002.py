import turtle

t = turtle.Turtle()

t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오:")

if s == "사각형" or s == '4' or str(s).lower() == 'square' or str(s).lower() == 's':
    w = int(turtle.textinput("","가로: "))
    h = int(turtle.textinput("","세로: "))

    for i in range(4):
        if i%2 == 0: # 가로, 세로, 가로, 세로
            t.forward(w)
        else:
            t.forward(h)
        t.left(90)
elif s == "삼각형" or s == '3' or str(s).lower() == 'triangle' or str(s).lower() == 't':
    length = int(turtle.textinput("","한 변의 길이: "))

    for i in range(3):
        t.forward(length)
        t.left(120)
elif s == '원' or s == '0' or str(s).lower() == 'circle' or str(s).lower() == 'c':
    r = int(turtle.textinput("","반지름: "))

    t.circle(r)