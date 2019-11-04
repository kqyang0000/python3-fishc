import tkinter as tk

app = tk.Tk()
app.title = 'First Tk'

tk_label = tk.Label(app, text='我的第二个窗口')
tk_label.pack()

app.mainloop()
