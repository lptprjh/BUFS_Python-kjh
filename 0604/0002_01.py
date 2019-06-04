from tkinter import *

def packAll(widgets):
    for a in widgets.values():
        for b in a.values():
            b.pack()

window = Tk()
window_1 = {
    'Label':dict(),
    'Entry':dict(),
    'Button':dict()
}

window_1['Label']['화씨'] = Label(window, text="화씨")
window_1['Label']['섭씨'] = Label(window, text="섭씨")
window_1['Entry']['화씨'] = Entry(window)
window_1['Entry']['섭씨'] = Entry()
window_1['Button']['F2C'] = Button(window, text="화씨=>섭씨")
window_1['Button']['C2F'] = Button(window, text="섭씨=>화씨")

packAll(window_1)

window.mainloop()
