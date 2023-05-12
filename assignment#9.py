from tkinter import * 

count = Tk()
count.geometry("350x500")
count.config(background="black")
count.title("🔢 Calculator", )

datas = []

def add():
    global datas
    datas.append(entry.get())

Button(count, text='1', command=add, background="grey", foreground="white", fontsize="100px" ).place(x=20, y=170, )
Button(count, text='4', command=add, background="grey", foreground="white", font="100px" ).place(x=20, y=200, )
Button(count, text='1/x', command=add, background="grey", foreground="white", font="100px" ).place(x=20, y=230, )
Button(count, text='%', command=add, background="grey", foreground="white", font="100px" ).place(x=20, y=260, )
Button(count, text='1', command=add, background="grey", foreground="white", font="100px" ).place(x=20, y=290, )

count.mainloop()