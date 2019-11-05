from tkinter import *

root = Tk()

s1 = Scale(root, from_=0, to=42, tickinterval=5, resolution=5, length=200)
s2 = Scale(root, from_=0, to=200, tickinterval=10, orient=HORIZONTAL, length=600)

s1.pack()
s2.pack()

mainloop()
