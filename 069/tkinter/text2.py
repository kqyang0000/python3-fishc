from tkinter import *

root = Tk()

text = Text(root, width=30, height=30)
text.pack()

text.insert(INSERT, 'I love you\n')
text.insert(END, 'kfc')


def cli():
    print("我被点了一下")


b1 = Button(text, text='点我', command=cli)
text.window_create(INSERT, window=b1)

mainloop()
