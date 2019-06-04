from tkinter import *

window = Tk()
def hello():
    print("Hello, world!")


button = Button(window, text="클릭하세요!", command=hello)
button.pack()

window.mainloop()
