import tkinter as tk

root = tk.Tk()

group = tk.LabelFrame(root, text='世界上最好的脚本语言是?', padx=5, pady=5)
group.pack(padx=5, pady=5)

v = tk.IntVar()

# tk.Radiobutton(group, text='one', variable=v, value='1', indicatoron=False).pack(anchor='w', fill='x')
tk.Radiobutton(group, text='java', variable=v, value='1').pack(anchor='w')
tk.Radiobutton(group, text='python', variable=v, value='2').pack(anchor='w')
tk.Radiobutton(group, text='C++', variable=v, value='3').pack(anchor='w')

tk.mainloop()
