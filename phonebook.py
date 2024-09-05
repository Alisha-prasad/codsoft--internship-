from tkinter import*
from tkinter import ttk
from view import *
from tkinter import messagebox


#color which i am going to using from making a frame and text 
col1="#ffffff"

main_frame=Tk()
main_frame.title("")
main_frame.geometry('485x450')
main_frame.configure(background=col1) 
main_frame.resizable(width=FALSE,height=FALSE)

#frame
frame_1=Frame(main_frame,width=500,height=50,bg="blue")
frame_1.grid(padx=0,pady=1)

frame_2=Frame(main_frame,width=500,height=150,bg="white")
frame_2.grid(row=1,padx=0,pady=1)


frame_table=Frame(main_frame,width=500,height=50,bg="white",relief=FLAT)
frame_table.grid(row=2,column=0,columnspan=2,padx=0,pady=1,sticky=NW)

#functions
def show():
    global tree

    table_header=['Name','Email id','Phone Number','Address']

    demo_test= view()
    tree=ttk.Treeview(frame_table,selectmode="extended",columns=table_header,show="headings")

    vsb=ttk.Scrollbar(frame_table,orient="vertical",command=tree.yview)
    hsb=ttk.Scrollbar(frame_table,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    tree.grid(column=1,row=0,sticky='ns')
    tree.grid(column=0,row=1,sticky='ew')

    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Email id',anchor=NW)
    tree.heading(2,text='Phone Number',anchor=NW)
    tree.heading(3,text='Address',anchor=NW)

    tree.column(0,width=80,anchor='nw')
    tree.column(1,width=100,anchor='nw')
    tree.column(2,width=150,anchor='nw')
    tree.column(3,width=180,anchor='nw')

    for item in demo_test:
        tree.insert('','end',values=item)
    
show()

def insert():
    Name=e_name.get()
    Email=e_email.get()
    Phonenumber=e_phonenumber.get()
    Address=e_address.get()

    data=[Name,Email,Phonenumber,Address]

    if Name =='' or Email =='' or Phonenumber =='' or Address =='':
        messagebox.showwarning('data','please fill all the details')
    
    else:
        add(data)
        messagebox.showinfo('data','data added successfully')

        e_name.delete(0,'end')
        e_email.delete(0,'end')
        e_phonenumber.delete(0,'end')
        e_address.delete(0,'end')

        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list=tree_dictionary['values']

        Name= str(tree_list[0])
        Email= str(tree_list[1])
        Phonenumber =str(tree_list[2])
        Address= str(tree_list[3])

        e_name.insert(0,Name)
        e_email.insert(0,Email)
        e_phonenumber.insert(0,Phonenumber)
        e_address.insert(0,Address)

        def confirm():
            new_name=e_name.get()
            new_email=e_email.get()
            new_phonenumber=e_phonenumber.get()
            new_address=e_address.get()

            data=[new_phonenumber,new_name,new_email,new_phonenumber,new_address]

            update(data)

            messagebox.showinfo('success','data update sucessfully')

            e_name.delete(0,'end')
            e_email.delete(0,'end')
            e_phonenumber.delete(0,'end')
            e_address.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy()
            
            b_confirm.destroy()

            show()

        b_confirm=Button(frame_2,text="Confirm",bg="red",height=1,width=15,font=('Ivy 8 bold'),command=confirm)
        b_confirm.place(x=250,y=110)

    except IndexError:
        messagebox.showerror('error','select one of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list=tree_dictionary['values']
        tree_phonenumber = str[tree_list[2]]

        remove(tree_phonenumber)

        messagebox.showinfo('sucess','data has been deleted sucessfully')

        for widget in frame_table.winfo_children():
            widget.destroy()
        
        show()

    except IndexError:

        messagebox.showerror('error','select one of them from the table')
def to_search():
    Phonenumber=e_search.get()
    data=search(phonenumber)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('','end',values=item)


#columns up
label_1=Label(frame_1,text="CONTACT BOOK",font=("Verdana 17 bold"),fg="white",bg="blue")
label_1.place(x=5,y=5)

#columns downs
label_2=Label(frame_2,text="Name:",width=20,height=1,font=('Ivy 10'),bg="white",anchor=NW)
label_2.place(x=10,y=20)
e_name=Entry(frame_2,width=25,justify="left",highlightthickness=1,relief=SOLID)
e_name.place(x=60,y=20)

label_2=Label(frame_2,text="Email i'd:",width=20,height=1,font=('Ivy 10'),bg="white",anchor=NW)
label_2.place(x=10,y=50)
e_email=Entry(frame_2,width=25,justify="left",highlightthickness=1,relief=SOLID)
e_email.place(x=70,y=50)

label_2=Label(frame_2,text="Phone Number:",width=20,height=1,font=('Ivy 10'),bg="white",anchor=NW)
label_2.place(x=10,y=80)
e_phonenumber=Entry(frame_2,width=25,justify="left",highlightthickness=1,relief=SOLID)
e_phonenumber.place(x=110,y=80)

label_2=Label(frame_2,text="Address:",width=20,height=1,font=('Ivy 10'),bg="white",anchor=NW)
label_2.place(x=10,y=110)
e_address=Entry(frame_2,width=25,justify="left",highlightthickness=1,relief=SOLID)
e_address.place(x=90,y=110)

#now search button for list
button_search=Button(frame_2,text="Search",bg="red",height=1,width=7,font=('Ivy 8 bold'))
button_search.place(x=285,y=20)
e_button_search=Entry(frame_2,width=16,justify="left", font=('Ivy 11 bold'),highlightthickness=1,relief=SOLID)
e_button_search.place(x=347,y=20)

view_search=Button(frame_2,text="View",bg="red",height=1,width=7,font=('Ivy 8 bold'))
view_search.place(x=285,y=60)

add_search=Button(frame_2,text="Add",bg="red", width=15,height=1,font=('Ivy 8 bold'), command= insert)
add_search.place(x=360,y=60)


update_search=Button(frame_2,text="Update",bg="red",height=1,width=15,font=('Ivy 8 bold') ,command= to_update)
update_search.place(x=360,y=90)

delete_search=Button(frame_2,text="Delete",bg="red",height=1,width=15,font=('Ivy 8 bold') ,command=to_remove)
delete_search.place(x=360,y=120)


main_frame.mainloop()
