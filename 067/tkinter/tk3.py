import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()


def test(content):
    return content.isdigit()


testCMD = root.register(test)

e1 = tk.Entry(frame, width=10, textvariable=v1, validate='key', validatecommand=(testCMD, '%P')).grid(row=0, column=0)
tk.Label(frame, text='+').grid(row=0, column=1)
e2 = tk.Entry(frame, width=10, textvariable=v2, validate='key', validatecommand=(testCMD, '%P')).grid(row=0, column=2)
tk.Label(frame, text='=').grid(row=0, column=3)
e2 = tk.Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0, column=4)


def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))


tk.Button(frame, text='计算结果', command=calc).grid(row=1, column=2, pady=5)
tk.Button(frame, text='退出', command=frame.quit).grid(row=1, column=3, pady=5)

tk.mainloop()
