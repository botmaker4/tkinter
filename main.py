import tkinter as tk
from tkinter import Label
from tkinter.ttk import Combobox
import time
import sys

master = tk.Tk()
master.geometry("400x350+400+50")
master.title("CLOCK")
master.attributes('-fullscreen', True)
master.configure(bg="black")
def updater_time():
    updated = time.strftime("%I:%M:%S %p")
    settings.config(text=updated)
    settings.after(200, updater_time)

def update_color():
    settings.config(fg=list.get())


list = Combobox(master, values=["white", "red", "green", "blue"])
list.set("white")
list.grid(row=1, column=0)

b1 = tk.Button(master, text='next', command=update_color)
b1.grid(row=1, column=1)

settings = Label(master, font=("Calibri", 90), bg="black", fg=list.get())
settings.grid(row=0, column=0, columnspan=2)

updater_time()
master.mainloop()
