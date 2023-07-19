#This .py file contains the code for the layout of the interface
#import the tkinter module
from tkinter import *

class Layout:
    #create the main window
    window = Tk()
    window.title("Safe Trace")
    window.geometry("1920x1080")
    window.configure(bg="#F5F5F5")

    #create the frames
    #top random plain header
    header_frame=Label(window,pady=2,bd=12,bg="#C42300", justify=CENTER)
    header_frame.pack(fill=X)

    #left frame
    left_frame = LabelFrame(window, bg="#F5F5F5")
    left_frame.place(x=20, y=63, width=470, height=710)

    #right frame
    right_frame = LabelFrame(window,bg="#F5F5F5")
    right_frame.place(x=500, y=63, width=1015, height=710)

    #create the header/title
    #create the labels
    #create the entry boxes where the user will input their entry
    #create the necessary buttons

    window.mainloop()