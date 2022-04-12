from tkinter import *
from turtle import width
window =Tk()
window.title =("flash card")
window.config(padx=20,pady=20,bg="#019267")

canvas=Canvas(width=800,height=520)
card_front_img=PhotoImage(file="card_back.png")
canvas.create_image(400,260,image=card_front_img)
canvas.grid(column=0,row=0)

canvas.create_text(400,150,text="Title",font=("Arial",24,"bold"))

window.mainloop()