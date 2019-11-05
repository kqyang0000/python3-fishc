import tkinter as tk

master = tk.Tk()
theLB = tk.Listbox(master, selectmode=tk.EXTENDED, height=14)
theLB.pack()

for item in range(19):
    theLB.insert(tk.END, item)

tk.mainloop()
