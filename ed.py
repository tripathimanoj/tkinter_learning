from cgi import test
from cgitb import text
from sqlite3 import Row
from tabnanny import check
import tkinter
from tkinter import *
from pkg_resources import to_filename


window=Tk()
window.title("text encription")
window.minsize(width=350,height=150)
window.config(padx=50,pady=50)

def ency():
    msg=msg_input.get()
    enc=msg[::-1]
    msg_label.config(text=enc)

def dyc():
    msg=msg_input.get()
    n=msg[::-1]
    n_msg=n[::-1]
    org_label.config(text=n_msg)

def exc():
    path="Program Terminated !"
    my_label2.config(text=path)


my_label2=Label(text="",font=("Arial",30,"bold"))
my_label2.grid(column=3,row=7)




msg_input= Entry(width=15)
msg_input.grid(column=1,row=0)

miles_label=Label(text="your msg")
miles_label.grid(column=1,row=1)


equal=Label(text="encryption  msg =>")
equal.grid(column=0,row=3)

equal=Label(text="decryption msg =>")
equal.grid(column=0,row=5)


msg_label=Label(width=15,text="---")
msg_label.grid(column=1,row=3)

org_label=Label(width=15,text="---")
org_label.grid(column=1,row=5)

b1=Button(text="encrypt",command=ency)
b1.grid(column=1,row=2)

b2=Button(text="decrypt",command=dyc)
b2.grid(column=1,row=4)

button=Button(text="EXIT",command=exc)
button.grid(column=0,row=7)

window.mainloop()
