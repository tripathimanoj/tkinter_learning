
import tkinter
from tkinter import *
from tkinter import font
from turtle import color
window=Tk()
import os

window.title("My first GUI program") 
window.minsize(width=500,height=300) # to resize
window.config(padx=100,pady=100)


my_label=Label(text="I am label",font=("Arial",24,"bold")) # to set label
# my_label.pack(expand=True) # to align ==> side=left or right
my_label.grid(column=0,row=0)

my_label.config(text="new text") # to set config (way 1)
 
my_label["text"]="new data"  # to set config(way 2)

# to create a button

import os
my_label2=Label(text="data",font=("Arial",24,"bold"))
# my_label2.pack()
my_label2.grid(column=1,row=1)


input=Entry(width=10)   # to create input box
# input.place(x=100,y=250) # to set it's location. defautl==> center
input.grid(column=2,row=2)

def button_click():
    print("I got clicked")
    my_label.config(text="you are inside")
    path=os.path.basename(__file__)
    my_label2.config(text=path)


button=Button(text="click me",command=button_click)
# button.pack()
button.grid(column=3,row=3)
















window.mainloop()

