import turtle

t = turtle.Turtle()
t.width(3)
t.shape("turtle")
t.shapesize(3,3)

while True:
    cmd = input("명령을 입력하시오: ")
    
    cmd = str.lower(cmd)

    if cmd == 'l' or cmd == 'left':
        t.left(90)
        t.forward(100)
    elif cmd == 'r' or cmd == 'right':
        t.right(90)
        t.forward(100)
    elif cmd == 'f' or cmd == 'forward':
        t.forward(100)
    elif cmd == 'q' or cmd == 'quit':
        quit(0)