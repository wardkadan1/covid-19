# login file -ali abo abead
from tkinter import *
import tkinter.messagebox
from tkinter import font as tkFont
import sqlite3
import webbrowser
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog

def Print():

    print("Registration Successful")

    tkinter.messagebox.showinfo("Welcome", 'Registration was successful')

def frame_destroy(frame):

    frame.destroy()

def exit1():

    window.destroy()

def Open_itch():

    webbrowser.open("https://www.ox.ac.uk/")

def the_main_page():

    root = Tk()
    root.geometry("500x500")
    root.title('our app')
    second_frame = Frame(root)
    second_frame.place(x=0, y=0, width=500, height=500)
    first_frame = Frame(root)
    first_frame.place(x=0, y=0, width=500, height=500)
    Button(second_frame, text="Switch back to page 1", width=20, bg='brown', fg='white',command=lambda: raise_frame(first_frame)).place(x=180, y=380)
    Button(first_frame, text='Submit', width=20, bg='brown', fg='white',command=lambda: raise_frame(second_frame)).place(x=180, y=380)
    Button(first_frame, text='welcome to the page', width=20, bg='brown', fg='white',command=lambda: t()).pack()

    def t():
        menu1 = Menu(first_frame)
        new_item = Menu(menu1)
        new_item.add_command(label='the covid data', command=lambda: raise_frame(second_frame))
        menu1.add_cascade(label='covid', menu=new_item)
        new_item.add_command(label="Exit", command=exit1)
        label1=Label(first_frame,text='the welcome page').pack()
        tab_control = ttk.Notebook(root)

        tab1 = ttk.Frame(tab_control)

        tab2 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='First')

        tab_control.add(tab2, text='Second')

        button = Button(tab1, text="oxford", command=Open_itch).grid(row=200, column=200, sticky=E, pady=2)

        tab_control.pack(expand=1, fill='both')
        root.config(menu=menu1)
        root.iconbitmap('/Users/HP/Downloads/p.ico')
def raise_frame(frame):
    frame.tkraise()
def new_win():
    root = Tk()
    root.geometry("250x300")
    root.title('Login Page')

    def ValidateLogin():
        with sqlite3.connect('Form.db') as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM 1 WHERE Email = ? AND Password = ?")
        cursor.execute(find_user, [(entry_2.get()), (entry_4.get())])
        results = cursor.fetchone()
        if results:
            print(' found')
            print(entry_2.get() + " , " + entry_4.get())
            """tkinter.messagebox.showinfo("Login Success", 'login was successful')"""

            the_main_page()

        else:
            print('not found')
            print(entry_2.get() + " , " + entry_4.get())
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


# Sign Up-muhamad fadel
def database():
    ID = id.get()
    LastName = last_name.get()
    FirstName = fn.get()
    email = Email.get()
    password = Password.get()
    phone = Phone.get()

    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS UserTB1 (FirstName TEXT, Email TEXT, Password TEXT, Phone TEXT,LastName TEXT,ID TEXT)')
    cursor.execute('INSERT INTO UserTB1 (FirstName, Email, Password, Ph'
                   'one,LastName,ID) VALUES (?, ?, ?, ?,?,?)',
                   (FirstName, email, password, phone, LastName, ID))
    conn.commit()


window = Tk()
id = StringVar()
last_name = StringVar()
fn = StringVar()
Email = StringVar()
Password = StringVar()
Phone = StringVar()
rad_var1 = StringVar()
window.title("Registration Form")
window.geometry("500x500")
# ****************************************************************************************************************************************************

menu = Menu(window)
window.config(menu=menu)
sub_menu1 = Menu(menu)
sub_menu2 = Menu(menu)

menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exit1)

label1 = Label(window, text="Registration Form", relief="solid", font=("Edwardian Script ITC", 20, "bold")).pack()

label21 = Label(window, text="LastName", font=("arial", 15))
label21.place(x=80, y=190)

entry21 = Entry(window, textvar=last_name)
entry21.place(x=200, y=190)

label2 = Label(window, text="First name", font=("arial", 15))
label2.place(x=80, y=220)

entry1 = Entry(window, textvar=fn)
entry1.place(x=200, y=224)

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

entry31 = Entry(window, textvar=id, show='*')
entry31.place(x=200, y=309)

label5 = Label(window, text="Phone", font=("arial", 15))
label5.place(x=80, y=330)

entry4 = Entry(window, textvar=Phone)
entry4.place(x=200, y=334)



managementList = ["Gender","Female", "Male"]

selectedRadiobutton = StringVar()
selectedRadiobutton.set(managementList[0])

RadiobuttonMenu = OptionMenu(window, selectedRadiobutton, *managementList)
RadiobuttonMenu.place(x=200, y=374)

managementList =sorted({'access','management', 'doctor', 'Patient'})

selectedmanagement = StringVar()
selectedmanagement.set('access')

managementMenu = OptionMenu(window, selectedmanagement, *managementList)
managementMenu.place(x=200, y=400)


def change_dropdown(*args):

    global dropdown
    dropdown=str(selectedmanagement.get())
    print(dropdown)

    if selectedmanagement.get()=="management":
        pass

selectedmanagement.trace('w',change_dropdown)
b1 = Button(window, text="Sign Up", bg="silver", fg="Black", relief=GROOVE, height=3, width=10, command=database)
window.bind("<Return>", database)
b1.place(x=400, y=450)
b2 = Button(window, text="Quit", bg="gold", fg="Black", relief=GROOVE, height=3, width=10, command=exit1)
b2.place(x=20, y=450)
b3 = Button(window, text="Login", bg="black", fg="white", relief=GROOVE, height=3, width=10, command=lambda :new_win())
b3.place(x=200, y=450)
var=456
window.mainloop()
