from tkinter import *
from turtle import width
import random


to_learn=['w1','d1','sample']
def next_card():
    current_card=random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(card_word,text=current_card)
    canvas.itemconfig(canvas_image,image=card_front_img)


def flip_card():
    canvas.itemconfig(card_word,text=["sample text"])
    canvas.itemconfig(canvas_image,image=card_back_img)
   



window =Tk()
window.title =("flash card")
window.config(padx=20,pady=20,bg="#019267")








canvas=Canvas(width=800,height=520)
card_front_img=PhotoImage(file="card_front.png")

card_back_img=PhotoImage(file="card_back.png")
canvas_image=canvas.create_image(400,260,image=card_front_img)


card_title=canvas.create_text(400,150,text="Title",font=("Arial",24,"bold"))
card_word=canvas.create_text(400,265,text="Word",font=("Arail",62,"italic"))
canvas.grid(column=0,row=0,columnspan=2)
cross_image =PhotoImage(file='wrong.png')
button1=Button(image=cross_image,highlightthickness=0,command=flip_card)
button1.grid(column=0,row=1)
check_image=PhotoImage(file='right.png')
button2=Button(image=check_image,highlightthickness=0,command=next_card)
button2.grid(column=1,row=1)


window.mainloop()