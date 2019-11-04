import tkinter as tk
from PIL import Image
from PIL import ImageTk


def callback():
    var.set('吹吧你')


root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

var = tk.StringVar()
var.set('未满18岁禁止点击')

textLabel = tk.Label(frame1, textvariable=var, justify=tk.LEFT)
textLabel.pack(side=tk.LEFT)

img = Image.open('/Users/yangkaiqiang/Desktop/images/cat.jpg')
photo = ImageTk.PhotoImage(img)

imageLabel = tk.Label(frame1, image=photo)
imageLabel.pack(side=tk.RIGHT)

theButton = tk.Button(frame2, text='我已满18岁', command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

tk.mainloop()
