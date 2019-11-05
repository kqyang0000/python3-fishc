import tkinter as tk

master = tk.Tk()
theLB = tk.Listbox(master, selectmode=tk.SINGLE)
theLB.pack()

for item in ['鸡蛋', '鸭蛋', '李狗蛋']:
    theLB.insert(tk.END, item)

theButton = tk.Button(master, text='删除', command=lambda x=theLB: x.delete(tk.ACTIVE))
theButton.pack()

tk.mainloop()
