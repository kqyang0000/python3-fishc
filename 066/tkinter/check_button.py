import tkinter as tk

root = tk.Tk()

GIRLS = ['西施', '貂蝉', '杨玉环', '王昭君']

v = []
for i in GIRLS:
    v.append(tk.IntVar())
    b = tk.Checkbutton(root, text=i, variable=v[-1])
    b.pack(anchor='w')

tk.mainloop()
