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

# menu = Menu(window)
# window.config(menu=menu)
# sub_menu1 = Menu(menu)
# sub_menu2 = Menu(menu)

#label0 = Label(window, text="Registration Form", relief="solid", font=("Edwardian Script ITC", 20, "bold")).pack()

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

label4 = Label(window, text="Doctor First Name", font=("arial", 15))
label4.place(x=10, y=105)

entry4 = Entry(window, textvar=first)
entry4.place(x=190, y=114)

label5 = Label(window, text="Doctor Last Name", font=("arial", 15))
label5.place(x=10, y=140)

entry5 = Entry(window, textvar=last)
entry5.place(x=190, y=144)

label6 = Label(window, text="date", font=("arial", 15))
label6.place(x=10, y=170)

entry6=Entry(window,textvar=day)
entry6.place(x=190,y=174)

label7= Label(window,text="time",font=("arial",15))
label7.place(x=10,y=204)

entry7=Entry(window,textvar=time)
entry7.place(x=190,y=210)

label8=Label(window,text="Corana Check",font=("arial",15))
label8.place(x=10,y=235)

entry8=Entry(window,textvar=corona)
entry8.place(x=190,y=240)



# b1 = Button(window, text="Sign Up", bg="silver", fg="Black", relief=GROOVE, height=3, width=10, command=database)
# window.bind("<Return>", database)
# b1.place(x=30, y=270)

window.mainloop()

