import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("my_data.db")
cursor = conn.cursor()

# cursor.execute("DROP TABLE Patients")

# cursor.execute('''CREATE TABLE Patients (
#                 Doctor text,
#                 Doctor_Last text,
#                 Doctor_ID int,
#                 Patient_First text,
#                 Patient_Last text,
#                 Patient_ID int,
#                 Patient_Email text,
#                 Patient_Phone int,
#                 Patient_Blood text,
#                 Patient_History text,
#                 Day text,
#                 Time int,
#                 Corona text,
#                 Method text
#                 )''')

window = tkinter.Tk()
window.geometry("300x420")
window.title("list")
window.resizable(False, False)

lable = Label(window, text="Doctor's first name")
lable.grid(column=0, row=0)
lable1 = Label(window, text="Doctor's last name")
lable1.grid(column=0, row=1)
lable2 = Label(window, text="Doctor's id")
lable2.grid(column=0, row=2)
lable3 = Label(window, text="Patient's first name")
lable3.grid(column=0, row=3)
lable4 = Label(window, text="Patient's last name")
lable4.grid(column=0, row=4)
lable5 = Label(window, text="Patient's ID")
lable5.grid(column=0, row=5)
lable6 = Label(window, text="Patient's Email")
lable6.grid(column=0, row=6)
lable7 = Label(window, text="Patient's Phone")
lable7.grid(column=0, row=7)
lable8 = Label(window, text="Patient's Blood")
lable8.grid(column=0, row=8)
lable9 = Label(window, text="Patient's History")
lable9.grid(column=0, row=9)
lable10 = Label(window, text="Day")
lable10.grid(column=0, row=10)
lable11 = Label(window, text="Time")
lable11.grid(column=0, row=11)
lable12 = Label(window, text="Corona")
lable12.grid(column=0, row=12)
lable12 = Label(window, text="Method")
lable12.grid(column=0, row=13)


def save_time_of_work_of_Patients():
    window1 = tkinter.Tk()
    window1.geometry("1310x400")
    window1.title("yes")
    top1 = Label(window1, text="Doctor_First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Doctor_Last")
    top2.grid(row=0, column=1)
    top3 = Label(window1, text="Doctor_ID")
    top3.grid(row=0, column=2)
    top4 = Label(window1, text="Patient_First")
    top4.grid(row=0, column=3)
    top5 = Label(window1, text="Patient_Last")
    top5.grid(row=0, column=4)
    top6 = Label(window1, text="Patient_ID")
    top6.grid(row=0, column=5)
    top7 = Label(window1, text="Patient_Email")
    top7.grid(row=0, column=6)
    top8 = Label(window1, text="Patient_Phone")
    top8.grid(row=0, column=7)
    top9 = Label(window1, text="Patient_Blood")
    top9.grid(row=0, column=8)
    top10 = Label(window1, text="Patient_History")
    top10.grid(row=0, column=9)
    top11 = Label(window1, text="Day")
    top11.grid(row=0, column=10)
    top12 = Label(window1, text="Time")
    top12.grid(row=0, column=11)
    top13 = Label(window1, text="Corona")
    top13.grid(row=0, column=12)
    top14 = Label(window1, text="Method")
    top14.grid(row=0, column=13)

    r_set = conn.execute("SELECT * from Patients")
    i = 1  # row value inside the loop
    for Patients in r_set:
        for j in range(len(Patients)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Patients[j])
            e["state"] = 'readonly'

        i = i + 1

    exitbutton = tkinter.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=6)


def add_Patients():
    val = entry.get().lower().capitalize()
    val1 = entry1.get().lower().capitalize()
    val2 = entry2.get().lower().capitalize()
    val3 = entry3.get().lower().capitalize()
    val4 = entry4.get().lower().capitalize()
    try:
        int(entry5.get())
        val5 = entry5.get()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    windowmessage.config(text="")
    val6 = entry6.get().lower().capitalize()
    try:
        str(entry7.get())
        val7 = entry7.get().lower().capitalize()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    val8 = entry8.get().lower().capitalize()
    val9 = entry9.get().lower().capitalize()
    val10 = entry10.get().lower().capitalize()
    try:
        int(entry11.get())
        val11 = entry11.get().lower().capitalize()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    val12 = entry12.get().lower().capitalize()
    val13=entry13.get().lower().capitalize()
    with conn:
        cursor.execute("INSERT INTO Patients VALUES (:Doctor, :Doctor_Last, :Doctor_ID, :Patient_First, :Patient_Last, "
                       ":Patient_ID, :Patient_Email, :Patient_Phone, :Patient_Blood, :Patient_History, :Day, :Time, "
                       ":Corona, :Method) "
                       ,
                       {'Doctor': val, 'Doctor_Last': val1, 'Doctor_ID': val2, 'Patient_First': val3,
                        'Patient_Last': val4,
                        'Patient_ID': val5, 'Patient_Email': val6, 'Patient_Phone': val7, 'Patient_Blood': val8,
                        'Patient_History': val9, 'Day': val10, 'Time': val11, 'Corona': val12, 'Method': val13})


entry = tkinter.Entry(window, width=25, fg='blue')
entry.grid(column=1, row=0, pady=2)
entry1 = tkinter.Entry(window, width=25, fg='blue')
entry1.grid(column=1, row=1, pady=2)
entry2 = tkinter.Entry(window, width=25, fg='blue')
entry2.grid(row=2, column=1, pady=2)
entry3 = tkinter.Entry(window, width=25, fg='blue')
entry3.grid(row=3, column=1, pady=2)
entry4 = tkinter.Entry(window, width=25, fg='blue')
entry4.grid(row=4, column=1, pady=2)
entry5 = tkinter.Entry(window, width=25, fg='blue')
entry5.grid(row=5, column=1, pady=2)
entry6 = tkinter.Entry(window, width=25, fg='blue')
entry6.grid(row=6, column=1, pady=2)
entry7 = tkinter.Entry(window, width=25, fg='blue')
entry7.grid(row=7, column=1, pady=2)
entry8 = tkinter.Entry(window, width=25, fg='blue')
entry8.grid(row=8, column=1, pady=2)
entry9 = tkinter.Entry(window, width=25, fg='blue')
entry9.grid(row=9, column=1, pady=2)
entry10 = tkinter.Entry(window, width=25, fg='blue')
entry10.grid(row=10, column=1, pady=2)
entry11 = tkinter.Entry(window, width=25, fg='blue')
entry11.grid(row=11, column=1, pady=2)
entry12 = tkinter.Entry(window, width=25, fg='blue')
entry12.grid(row=12, column=1, pady=2)
entry13 = tkinter.Entry(window, width=25, fg='blue')
entry13.grid(row=13, column=1, pady=2)

btn2 = tkinter.Button(window, text="add", command=add_Patients, width=15, bg='Grey', fg='white')
btn2.grid(column=1, row=14)

entry12 = tkinter.Entry(window, width=25, fg='blue')
entry12.grid(row=12, column=1, pady=2)

btn1 = tkinter.Button(window, text="View Patients list", command=save_time_of_work_of_Patients, width=15, bg='Grey',
                      fg='White')
btn1.grid(column=1, row=15)

exitbutton = tkinter.Button(window, text="EXIT", command=window.destroy, width=15, bg='Grey', fg='white')
exitbutton.grid(row=16, column=1)

windowmessage=Label(window, text="")
windowmessage.grid(column=1, row=17,pady=3)

window.mainloop()
conn.close()
