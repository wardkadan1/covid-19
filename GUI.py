import tkinter as tk
from tkinter import *
import sqlite3
import Employee_list_Database


#USER STORY 2
#ABED ALHAFEED
#318849866

conn = sqlite3.connect('Employee_list.db')
c = conn.cursor()

window = tk.Tk()
window.geometry("475x400")
window.title("Employees list")
window.resizable(False, False)

label1 = Label(window, text="Current employees list", relief='solid', width=20, font=("aerial", 19, "bold"))
label1.pack(padx=90, pady=30)


def viewfull():
    window1 = tk.Tk()
    window1.geometry("500x400")
    window1.title("yes")
    top1 = Label(window1, text="First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last")
    top2.grid(row=0, column=1)
    top2 = Label(window1, text="ID")
    top2.grid(row=0, column=2)
    top2 = Label(window1, text="Job")
    top2.grid(row=0, column=3)
    top2 = Label(window1, text="Sick")
    top2.grid(row=0, column=4)

    r_set = conn.execute("SELECT * from Employees")
    i = 1  # row value inside the loop
    for Employees in r_set:
        for j in range(len(Employees)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Employees[j])
        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn1 = tk.Button(window, text="View entire list", command=viewfull, width=15, bg='Grey', fg='White')
btn1.pack(pady=3)
entry1 = tk.Entry(window, width=25)
entry1.place(x=300, y=135)


def getfirst():
    window1 = tk.Tk()
    window1.geometry("500x400")
    window1.title("yes")
    top1 = Label(window1, text="First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last")
    top2.grid(row=0, column=1)
    top2 = Label(window1, text="ID")
    top2.grid(row=0, column=2)
    top2 = Label(window1, text="Job")
    top2.grid(row=0, column=3)

    first_name = entry1.get()

    r_set = Employee_list_Database.find_employee_first(first_name)
    i = 1  # row value inside the loop
    for Employees in r_set:
        for j in range(len(Employees)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Employees[j])
        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn2 = tk.Button(window, text="Search by first name", command=getfirst, width=15, bg='Grey', fg='white')
btn2.pack(pady=3)

entry2 = tk.Entry(window, width=25)
entry2.place(x=300, y=165)


def getfinal():
    window1 = tk.Tk()
    window1.geometry("500x400")
    window1.title("yes")
    top1 = Label(window1, text="First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last")
    top2.grid(row=0, column=1)
    top2 = Label(window1, text="ID")
    top2.grid(row=0, column=2)
    top2 = Label(window1, text="Job")
    top2.grid(row=0, column=3)

    final_name = entry2.get()
    r_set = Employee_list_Database.find_employee_last(final_name)
    i = 1  # row value inside the loop
    for Employees in r_set:
        for j in range(len(Employees)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Employees[j])
        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn3 = tk.Button(window, text="Search by last name", command=getfinal, width=15, bg='Grey', fg='white')
btn3.pack(pady=3)

entry3 = tk.Entry(window, width=25)
entry3.place(x=300, y=200)


def getid():
    window1 = tk.Tk()
    window1.geometry("500x400")
    window1.title("yes")
    top1 = Label(window1, text="First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last")
    top2.grid(row=0, column=1)
    top2 = Label(window1, text="ID")
    top2.grid(row=0, column=2)
    top2 = Label(window1, text="Job")
    top2.grid(row=0, column=3)

    id = entry3.get()
    r_set = Employee_list_Database.find_employee_id(id)
    i = 1  # row value inside the loop
    for Employees in r_set:
        for j in range(len(Employees)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Employees[j])
        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn4 = tk.Button(window, text="Search by ID", command=getid, width=15, bg='Grey', fg='white')
btn4.pack(pady=3)

entry4 = tk.Entry(window, width=25)
entry4.place(x=300, y=230)


def getjob():
    window1 = tk.Tk()
    window1.geometry("500x400")
    window1.title("yes")
    top1 = Label(window1, text="First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last")
    top2.grid(row=0, column=1)
    top2 = Label(window1, text="ID")
    top2.grid(row=0, column=2)
    top2 = Label(window1, text="Job")
    top2.grid(row=0, column=3)

    job = entry4.get()
    r_set = Employee_list_Database.find_employee_job(job)
    i = 1  # row value inside the loop
    for Employees in r_set:
        for j in range(len(Employees)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Employees[j])
        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn5 = tk.Button(window, text="Search by job", command=getjob, width=15, bg='Grey', fg='white', )
btn5.pack(pady=3)

window.mainloop()
