from tkinter import *
from tkinter.ttk import *

from time import strftime

window = Tk()
window .title("My first Tkinter windows")

def showTime():
    string = strftime("%r")
    clock.config(text=string)
    clock.after(1000, showTime)

clock = Label(window, font=("DilleniaUPC", 100), background="Blue", foreground="white")
clock.pack()

showTime()
mainloop()