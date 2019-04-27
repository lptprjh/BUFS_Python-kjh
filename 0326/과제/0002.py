import turtle
t = turtle.Turtle()

s = turtle.textinput("","이름을 입력하시오:")

for i in range(4):
    t.right(90)
    t.forward(250)
    t.write("안녕하세요? "+s+"씨, 터틀 인사드립니다.")