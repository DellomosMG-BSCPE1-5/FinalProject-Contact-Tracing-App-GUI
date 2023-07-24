#This .py file contains the code for the layout of the interface
#import the tkinter module
from tkinter import *
from tkinter import ttk

class Layout:
    #create the main window
    window = Tk()
    window.title("Safe Trace")
    window.geometry("1920x1200")
    window.configure(bg="#F5F5F5")

    #create the frames
    #top frame
    header_frame=Label(window,pady=2,bd=12,bg="#C42300", justify=CENTER)
    header_frame.pack(fill=X)

    #left frame
    left_frame = LabelFrame(window, bg="#F5F5F5", borderwidth=0)
    left_frame.place(x=20, y=60, width=470, height=730)
    #left frame: title
    app_title= Label(left_frame, text='Safe Trace', font=('Couture',35, 'bold'), bg="#F5F5F5", fg='red3').grid(
    row=0, column=0, padx=75, pady=7)
    #left frame: poster
    poster = PhotoImage(file = 'C:\\Users\\Mary Grace\\Downloads\\OOP POSTER.png')
    Label(left_frame, image = poster).place(x=5, y=73)
   
    #right frame
    contact_info_frame = LabelFrame(window,text='Contact Information', font=('consolas', 15), fg= "black", bg="#F5F5F5")
    contact_info_frame.place(x=500, y=125, width=1015, height=270)
    addtl_info_frame = LabelFrame(window,bg="#F5F5F5")
    addtl_info_frame.place(x=500, y=405, width=1015, height=305)

    #create the labels
    first_name_label = Label(contact_info_frame, text="First Name", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    first_name_label.grid(row=0, column=0, padx=50, pady=10)
    last_name_label = Label(contact_info_frame, text="Last Name", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    last_name_label.grid(row=0, column=1, padx=325, pady=10)

    #create the entry boxes where the user will input their entry
    first_name_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    first_name_input.place(x=50, y=40, width=425, height=30)
    last_name_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2 )
    last_name_input.place(x=525, y=40, width=425, height=30)

    #create the necessary buttons

    window.mainloop()