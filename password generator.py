from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("650x445+370+140")

        main_frame = Frame(self.root, bd=5, relief=RIDGE)
        main_frame.place(x=0, y=0, width=650, height=445)

        title_lbl = Label(main_frame, text="Password Generator", font=("times new roman", 15, "bold"), fg="blue", bg="white", border=5, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=650)

        length_lbl = Label(main_frame, text="Enter The Length of Password", font=("times new roman", 15, "bold"), fg="red")
        length_lbl.place(x=40, y=150)

        self.var_entry = StringVar()
        entry_fill = ttk.Entry(main_frame, textvariable=self.var_entry, width=40, font=("times new roman", 15, "bold"))
        entry_fill.place(x=40, y=185)

        btn = Button(main_frame, text="Generate Password", font=("times new roman", 15, "bold"), fg="white", bg="red", border=5, relief=SUNKEN, cursor="hand2", command=self.generate_password)
        btn.place(x=40, y=235, width=555, height=35)

        self.pass_lbl = Label(main_frame, text="Random Password Generator", font=("times new roman", 15, "bold"), fg="green")
        self.pass_lbl.place(x=40, y=290)

    def generate_password(self):
        if self.var_entry.get() == "":
            messagebox.showerror("Error", "Please enter some input")
        else:
            try:
                num = int(self.var_entry.get())
                s1 = string.ascii_lowercase
                s2 = string.ascii_uppercase
                s3 = string.digits
                s4 = string.punctuation

                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))

                random.shuffle(s)
                password = ''.join(s[:num])

                self.pass_lbl.config(text=password)

            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

if __name__ == "__main__": 
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()

#simple password generater 




