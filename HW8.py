from tkinter import *

top = Tk()
top.geometry("400x450")
top.config(background="Blue")

user_name = Label(top, text= "Name").place(x=40, y=60)
user_password = Label(top, text="Password").place(x=40, y=100)
user_fathers_name = Label(top, text="Father name").place(x=40, y=140)
user_phone_number = Label(top, text="Phone number").place(x=40, y=180)
user_email = Label(top, text="E-mail").place(x=40, y=220)
user_address = Label(top, text="Adress").place(x=40, y=260)
user_city = Label(top, text="City").place(x=40, y=300)
user_country = Label(top, text="Country").place(x=40, y=340)
submit_buttom = Button(top, text="Submit", background="Green", font=11, foreground="Yellow").place(x=40, y=380)

user_name_input_area = Entry(top).place(x=130, y=60)
user_password_input_area = Entry(top).place(x=130, y=100)
user_fathers_name_input_area = Entry(top).place(x=130, y=140)
user_phone_number_input_area = Entry(top).place(x=130, y=180)
user_email_input_area = Entry(top).place(x=130, y=220)
user_address_input_area = Entry(top).place(x=130, y=260)
user_city_input_area = Entry(top).place(x=130, y=300)
user_country_input_area = Entry(top).place(x=130, y=340)

top.mainloop()