import tkinter as tk

root = tk.Tk()

tk.Label(root, text='作品：').grid(row=0, column=0)
tk.Label(root, text='作者：').grid(row=1, column=0)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print('作品:《%s》' % e1.get())
    print('作者: %s' % e2.get())


tk.Button(root, text='获取信息', width=10, command=show).grid(row=2, column=0, sticky='w', padx=10, pady=5)
tk.Button(root, text='退出', width=10, command=root.quit).grid(row=2, column=1, sticky='e', padx=10, pady=5)

tk.mainloop()
