from cgi import test
from cgitb import text
from sqlite3 import Row
from tabnanny import check
import tkinter
from tkinter import *
from pkg_resources import to_filename


window=Tk()
window.title("miles to km conv")
window.minsize(width=250,height=250)
window.config(padx=50,pady=50)

def m_to_km():
    miles=miles_input.get()
    km=float(miles)*1.609
    km_label.config(text=f"{km} km")


miles_input= Entry(width=5)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=1,row=1)


equal=Label(text="is equal to ")
equal.grid(column=0,row=2)


km_label=Label(text="0")
km_label.grid(column=1,row=2)

calculate=Button(text="convert",command=m_to_km)
calculate.grid(column=1,row=3)


window.mainloop()
