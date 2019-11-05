from tkinter import *

master = Tk()

sb = Scrollbar(master)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(master, yscrollcommand=sb.set)

for item in range(1000):
    lb.insert(END, item)

lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

mainloop()
