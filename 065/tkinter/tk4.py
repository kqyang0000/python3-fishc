import tkinter as tk
from PIL import Image
from PIL import ImageTk

root = tk.Tk()

img = Image.open('/Users/yangkaiqiang/Desktop/images/cat.jpg')
photo = ImageTk.PhotoImage(img)

imageLabel = tk.Label(root, text='猫咪', image=photo, justify=tk.LEFT, compound=tk.CENTER, font=('宋体', 20), fg='white')
imageLabel.pack()

tk.mainloop()
