import tkinter as tk
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
textLabel = tk.Label(root, text="猫咪\n可爱", justify=tk.LEFT, padx=10, pady=10)
textLabel.pack(side=tk.LEFT)

img = Image.open('/Users/yangkaiqiang/Desktop/images/cat.jpg')
photo = ImageTk.PhotoImage(img)

imageLabel = tk.Label(root, image=photo)
imageLabel.pack(side=tk.RIGHT)

tk.mainloop()
