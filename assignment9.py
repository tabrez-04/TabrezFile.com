from tkinter import *

count = Tk()
count.geometry("310x320")
count.config(background="white")

header = Entry(count, width=50, borderwidth=5)
header.grid(row=0, column=0, columnspan=4,pady=10)


count.title("🔢Calculator")


def on_click(number):
    current = header.get()
    header.delete(0, END)
    header.insert(0, str(current) + str(number))


def on_eval():
    current = header.get()
    header.delete(0, END)
    header.insert(END, eval(current))


def header_clear():
    header.delete(0, END)
  

def header_clear_last():
    current = str(header.get())
    current = current[:-1]
    header.delete(0, END)
    header.insert(0, current)


(Button(count,  text="0", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("0"))).grid(row=5, column=0)
(Button(count,  text=".", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("."))).grid(row=5, column=1)
(Button(count,  text="=", padx=32, pady=15, background = "black", foreground = "white", command=lambda: on_eval())).grid(row=5, column=2)
(Button(count,  text="+", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("+"))).grid(row=5, column=3)

(Button(count,  text="1", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("1"))).grid(row=4, column=0)
(Button(count,  text="2", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("2"))).grid(row=4, column=1)
(Button(count,  text="3", padx=32, pady=15, background = "black", foreground = "white", command=lambda: on_click("3"))).grid(row=4, column=2)
(Button(count,  text="-", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("-"))).grid(row=4, column=3)

(Button(count,  text="4", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("4"))).grid(row=3, column=0)
(Button(count,  text="5", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("5"))).grid(row=3, column=1)
(Button(count,  text="6", padx=32, pady=15, background = "black", foreground = "white", command=lambda: on_click("6"))).grid(row=3, column=2)
(Button(count,  text="x", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("*"))).grid(row=3, column=3)

(Button(count,  text="7", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("7"))).grid(row=2, column=0)
(Button(count,  text="8", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("8"))).grid(row=2, column=1)
(Button(count,  text="9", padx=32, pady=15, background = "black", foreground = "white", command=lambda: on_click("9"))).grid(row=2, column=2)
(Button(count,  text="÷", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("/"))).grid(row=2, column=3)

(Button(count,  text="(", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click("("))).grid(row=1, column=0)
(Button(count,  text=")", padx=30, pady=15, background = "black", foreground = "white", command=lambda: on_click(")"))).grid(row=1, column=1)
(Button(count,  text="CE", padx=30, pady=15, background = "black", foreground = "white", command=lambda: header_clear_last())).grid(row=1, column=2)
(Button(count,  text="AC", padx=30, pady=15, background = "black", foreground = "white", command=lambda: header_clear())).grid(row=1, column=3)


count.mainloop()