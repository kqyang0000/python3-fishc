from tkinter import *

root = Tk()

text = Text(root, width=30, height=30)
text.pack()

text.insert(INSERT, 'I love you\n')
text.insert(END, 'kfc')

mainloop()
