import sqlite3
import tkinter
import tkinter.messagebox
import tkinter as tk
from tkinter import *

conn = sqlite3.connect("C:\\Users\\WARD\\PycharmProjects\\pythonProject3\\my_data.db")
cursor = conn.cursor()

root = tkinter.Tk()
root.title("-Time Work-")


def find_work_time():
    listbox_tasks.delete(0, tkinter.END)
    id = get_id()

    Answer = first_name(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'First_name:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = last_name(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Last_name:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = sunday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Sunday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = monday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Monday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = tuesday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Tuesday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = wednesday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Wednesday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = thursday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Thursday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = friday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Friday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")

    Answer = saturday(id)
    x = Answer.fetchone()
    listbox_tasks.insert(tkinter.END, 'Saturday:')
    if x != ('',):
        listbox_tasks.insert(tkinter.END, x)
    else:
        listbox_tasks.insert(tkinter.END, "NO WORK")


def first_name(id):
    return cursor.execute('SELECT First_name FROM Schedule WHERE ID=(?)', (id,))


def last_name(id):
    return cursor.execute('SELECT Last_name FROM Schedule WHERE ID=(?)', (id,))


def sunday(id):
    return cursor.execute('SELECT Sunday FROM Schedule WHERE ID=(?)', (id,))


def monday(id):
    return cursor.execute('SELECT Monday FROM Schedule WHERE ID=(?)', (id,))


def tuesday(id):
    return cursor.execute('SELECT Tuesday FROM Schedule WHERE ID=(?)', (id,))


def wednesday(id):
    return cursor.execute('SELECT Wednesday FROM Schedule WHERE ID=(?)', (id,))


def thursday(id):
    return cursor.execute('SELECT Thursday FROM Schedule WHERE ID=(?)', (id,))


def friday(id):
    return cursor.execute('SELECT Friday FROM Schedule WHERE ID=(?)', (id,))


def saturday(id):
    return cursor.execute('SELECT Saturday FROM Schedule WHERE ID=(?)', (id,))


def _id_(id):
    return cursor.execute('SELECT ID FROM Schedule WHERE ID=(?)', (id,))


def get_id():
    id = entry_task.get().lower().capitalize()
    if id != "":
        return id
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a id.")


def find_patient_time():
    id = entry_task.get()
    r = cursor.execute("SELECT Doctor_ID FROM Patients;")
    if id != "":
        id = int(id)
    flag = 0
    for row in r.fetchall():
        if row[0] == id:
            flag = 1

    if flag == 0 or id == None or id == "":
        listbox_tasks.insert(0, 'Not a valid input')

    elif flag == 1:
        window1 = tk.Tk()
        window1.geometry("1235x300")
        window1.title("Patient list")
        top1 = Label(window1, text="First")
        top1.grid(row=0, column=0)
        top2 = Label(window1, text="Last")
        top2.grid(row=0, column=1)
        top2 = Label(window1, text="ID")
        top2.grid(row=0, column=2)
        top2 = Label(window1, text="Email")
        top2.grid(row=0, column=3)
        top2 = Label(window1, text="Phone")
        top2.grid(row=0, column=4)
        top2 = Label(window1, text="Blood")
        top2.grid(row=0, column=5)
        top2 = Label(window1, text="History")
        top2.grid(row=0, column=6)
        top2 = Label(window1, text="Day")
        top2.grid(row=0, column=7)
        top2 = Label(window1, text="Time")
        top2.grid(row=0, column=8)
        top2 = Label(window1, text="Corona")
        top2.grid(row=0, column=9)
        r_set = view_all(id)
        i = 1  # row value inside the loop
        for Patients in r_set:
            for j in range(len(Patients)):
                e = Entry(window1, width=20, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, Patients[j])
                e["state"] = 'readonly'

            i = i + 1

        spacer1 = Label(window1, text="", width=5).grid(column=2, row=i)
        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=16, bg='Grey', fg='white')
        exitbutton.grid(row=i + 1, column=6)

        requested_id = Entry(window1, width=20, fg='blue')
        requested_id.grid(row=i + 1, column=5)

        row_temp=i

        def updateinfo():
            Patient_ID = requested_id.get()
            r = cursor.execute("SELECT Patient_ID FROM Patients;")
            if Patient_ID != "":
                Patient_ID = int(Patient_ID)
            flag = 0
            for row in r.fetchall():
                if row[0] == Patient_ID:
                    flag = 1

            if flag == 0 or Patient_ID == None or Patient_ID == "":
                warning = Label(window1, text="Not a valid input", fg="Red")
                warning.grid(row=row_temp + 2, column=5)

                def after_time():
                    warning.config(text="")

                warning.after(3000, after_time)


            elif flag == 1:
                window2 = tk.Tk()
                window2.geometry("940x300")
                window2.title("Info update")

                top1 = Label(window2, text="First")
                top1.grid(row=0, column=0)
                top2 = Label(window2, text="Last")
                top2.grid(row=0, column=1)
                top2 = Label(window2, text="ID")
                top2.grid(row=0, column=2)
                top2 = Label(window2, text="Email")
                top2.grid(row=0, column=3)
                top2 = Label(window2, text="Phone")
                top2.grid(row=0, column=4)
                top2 = Label(window2, text="Blood")
                top2.grid(row=0, column=5)
                top2 = Label(window2, text="History")
                top2.grid(row=0, column=6)
                top2 = Label(window2, text="Day")
                top2.grid(row=0, column=7)
                top2 = Label(window2, text="Time")
                top2.grid(row=0, column=8)
                top2 = Label(window2, text="Corona")
                top2.grid(row=0, column=9)

                r_set = conn.execute(
                    "SELECT Patient_First, Patient_Last, Patient_ID, Patient_Email, Patient_Phone, Patient_Blood, "
                    "Patient_History, Day, Time, Corona FROM Patients WHERE Patient_ID=(?) AND Doctor_ID=(?)",
                    (Patient_ID, id))
                i = 1  # row value inside the loop
                for Patients in r_set:
                    for j in range(len(Patients)):
                        e = Entry(window2, width=15, fg='blue')
                        e.grid(row=i, column=j, pady=2)
                        e.insert(END, Patients[j])
                        e["state"] = 'readonly'
                    i = i + 1

                j = 0
                i = i + 1

                top1 = Label(window2, text="New First")
                top1.grid(row=2, column=0)
                top2 = Label(window2, text="New Last")
                top2.grid(row=2, column=1)
                top3 = Label(window2, text="ID")
                top3.grid(row=2, column=2)
                top4 = Label(window2, text="New Email")
                top4.grid(row=2, column=3)
                top5 = Label(window2, text="New Phone")
                top5.grid(row=2, column=4)
                top6 = Label(window2, text="Blood")
                top6.grid(row=2, column=5)
                top7 = Label(window2, text="History")
                top7.grid(row=2, column=6)
                top8 = Label(window2, text="Day")
                top8.grid(row=2, column=7)
                top9 = Label(window2, text="Time")
                top9.grid(row=2, column=8)
                top10 = Label(window2, text="Corona")
                top10.grid(row=2, column=9)

                new1 = Entry(window2, width=15, fg='blue')
                new1.grid(row=i, column=j, pady=2)
                new1.insert(END, Patients[0])
                new1["state"] = 'readonly'

                new2 = Entry(window2, width=15, fg='blue')
                new2.grid(row=i, column=j + 1, pady=2)
                new2.insert(END, Patients[1])
                new2["state"] = 'readonly'

                new3 = Entry(window2, width=15, fg='blue')
                new3.grid(row=i, column=j + 2, pady=2)
                new3.insert(END, Patients[2])
                new3["state"] = 'readonly'

                new4 = Entry(window2, width=15, fg='blue')
                new4.grid(row=i, column=j + 3, pady=2)
                new4.insert(END, Patients[3])
                new4["state"] = 'readonly'

                new5 = Entry(window2, width=15, fg='blue')
                new5.grid(row=i, column=j + 4, pady=2)
                new5.insert(END, Patients[4])
                new5["state"] = 'readonly'

                new6 = Entry(window2, width=15, fg='blue')
                new6.grid(row=i, column=j + 5, pady=2)
                new6.insert(END, Patients[5])
                new6["state"] = 'readonly'

                new7 = Entry(window2, width=15, fg='blue')
                new7.grid(row=i, column=j + 6, pady=2)

                new8 = Entry(window2, width=15, fg='blue')
                new8.grid(row=i, column=j + 7, pady=2)
                new8.insert(END, Patients[7])
                new8["state"] = 'readonly'

                new9 = Entry(window2, width=15, fg='blue')
                new9.grid(row=i, column=j + 8, pady=2)
                new9.insert(END, Patients[8])
                new9["state"] = 'readonly'

                new10 = Entry(window2, width=15, fg='blue')
                new10.grid(row=i, column=j + 9, pady=2)

                def updateinfobutton():
                    val7 = new7.get().lower().capitalize()

                    val10 = new10.get().lower().capitalize()

                    val3 = new3.get().lower().capitalize()

                    with conn:
                        cursor.execute(
                            """UPDATE Patients SET Patient_History = ?, Corona = ? WHERE Patient_ID = ?""",
                            (val7, val10, val3))

                    window2.destroy()
                    r_set = view_all(id)
                    i = 1  # row value inside the loop
                    for Patients in r_set:
                        for j in range(len(Patients)):
                            e = Entry(window1, width=20, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, Patients[j])
                            e["state"] = 'readonly'
                        i = i + 1
                    requested_id.delete(0, 'end')

                i = i + 1
                Updatebutton = tk.Button(window2, text="Update", command=updateinfobutton, width=12, bg='Grey',
                                         fg='white')
                Updatebutton.grid(row=i, column=3)
                exitbutton = tk.Button(window2, text="Exit", command=window2.destroy, width=12, bg='Grey', fg='white')
                exitbutton.grid(row=i, column=6)
                i = i + 1
        updatebutton = tk.Button(window1, text="Press to update by ID", command=updateinfo, width=16, bg='Grey',
                                 fg='white')
        updatebutton.grid(row=i + 1, column=4)

        def deletebutton():
            Patient_ID = requested_id.get()
            with conn:
                cursor.execute("DELETE from Patients WHERE Patient_ID = :Patient_ID", {'Patient_ID': Patient_ID})
            r_set = view_all(id)
            i = 1  # row value inside the loop
            for Patients in r_set:
                for j in range(len(Patients)):
                    e = Entry(window1, width=20, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, Patients[j])
                    e["state"] = 'readonly'
                # use insert to delete valuse (add space)
                i = i + 1

        delete_button = tk.Button(window1, text="Press to delete by id", command=deletebutton, width=16, bg='Grey',
                                  fg='white')
        delete_button.grid(row=i + 1, column=3)


def view_all(Doctor_ID):
    return cursor.execute(
        "SELECT Patient_First, Patient_Last, Patient_ID, Patient_Email, Patient_Phone, Patient_Blood, "
        "Patient_History, Day, Time, Corona FROM Patients WHERE Doctor_ID=:Doctor_ID", {'Doctor_ID': Doctor_ID})


def salary():
    id = entry_task.get()
    r = cursor.execute("SELECT ID FROM Schedule;")
    if id != "":
        id = int(id)
    flag = 0
    for row in r.fetchall():
        if row[0] == id:
            flag = 1

    if flag == 0 or id == None or id == "":
        listbox_tasks.insert(0, 'Not a valid input')

    elif flag == 1:
        window1 = tkinter.Tk()
        window1.geometry("850x200")
        window1.title("update salary")
        top1 = Label(window1, text="Doctor_First")
        top1.grid(row=0, column=0)
        top2 = Label(window1, text="Doctor_Last")
        top2.grid(row=0, column=1)
        top3 = Label(window1, text="Doctor_ID")
        top3.grid(row=0, column=2)
        top4 = Label(window1, text="Job")
        top4.grid(row=0, column=3)
        top5 = Label(window1, text="hours")
        top5.grid(row=0, column=4)
        top6 = Label(window1, text="overtime_hours")
        top6.grid(row=0, column=5)
        top7 = Label(window1, text="patients_treated")
        top7.grid(row=0, column=6)
        top8 = Label(window1, text="salary")
        top8.grid(row=0, column=7)
        r_set = conn.execute(
            "SELECT First_name, Last_name, ID, Job, hours, overtime_hours,patients_treated,salary FROM Schedule WHERE "
            "ID=:ID", {'ID': id})
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=17, fg='blue')
                e.grid(row=i, column=j, pady=2)
                e.insert(END, Schedule[j])
                e["state"] = 'readonly'
            i = i + 1
        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=14, bg='Grey', fg='white')
        exitbutton.grid(row=i + 1, column=3)

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=70)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_find_work_time = tkinter.Button(root, text="search", width=48, command=find_work_time)
button_find_work_time.pack()

button_find_patient_time = tkinter.Button(root, text="search_patient", width=48, command=find_patient_time)
button_find_patient_time.pack()

button_find_salary = tkinter.Button(root, text="show salary", width=48, command=salary)
button_find_salary.pack()

exit_button = tkinter.Button(root, text="Exit", width=48, command=quit)
exit_button.pack()

root.mainloop()
conn.commit()
conn.close()
