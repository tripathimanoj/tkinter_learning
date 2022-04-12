from cgitb import text
from email.mime import image
from re import T
import tkinter
from tkinter import *
import time
import math


def reset_timer():
    window.after_cancel(timer_window)
    canvas.itemconfig(timer_text, text="00:00:00")
    title.config(text="Timer")
    check.config(text="")


def start_timer():
    count_down(5*60)


def start_time():
    global reps
    reps+=1

    work_sec=work_min*60
    shore_break_sec=short_break*60
    long_break_sec=long_break*60

    if reps%8==0:
        count_down(long_break_sec)
        title.config(text="Long Break Time")

    elif reps%2==0:
        count_down(short_break_sec)
        title.config(text="Short Brak")

    else:
        count_down(work_sec)
        title.config(text="work")




def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count_sec<10:
        canvas.itemconfig(timer_text,text=f"{count_min}:0{count_sec}")
    
    
    
    if count>0:
        global timer_window
        timer_window=window.after(1000,count_down,count-1)

    else:
        start_time()
        mark=""
        work_sessions=reps//2
        for i in range(work_sessions):
            mark+="✅"
        check.config(text=mark)
    




window=Tk()
Pink="#FFF6EA"
Red="#FF1818"
Green="#019267"
Yellow="#FFC300"
# window.minsize(width=500,height=500)
window.title("sample gui")
window.config(padx=100,pady=50,bg=Yellow)


title = Label(text="Timer",fg=Green,font=("Courier",50,"normal"),bg=Yellow)
title.grid(column=1,row=0)
# finding color code.................



work_min=25
short_break=5
long_break=20
canvas=Canvas(width=200,height=230,bg=Yellow,highlightthickness=0)
tomato=PhotoImage(file='t1.png')
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=("Arial",22,"bold"))
canvas.grid(column=1,row=1)


# count_down(5)

start=Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)


reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)


check=Label(text="",fg=Green,bg=Yellow,font=("Courier",22,"bold"))
check.grid(column=1,row=3)


window.mainloop()