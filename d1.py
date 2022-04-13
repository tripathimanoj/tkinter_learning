import tkinter
from tkinter import *
import time
import math
from tkinter import messagebox
import shutil
# from shutil import make_archive
import os


window=Tk()
window.title=("File Unzipper")
window.config(padx=50,pady=50)
path_z=Label(text="path of zip") # to unzip
path_z.grid(column=0,row=0)


def unzip_file():
    '''
    This function is for unzip the zip folder
    it will create the new folder of same name
    it takes zero arguments at the time of calling.

    '''
    # import shutil
    # import os
    file_to_zip=pathz_entry.get() 
    file_to_unzip=file_to_zip[3:-4] # it will strore only file name
    shutil.unpack_archive(file_to_zip, file_to_zip[0:3]+file_to_unzip) # Drive path + file name 

def get_loc():
    pass




pathz_entry = Entry(width=40) # to unzip
pathz_entry.grid(column=1,row=0,columnspan=2)

unzip=Button(text="Unzip File",width=14,command=unzip_file)  
unzip.grid(column=1,row=1)

get_location=Button(text="output path",width=34,command=get_loc)
get_location.grid(column=1,row=3,columnspan=2)

display_text=Text(height=2,width=35) # displaying the location of unziped file
display_text.grid(column=1,row=4)



window.mainloop()