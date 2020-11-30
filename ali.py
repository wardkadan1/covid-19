#Login file-Ali Abu Abid
from tkinter import *
import tkinter.messagebox


import sqlite3

def Print():

    print("Registration Successful")
    tkinter.messagebox.showinfo("Welcome", 'Registration was successful')

def exit1():
    window.destroy()

def new_win():
    root = Tk()
    root.geometry("250x300")
    root.title('Login Page')
    def ValidateLogin():
        with sqlite3.connect('Form.db') as db:
            cursor = db.cursor()
        find_user= ("SELECT * FROM UserTB WHERE Email = ? AND Password = ?")
        cursor.execute(find_user,[(entry_2.get()),(entry_4.get())])
        results = cursor.fetchone()
        if results :
            print(' found')
            print(entry_2.get()+" , "+entry_4.get())
            tkinter.messagebox.showinfo("Login Success", 'login was successful')


        else:
            print('not found')
            print(entry_2.get()+" , "+entry_4.get())
            tkinter.messagebox.showinfo("Error", 'Error')



    Label(root, text='Login Page.').pack()
    label_1 = Label(root, text="Email", font=("arial", 12))
    label_1.place(x=20, y=150)

    entry_2 = Entry(root, textvar=Email)
    entry_2.place(x=100, y=154)

    label_3 = Label(root, text="Password", font=("arial", 12))
    label_3.place(x=20, y=180)

    entry_4 = Entry(root, textvar=Password, show='*')
    entry_4.place(x=100, y=184)
    b3 = Button(root, text="Login", bg="cyan", fg="Black", relief=GROOVE, height=1, width=4, command=ValidateLogin)
    b3.place(x=120, y=220)


def database():
    Name = fn.get()
    email = Email.get()
    password = Password.get()
    phone = Phone.get()

    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS UserTB (Name TEXT, Email TEXT, Password TEXT, Phone TEXT)')
    cursor.execute('INSERT INTO UserTB (Name, Email, Password, Phone) VALUES (?, ?, ?, ?)',
                   (Name, email, password, phone))
    conn.commit()


window = Tk()
fn = StringVar()
Email = StringVar()
Password = StringVar()
Phone =StringVar()
rad_var1=StringVar()
window.title("Registration Form")
window.geometry("500x500")


#Sign up-Mohamad eghbarya


menu = Menu(window)
window.config(menu=menu)
sub_menu1 = Menu(menu)
sub_menu2 = Menu(menu)

menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exit1)



label1 = Label(window, text="Registration Form", relief="solid", font=("Edwardian Script ITC", 20, "bold")).pack()

label2 = Label(window, text="Full name", font=("arial", 15))
label2.place(x=80, y=220)

entry1 = Entry(window, textvar=fn)
entry1.place(x=200, y=224)

label3 = Label(window, text="Email", font=("arial", 15))
label3.place(x=80, y=250)

entry2 = Entry(window, textvar=Email)
entry2.place(x=200, y=254)

label4 = Label(window, text="Password", font=("arial", 15))
label4.place(x=80, y=280)

entry3 = Entry(window, textvar=Password , show='*')
entry3.place(x=200, y=284)

label5 = Label(window, text="Phone", font=("arial", 15))
label5.place(x=80, y=330)
entry3 = Entry(window, textvar=Phone)
entry3.place(x=200, y=330)

label7 = Label(window, text="Gender", font=("arial", 15))
label7.place(x=80, y=380)
r1 = Radiobutton(window, text="Male", variable=rad_var1, value="Male").place(x=200, y=384)
r1 = Radiobutton(window, text="Female", variable=rad_var1, value="Female").place(x=250, y=384)

b1 = Button(window, text="Sign Up", bg="blue", fg="Black", relief=GROOVE, height=3, width=10, command=database)
window.bind("<Return>", database)
b1.place(x=400, y=450)
b2 = Button(window, text="Quit", bg="red", fg="Black", relief=GROOVE, height=3, width=10, command=exit1)
b2.place(x=20, y=450)
b3 = Button(window, text="Login", bg="green", fg="Black", relief=GROOVE, height=3, width=10, command=new_win)
b3.place(x=200, y=450)

window.mainloop()