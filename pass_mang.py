from cgitb import text
from email.mime import image
from re import T
import tkinter
from tkinter import *
import time
import math
from tkinter import messagebox
import random

def generate_password():
    password_entry.insert(END,"")
    letter=['a','b','c','d','e','f','g','h','i','j','k']
    numbers=[0,1,2,3,4,5,6,7,8,9]
    symbols=['!','#','%','&','*']

    nr_letter=random.randint(0,10)
    nr_numbers=random.randint(2,5)
    nr_symbols=random.randint(2,4)
    password_list=[]

    for c in range(nr_letter):
        password_list.append(random.choice(letter))
    
    for c in range(nr_letter):
        password_list.append(random.choice(numbers))

    for c in range(nr_letter):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password_date="".join(password_list)
    print(password_date)
    password_entry.delete(0,END)
    password_entry.insert(0,password_date)

def save():
    website=website_entry.get()
    email=email_entry.get()
    pas=password_entry.get()

    if len(website)==0 or len(pas)==0 or len(email)==0:
        not_empty=messagebox.showinfo(title="oops",messagebox="fill all required box")


    is_ok= messagebox.askokcancel(title=website,message="successfully submitted")
    if is_ok or not_empty:
         with open("data.text","a")as data_file:
             data_file.write(f"{website} , {email} , {pas} \n")
             website_entry.delete(0,END)
             password_entry.delete(0,END)
             email_entry.delete(0,END)




window=Tk()
window.title=("Panssword manager")
window.config(padx=150,pady=150)
website_label=Label(text="website")
website_label.grid(column=0,row=0)
email_label=Label(text="email")
email_label.grid(column=0,row=1)
password_label=Label(text="password")
password_label.grid(column=0,row=2)

# Entries

website_entry = Entry(width=40)
website_entry.grid(column=1,row=0,columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1,row=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=2,column=1)

generate_password=Button(text="Generate password",width=14,command=generate_password)
generate_password.grid(column=2,row=2)
add_button=Button(text="Add",width=34,command=save)
add_button.grid(column=1,row=3,columnspan=2)

window.mainloop()









