import tkinter
from tkinter import *

window=Tk()
window.minsize(width=250,height=250)
window.config(padx=20,pady=20)

# ----------------------------------------------

# to add text box...

# text=Text(height=5,width=30)
# text.focus()
# text.insert(END,"excample of test box")
# text.grid(column=1,row=4)

# ----------------------------------------------

def spin():
    print(spinbpx.get())

spinbpx=Spinbox(from_=0,to_ =10,width=5, command=spin)
spinbpx.pack()

# ----------------------------------------------

# for scaled (vertical bar)

def scale_used(value):
    print(value)


scale=Scale(from_=0,to_ =100, command=scale_used)
scale.pack()

# ------------------------------------------------

# for check button. 

def check_used():
    print(check.get())


check=IntVar()
checkbutton=Checkbutton(text=" Is On?", variable=check,command=check_used)
checkbutton.pack()


# -----------------------------------------------

# for radio button

def radio_used():
    print(radio.get())

radio=IntVar()
radio_button1=Radiobutton(text="option1",value=1,variable=radio,command=radio_used)
radio_button1.pack()

radio_button2=Radiobutton(text="option2",value=2,variable=radio,command=radio_used)
radio_button2.pack()

# ----------------------------------------------------

# for listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox=Listbox(height=4)
data=["first","second","third","four"]
for item in data:
    listbox.insert(data.index(item),item)

listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()


# ----------------------------------------------------






window.mainloop()
