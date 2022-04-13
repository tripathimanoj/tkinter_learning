import tkinter
from tkinter import *
import time
import math
from tkinter import messagebox
import random

window=Tk()
window.title=("Application")
window.config(padx=50,pady=50)

# ----------------------------------FUNCTION FOR UNZIP--------

def unzip_folder():
    pass


#------------------------------------------------------------

# ----------------------------------FUNCTION FOR ZIP---------

def zip_folder():
    pass

# ------------------------------------------------------------

# ----------------------------------STRUCTURE FOR UNZIP------
my_label=Label(text="ZIP => UNZIP",font=("Arial",20,"bold")) # to set label
my_label.grid(column=1,row=0)

filetz_label=Label(text="file path")
filetz_label.grid(column=0,row=1)

filetz_entry = Entry(width=40)
filetz_entry.grid(column=1,row=1,columnspan=2)

filename_label=Label(text="rename")
filename_label.grid(column=0,row=2)

filename_entry = Entry(width=20)
filename_entry.grid(column=1,row=2)

unzip_f=Button(text="UNZIP",width=14,command=unzip_folder)
unzip_f.grid(column=1,row=3)

display_text_z=Text(height=2,width=35) 
display_text_z.grid(column=1,row=4)

# ------------------------------------------------------------

# ---------------------------------STRUCTURE FOR ZIP----------

my_label=Label(text="FOLDER => ZIP",font=("Arial",20,"bold")) # to set label
my_label.grid(column=4,row=0)

filetu_label=Label(text="file path")
filetu_label.grid(column=3,row=1)

filetu_entry = Entry(width=40)
filetu_entry.grid(column=4,row=1,columnspan=2)

filenameu_label=Label(text="rename")
filenameu_label.grid(column=3,row=2)

filenameu_entry = Entry(width=20)
filenameu_entry.grid(column=4,row=2)

zip_f=Button(text="ZIP",width=14,command=zip_folder)
zip_f.grid(column=4,row=3)

display_text_u=Text(height=2,width=35) 
display_text_u.grid(column=4,row=4)


# -------------------------------------------------------------

window.mainloop()