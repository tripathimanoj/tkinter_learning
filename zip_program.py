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

path_f=Label(text="path of folder") # to zip
path_f.grid(column=4,row=0)

file_name=Label(text="File name") # to zip
path_f.grid(column=4,row=0)

#------------------------------------------------------------ TO UNZIP -------------------------------------------

def unzip_file():     # function to unzip the file.
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




def get_loc():                                  # getting the location of unziped file
    file_to_zip=pathz_entry.get() 
    file_to_unzip=file_to_zip[3:-4] # it will strore only file name
    display_text.insert(END,f"Unzip file path ==> {file_to_zip[0:3]}{file_to_unzip}")


#-----------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------TO ZIP----------------------------------------------------------------

def zip_folder():
    pass
    from shutil import make_archive
    dir_name=pathz_f.get()
    output_filename=file_name.get()
    shutil.make_archive(dir_name[0:3]+output_filename, 'zip', dir_name)


def get_loc_z():
    pass
    dir_name=pathz_f.get()
    output_filename=file_name.get()
    display_text_z.insert(END,f"zip file path ==> {dir_name[0:3]+output_filename}")

    

#-----------------------------------------------------------------------------------------------------------------------
# Entries

pathz_entry = Entry(width=40) # to unzip
pathz_entry.grid(column=1,row=0,columnspan=2)

pathz_f = Entry(width=40) # to zip
pathz_f.grid(column=5,row=0,columnspan=2)

file_name=Entry(width=10)
file_name.grid(column=5,row=1)


#-------------------TO UNZIP-----------------------------------------
unzip=Button(text="Unzip File",width=14,command=unzip_file)  
unzip.grid(column=1,row=1)

get_location=Button(text="output path",width=34,command=get_loc)
get_location.grid(column=1,row=3,columnspan=2)

display_text=Text(height=2,width=35) # displaying the location of unziped file
display_text.grid(column=1,row=4)


#-----------------------TO ZIP----------------------------------------

zip=Button(text="zip Folder",width=14,command=zip_folder)  
zip.grid(column=5,row=2)

get_location_z=Button(text="output path",width=34,command=get_loc_z)
get_location_z.grid(column=5,row=4,columnspan=2)

display_text_z=Text(height=2,width=35) # displaying the location of ziped file
display_text_z.grid(column=5,row=5)


window.mainloop()