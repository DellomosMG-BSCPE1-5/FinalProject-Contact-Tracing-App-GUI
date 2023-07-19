#This .py file contains the code for the layout of the interface
#import the tkinter module
from tkinter import *
from tkinter import ttk

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
    left_frame = LabelFrame(window, bg="#F5F5F5", borderwidth=0)
    left_frame.place(x=20, y=60, width=470, height=730)
    poster = PhotoImage(file = 'C:\\Users\\Mary Grace\\Downloads\\OOP POSTER.png')
    Label(left_frame, image = poster).place(x=5, y=73)
   
    #right frame
    right_frame_up = LabelFrame(window,text='Contact Information', font=('consolas', 15), fg= "black", bg="#F5F5F5")
    right_frame_up.place(x=500, y=125, width=1015, height=270)
    right_frame_down = LabelFrame(window,bg="#F5F5F5")
    right_frame_down.place(x=500, y=405, width=1015, height=305)

    #create the header/title
    app_title= Label(left_frame, text='Safe Trace', font=('Couture',35, 'bold'), bg="#F5F5F5", fg='red3').grid(
    row=0, column=0, padx=75, pady=7)
    #create the labels
    #create the entry boxes where the user will input their entry
    #create the necessary buttons

    window.mainloop()