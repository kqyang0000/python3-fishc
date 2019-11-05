from tkinter import *
from PIL import Image, ImageTk

root = Tk()

text = Text(root, width=30, height=30)
text.pack()

text.insert(INSERT, 'I love you\n')
text.insert(END, 'kfc')

photo = ImageTk.PhotoImage(Image.open('/Users/yangkaiqiang/Desktop/images/cat.jpg'))


def cli():
    text.image_create(END, image=photo)


b1 = Button(text, text='点我', command=cli)
text.window_create(INSERT, window=b1)

mainloop()
