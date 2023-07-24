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
    addtl_info_frame.place(x=500, y=405, width=1015, height=65)
    covid_rltd_frame_1 = LabelFrame(window,bg="#F5F5F5")
    covid_rltd_frame_1.place(x=1013, y=480, width=502, height=200)
    covid_rltd_frame_2 = LabelFrame(window,bg="#F5F5F5")
    covid_rltd_frame_2.place(x=500, y=480, width=502, height=277)

    #right frame; Contact Information; LABELS
    first_name_label = Label(contact_info_frame, text="First Name      ", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    last_name_label = Label(contact_info_frame, text="\t     Last Name", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    contact_num_label = Label(contact_info_frame, text="   Contact Number     ", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    email_address_label = Label(contact_info_frame, text="Email Address", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    residential_address_label = Label(contact_info_frame, text="   Residential Address", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    vaccines_received_label = Label(covid_rltd_frame_1, text="Received  COVID-19 Vaccine:", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")

    first_name_label.grid(row=0, column=0, padx=55, pady=10)
    last_name_label.grid(row=0, column=1, padx=0, pady=10)
    contact_num_label.grid(row=1, column=0, padx=25, pady=40)
    email_address_label.grid(row=1, column=1, padx=187, pady=40)
    residential_address_label.grid(row=2, column=0, padx=0, pady=10)
    vaccines_received_label.pack(anchor="w", padx=15, pady=5)

    #right frame; Contact Information; ENTRY
    first_name_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    last_name_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2 )
    contact_num_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    email_address_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    residential_address_input = Entry(contact_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    first_name_input.place(x=60, y=40, width=425, height=30)
    last_name_input.place(x=525, y=40, width=425, height=30)
    contact_num_input.place(x=60, y=115, width=350, height=30)
    email_address_input.place(x=450, y=115, width=500, height=30) 
    residential_address_input.place(x=60, y=190, width=890, height=30)

    #right frame; Additional Information; LABELS
    entry_time_label = Label(addtl_info_frame, text="Time of Arrival at the Premises:", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    entry_time_label.grid(row=0, column=0, padx=55, pady=15)
    entry_date_label = Label(addtl_info_frame, text="Date of Arrival at the Premises:", font=('consolas', 13), fg= "dark red", bg="#F5F5F5")
    entry_date_label.grid(row=0, column=1, padx=125, pady=15)

    #right frame; Additional Information; ENTRY
    entry_time_input = Entry(addtl_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    entry_time_input.place(x=350, y=15, width=70, height=30)
    entry_time_am_pm = ttk.Combobox(addtl_info_frame, values=["A.M.", "P.M."], font=("consolas", 11))
    entry_time_am_pm.place(x=423, y=14.3, width=50, height=30)
    entry_date_input = Entry(addtl_info_frame, font=('consolas', 12), fg= "black", bg="#E6E4E4",relief=GROOVE, bd=2)
    entry_date_input.place(x=825, y=15, width=125, height=30)

    #create the necessary buttons
    vaccines_received_var = StringVar(covid_rltd_frame_1, "1")
    vaccines_received_values = {"No" : "1", "First Dose" : "2", "Second Dose" : "3", "First Booster Shot" : "4", "Second Booster Shot" : "5",}
    for (text, value) in vaccines_received_values.items():
        vaccines_received = Radiobutton(covid_rltd_frame_1, text = text, variable = vaccines_received_var, value = value, bg="#F5F5F5", font=('consolas', 12))
        vaccines_received.pack(anchor="w", padx=15, pady=0)

    window.mainloop()