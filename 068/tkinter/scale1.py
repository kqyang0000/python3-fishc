from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=42)
s2 = Scale(root, from_=0, to=200, orient=HORIZONTAL)

s1.pack()
s2.pack()


def show():
    print(s1.get())
    print(s2.get())


Button(root, text='获取位置', command=show).pack()

mainloop()
