# login file -ali abo abid
from tkinter.ttk import *
from tkinter import*
import tkinter.messagebox
import sqlite3
import tkinter as tk


def Print():
    print("Registration Successful")
    tkinter.messagebox.showinfo("Welcome", 'Registration was successful')


def exit1():
    window.destroy()

def ValidateForget():
    root = Tk()
    root.geometry("250x300")

    label_1 = Label(root, text="Id Number", font=("arial", 12))
    label_1.place(x=20, y=150)

    entry31 = Entry(root, textvar=id)
    entry31.place(x=100, y=154)

    label5 = Label(root, text="Phone", font=("arial", 12))
    label5.place(x=20, y=175)

    entry4 = Entry(root, textvar=Phone)
    entry4.place(x=100, y=180)

    def Show():
        id = StringVar(" ")
        password = StringVar(" ")


    def Forget():
        with sqlite3.connect('Form.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM UserTB WHERE id = ? AND Phone = ?")
        cursor.execute(find_user, [(entry31.get()), (entry4.get())])

        results = cursor.fetchone()
        if results:
            find_user = ("INSERT * FROM UserTB WHERE Password=?")
            print(' found')
            #print(' ',Password)
            tkinter.messagebox.showinfo(Password)

        else:
            print('not found')
            print(entry31.get() + " , " + entry4.get())
            tkinter.messagebox.showinfo("user not found", 'user not found')
            sys.exit(1)
    b4 = Button(root, text="show my Password", bg="gold", fg="Black", relief=GROOVE, height=1, width=17,command=Forget)
    b4.place(x=60, y=250)

def new_win():
    root = Tk()
    root.geometry("250x300")

    label_1 = Label(root, text="Id Number", font=("arial", 12))
    label_1.place(x=20, y=150)

    entry31 = Entry(root, textvar=id)
    entry31.place(x=100, y=154)

    label_0 = Label(root, text="Password", font=("arial", 12))
    label_0.place(x=20, y=180)


    def ValidateLogin():
        with sqlite3.connect('Form.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM UserTB WHERE id = ? AND Password = ?")
        cursor.execute(find_user, [(entry31.get()), (entry_4.get())])
        results = cursor.fetchone()
        if  results is not None:
            print(' found')
            print(entry31.get() + " , " + entry_4.get())
            tkinter.messagebox.showinfo("Login Success", 'login was successful')


        else:
            print('not found')
            print(entry31.get() + " , " + entry_4.get())
            #tk.showerror("Login error", "Incorrect password")
            Label(root,text="incorrect password", fg="red", font=("calibri", 11)).pack()
            window.destroy
             #tkinter.messagebox.showinfo("forgot pass word",'forgot password?')
            #sys.exit(1)


    Label(root, text='Login Page.').pack()

    label_1 = Label(root, text="Id Number", font=("arial", 12))
    label_1.place(x=20, y=150)

    entry31 = Entry(root, textvar=id)
    entry31.place(x=100, y=154)

    label_4 = Label(root, text="Password", font=("arial", 12))
    label_4.place(x=20, y=180)

    entry_4 = Entry(root, textvar=Password, show='*')
    entry_4.place(x=100, y=184)
    b3 = Button(root, text="Login", bg="cyan", fg="Black", relief=GROOVE, height=1, width=17, command=ValidateLogin)
    b3.place(x=60, y=220)
    b4 = Button(root, text="Forget Password", bg="cyan", fg="Black",relief=GROOVE,height=1,width=17,command=ValidateForget)
    b4.place(x=60,y=250)



def database():
    ID=id.get()
    LastName = last_name.get()
    FirstName = fn.get()
    email = Email.get()
    password = Password.get()
    phone = Phone.get()

    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS UserTB (FirstName TEXT, Email TEXT, Password TEXT, Phone TEXT,LastName TEXT,ID TEXT)')
    cursor.execute('INSERT INTO UserTB (FirstName, Email, Password, Phone,LastName,ID) VALUES (?, ?, ?, ?,?,?)',
                   (FirstName, email, password, phone, LastName,ID))
    conn.commit()



window=Tk()
id=StringVar()
last_name = StringVar()
fn = StringVar()
Email = StringVar()
Password = StringVar()
Phone = StringVar()
rad_var1 = StringVar()

window.title("Registration Form")
window.geometry("500x500")


# ****************************************************************************************************************************************************
# Sign Up-muhamad fadel
menu = Menu(window)
window.config(menu=menu)
sub_menu1 = Menu(menu)
sub_menu2 = Menu(menu)


menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exit1)

label1 = Label(window, text="Registration Form", relief="solid", font=("Edwardian Script ITC", 20, "bold")).pack()

label21 = Label(window, text="LastName", font=("arial", 15))
label21.place(x=80, y=220)

entry21 = Entry(window, textvar=last_name)
entry21.place(x=200, y=220)

label2 = Label(window, text="First name", font=("arial", 15))
label2.place(x=80, y=190)

entry1 = Entry(window, textvar=fn)
entry1.place(x=200, y=190)

label3 = Label(window, text="Email", font=("arial", 15))
label3.place(x=80, y=250)

entry2 = Entry(window, textvar=Email)
entry2.place(x=200, y=254)

label4 = Label(window, text="Password", font=("arial", 15))
label4.place(x=80, y=280)

entry3 = Entry(window, textvar=Password, show='*')
entry3.place(x=200, y=284)

label41 = Label(window, text="ID", font=("arial", 15))
label41.place(x=80, y=305)

entry31 = Entry(window, textvar=id)
entry31.place(x=200, y=305)

label5 = Label(window, text="Phone", font=("arial", 15))
label5.place(x=80, y=330)

entry4 = Entry(window, textvar=Phone)
entry4.place(x=200, y=330)


label7 = Label(window, text="Gender", font=("arial", 15))
label7.place(x=80, y=380)
r1 = Radiobutton(window, text="Male", variable=rad_var1, value="Male").place(x=200, y=384)
r1 = Radiobutton(window, text="Female", variable=rad_var1, value="Female").place(x=250, y=384)

b1 = Button(window, text="Sign Up", bg="silver", fg="Black", relief=GROOVE, height=3, width=10, command=database)
window.bind("<Return>", database)
b1.place(x=400, y=450)
b2 = Button(window, text="Quit", bg="gold", fg="Black", relief=GROOVE, height=3, width=10, command=exit1)
b2.place(x=20, y=450)
b3 = Button(window, text="Login", bg="black", fg="white", relief=GROOVE, height=3, width=10, command=new_win)
b3.place(x=200, y=450)



window.mainloop()
