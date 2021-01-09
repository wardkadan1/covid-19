import sqlite3
from tkinter import*
import tkinter.messagebox



def new_win():
    root = Tk()
    root.geometry("10x20")


def exit1():
    window.destroy()


def database():
    PatientID=id.get()
    LastName = las.get()
    FirstName = fn.get()
    DocName = first.get()
    Doctlast = last.get()
    Date=day.get()
    Time=time.get()
    Corona=corona.get()




    conn = sqlite3.connect("HospitalManagement.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS UserTB (Firstname TEXT, PatientID TEXT, DocName TEXT, Doctlast TEXT,LastName TEXT,Date TEXT,Time TEXT,Corona TEXT)')
    cursor.execute('INSERT INTO UserTB (Patient_First,Patient_Last, Doctor_Last, Doctor,Patient_ID,Day,Time,Corona) VALUES (?,?,?,?,?,?,?,?)',
                   (FirstName, DocName, Time, Date, LastName,PatientID,Doctlast,Corona))
    conn.commit()


window=Tk()
id=StringVar()
las = StringVar()
fn = StringVar()
first = StringVar()
last = StringVar()
day = StringVar()
time = StringVar()
corona=StringVar()
rad_var1 = StringVar()



# def InformationPage():
#     Label(root, text=' Information Page.').pack()

menu = Menu(window)
window.config(menu=menu)
window.geometry("500x500")
sub_menu1 = Menu(menu)
sub_menu2 = Menu(menu)


menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exit1)



label1 = Label(window, text="Patient First Name", font=("arial", 15))
label1.place(x=10, y=10)

entry1 = Entry(window, textvar=fn)
entry1.place(x=190, y=20)

label2 = Label(window, text="Patient Last Name", font=("arial", 15))
label2.place(x=10, y=40)

entry2 = Entry(window, textvar=las)
entry2.place(x=190, y=50)

label3 = Label(window, text="Patient Id", font=("arial", 15))
label3.place(x=10, y=70)

entry3 = Entry(window, textvar=id)
entry3.place(x=190, y=80)

label6 = Label(window, text="date", font=("arial", 15))
label6.place(x=10, y=100)

entry6=Entry(window,textvar=day)
entry6.place(x=190,y=110)


b1 = Button(window, text="Send Order", bg="purple", fg="Black", relief=GROOVE, height=3, width=10, command=database)
window.bind("<Return>", database)
b1.place(x=30, y=160)

window.mainloop()

