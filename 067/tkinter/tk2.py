import tkinter as tk

root = tk.Tk()

tk.Label(root, text='账号：').grid(row=0, column=0)
tk.Label(root, text='密码：').grid(row=1, column=0)

v1 = tk.StringVar()
v2 = tk.StringVar()


def chk(content, reason, name):
    if e1.get() == 'a':
        print(content, reason, name)
        return True
    else:
        e1.delete(0, tk.END)
        return False


def fallback():
    print('我被调用了')


# 函数绑定
regChk = root.register(chk)

# 失去焦点时验证
# invalidcommand 只有当validatecommand函数返回false时才回被调用
e1 = tk.Entry(root, textvariable=v1, validate='focusout', validatecommand=(regChk, '%P', '%v', '%W'),
              invalidcommand=fallback)
e2 = tk.Entry(root, textvariable=v2, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print('账号: %s' % e1.get())
    print('密码: %s' % e2.get())


tk.Button(root, text='登陆', width=10, command=show).grid(row=2, column=0, sticky='w', padx=10, pady=5)
tk.Button(root, text='退出', width=10, command=root.quit).grid(row=2, column=1, sticky='e', padx=10, pady=5)

tk.mainloop()
