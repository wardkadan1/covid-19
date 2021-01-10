import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("C:/Users/WARD/PycharmProjects/pythonProject3/my_data.db")
cursor = conn.cursor()

# cursor.execute("DROP TABLE Schedule")

# cursor.execute('''CREATE TABLE Schedule (
#                 First_name text,
#                 Last_name text,
#                 ID int,
#                 Job text,
#                 Sunday int,
#                 Monday int,
#                 Tuesday int,
#                 Wednesday int,
#                 Thursday int,
#                 Friday int,
#                 Saturday int,
#                 hours int,
#                 overtime_hours int,
#                 patients_treated int,
#                 salary int
#                 )''')

window = tkinter.Tk()
window.geometry("260x300")
window.title("list")
window.resizable(False, False)

entry = tkinter.Entry(window, width=25)
entry.grid(row=0, column=1)
entry1 = tkinter.Entry(window, width=25)
entry1.grid(row=1, column=1)
entry2 = tkinter.Entry(window, width=25)
entry2.grid(row=2, column=1)
entry3 = tkinter.Entry(window, width=25)
entry3.grid(row=3, column=1)
entry4 = tkinter.Entry(window, width=25)
entry4.grid(row=4, column=1)
entry5 = tkinter.Entry(window, width=25)
entry5.grid(row=5, column=1)
entry6 = tkinter.Entry(window, width=25)
entry6.grid(row=6, column=1)
entry7 = tkinter.Entry(window, width=25)
entry7.grid(row=7, column=1)
entry8 = tkinter.Entry(window, width=25)
entry8.grid(row=8, column=1)
entry9 = tkinter.Entry(window, width=25)
entry9.grid(row=9, column=1)
entry10 = tkinter.Entry(window, width=25)
entry10.grid(row=10, column=1)

top = Label(window, text="First_name")
top.grid(row=0, column=0)
top1 = Label(window, text="Last_name")
top1.grid(row=1, column=0)
top2 = Label(window, text="ID")
top2.grid(row=2, column=0)
top3 = Label(window, text="Job")
top3.grid(row=3, column=0)
top4 = Label(window, text="Sunday")
top4.grid(row=4, column=0)
top5 = Label(window, text="Monday")
top5.grid(row=5, column=0)
top6 = Label(window, text="Tuesday")
top6.grid(row=6, column=0)
top7 = Label(window, text="Wednesday")
top7.grid(row=7, column=0)
top8 = Label(window, text="Thursday")
top8.grid(row=8, column=0)
top9 = Label(window, text="Friday")
top9.grid(row=9, column=0)
top10 = Label(window, text="Saturday")
top10.grid(row=10, column=0)


def save_time_of_work():
    val = entry.get().lower().capitalize()
    val1 = entry1.get().lower().capitalize()
    try:
        int(entry2.get())
        val2 = entry2.get()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    windowmessage.config(text="")
    val3 = entry3.get().lower().capitalize()
    val4 = entry4.get().lower().capitalize()
    val5 = entry5.get().lower().capitalize()
    val6 = entry6.get().lower().capitalize()
    val7 = entry7.get().lower().capitalize()
    val8 = entry8.get().lower().capitalize()
    val9 = entry9.get().lower().capitalize()
    val10 = entry10.get().lower().capitalize()
    val11 = 0
    val12 = 0
    val13 = 0
    val14 = 0

    with conn:
        cursor.execute("INSERT INTO Schedule (First_name, Last_name, ID, Job, Sunday, Monday, Tuesday, Wednesday, "
                       "Thursday, Friday, Saturday, hours, overtime_hours, patients_treated, salary) VALUES ("
                       ":First_name, :Last_name, :ID, :Job, :Sunday, :Monday, :Tuesday, "
                       ":Wednesday, :Thursday, :Friday, :Saturday, :hours, :overtime_hours, :patients_treated, :salary)",
                       {'First_name': val, 'Last_name': val1, 'ID': val2, 'Job': val3, 'Sunday': val4, 'Monday': val5,
                        'Tuesday': val6, 'Wednesday': val7, 'Thursday': val8, 'Friday': val9, 'Saturday': val10,
                        'hours': val11, 'overtime_hours': val12, 'patients_treated': val13, 'salary': val14})


def view_all():
    window1 = tkinter.Tk()
    window1.geometry("1370x400")
    window1.title("Schedule list")

    top1 = Label(window1, text="First_name")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last_name")
    top2.grid(row=0, column=1)
    top3 = Label(window1, text="ID")
    top3.grid(row=0, column=2)
    top4 = Label(window1, text="Job")
    top4.grid(row=0, column=3)
    top5 = Label(window1, text="Sunday")
    top5.grid(row=0, column=4)
    top6 = Label(window1, text="Monday")
    top6.grid(row=0, column=5)
    top7 = Label(window1, text="Tuesday")
    top7.grid(row=0, column=6)
    top8 = Label(window1, text="Wednesday")
    top8.grid(row=0, column=7)
    top9 = Label(window1, text="Thursday")
    top9.grid(row=0, column=8)
    top10 = Label(window1, text="Friday")
    top10.grid(row=0, column=9)
    top11 = Label(window1, text="Saturday")
    top11.grid(row=0, column=10)

    r_set = cursor.execute(
        "SELECT First_name, Last_name, ID, Job, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday FROM "
        "Schedule;")
    i = 1  # row value inside the loop
    for Schedule in r_set:
        for j in range(len(Schedule)):
            e = Entry(window1, width=20, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Schedule[j])
            e["state"] = 'readonly'
        i = i + 1

    requested_id = Entry(window1, width=20, fg='blue')
    requested_id.grid(row=i + 1, column=5)
    row_temp = i

    def updateinfo():

        window2 = tkinter.Tk()
        window2.geometry("1370x400")
        window2.title("Info update")

        r = cursor.execute("SELECT ID FROM Schedule;")
        flag = 0
        # print(r.fetchall())
        for row in r.fetchall():
            if requested_id.get() != '':
                if row[0] == int(requested_id.get()):
                    flag = 1

        status = cursor.execute("SELECT sick FROM Schedule WHERE ID=:ID", {'ID': requested_id.get()})
        t=status.fetchone()
        if t == ('Yes',) or flag == 0:
            window2.destroy()
            requested_id.delete(0, "end")
            if t==('Yes',):
                warning = Label(window1, text="This employee\n has Covid!", fg="Red")
                warning.grid(row=row_temp + 2, column=5)
            if flag==0:
                warning = Label(window1, text="Not a valid input!", fg="Red")
                warning.grid(row=row_temp + 2, column=5)

            def after_time():
                warning.config(text="")

            warning.after(3000, after_time)



        else:
            top1 = Label(window2, text="First_name")
            top1.grid(row=0, column=0)
            top2 = Label(window2, text="Last_name")
            top2.grid(row=0, column=1)
            top3 = Label(window2, text="ID")
            top3.grid(row=0, column=2)
            top4 = Label(window2, text="Job")
            top4.grid(row=0, column=3)
            top5 = Label(window2, text="Sunday")
            top5.grid(row=0, column=4)
            top6 = Label(window2, text="Monday")
            top6.grid(row=0, column=5)
            top7 = Label(window2, text="Tuesday")
            top7.grid(row=0, column=6)
            top8 = Label(window2, text="Wednesday")
            top8.grid(row=0, column=7)
            top9 = Label(window2, text="Thursday")
            top9.grid(row=0, column=8)
            top10 = Label(window2, text="Friday")
            top10.grid(row=0, column=9)
            top11 = Label(window2, text="Saturday")
            top11.grid(row=0, column=10)

            r_set = cursor.execute(
                "SELECT First_name, Last_name, ID, Job, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, "
                "Saturday FROM Schedule WHERE ID=:ID ", {'ID': requested_id.get()})

            i = 1  # row value inside the loop
            for Schedule in r_set:
                for j in range(len(Schedule)):
                    e = Entry(window2, width=20, fg='blue')
                    e.grid(row=i, column=j, pady=2)
                    e.insert(END, Schedule[j])
                    e["state"] = 'readonly'
                i = i + 1

            j = 0
            i = i + 1

            top1 = Label(window2, text="First_name")
            top1.grid(row=2, column=0)
            top2 = Label(window2, text="Last_name")
            top2.grid(row=2, column=1)
            top3 = Label(window2, text="ID")
            top3.grid(row=2, column=2)
            top4 = Label(window2, text="Job")
            top4.grid(row=2, column=3)
            top5 = Label(window2, text="Sunday")
            top5.grid(row=2, column=4)
            top6 = Label(window2, text="Monday")
            top6.grid(row=2, column=5)
            top7 = Label(window2, text="Tuesday")
            top7.grid(row=2, column=6)
            top8 = Label(window2, text="Wednesday")
            top8.grid(row=2, column=7)
            top9 = Label(window2, text="Thursday")
            top9.grid(row=2, column=8)
            top10 = Label(window2, text="Friday")
            top10.grid(row=2, column=9)
            top11 = Label(window2, text="Saturday")
            top11.grid(row=2, column=10)

            new1 = Entry(window2, width=20, fg='blue')
            new1.grid(row=i, column=j, pady=2)
            new1.insert(END, Schedule[0])
            new1["state"] = 'readonly'

            new2 = Entry(window2, width=20, fg='blue')
            new2.grid(row=i, column=j + 1, pady=2)
            new2.insert(END, Schedule[1])
            new2["state"] = 'readonly'

            new3 = Entry(window2, width=20, fg='blue')
            new3.grid(row=i, column=j + 2, pady=2)
            new3.insert(END, Schedule[2])
            new3["state"] = 'readonly'

            new4 = Entry(window2, width=20, fg='blue')
            new4.grid(row=i, column=j + 3, pady=2)
            new4.insert(END, Schedule[3])
            new4["state"] = 'readonly'

            new5 = Entry(window2, width=20, fg='blue')
            new5.grid(row=i, column=j + 4, pady=2)

            new6 = Entry(window2, width=20, fg='blue')
            new6.grid(row=i, column=j + 5, pady=2)

            new7 = Entry(window2, width=20, fg='blue')
            new7.grid(row=i, column=j + 6, pady=2)

            new8 = Entry(window2, width=20, fg='blue')
            new8.grid(row=i, column=j + 7, pady=2)

            new9 = Entry(window2, width=20, fg='blue')
            new9.grid(row=i, column=j + 8, pady=2)

            new10 = Entry(window2, width=20, fg='blue')
            new10.grid(row=i, column=j + 9, pady=2)

            new11 = Entry(window2, width=20, fg='blue')
            new11.grid(row=i, column=j + 10, pady=2)

            def updateinfobutton():
                val5 = new5.get().lower().capitalize()
                val6 = new6.get().lower().capitalize()
                val7 = new7.get().lower().capitalize()
                val8 = new8.get().lower().capitalize()
                val9 = new9.get().lower().capitalize()
                val10 = new10.get().lower().capitalize()
                val11 = new11.get().lower().capitalize()
                val3 = new3.get()

                with conn:
                    cursor.execute(
                        """UPDATE Schedule SET Sunday = ?, Monday = ?, Tuesday= ?, Wednesday= ?, Thursday=?,Friday=?,
                        Saturday = ? WHERE ID = ?""",
                        (val5, val6, val7, val8, val9, val10, val11, val3))
                # window1message.config(text="Updated")

                window2.destroy()
                r_set = cursor.execute("SELECT First_name, Last_name, ID, Job, Sunday, Monday, Tuesday, Wednesday, "
                                       "Thursday, Friday,Saturday FROM Schedule WHERE ID=:ID ",
                                       {'ID': requested_id.get()})
                i = 1  # row value inside the loop
                for Schedule in r_set:
                    for j in range(len(Schedule)):
                        e = Entry(window1, width=20, fg='blue')
                        e.grid(row=i, column=j)
                        e.insert(END, Schedule[j])
                        e["state"] = 'readonly'
                    i = i + 1
                requested_id.delete(0, 'end')

            i = i + 1
            Updatebutton = tkinter.Button(window2, text="Update", command=updateinfobutton, width=12, bg='Grey',
                                          fg='white')
            Updatebutton.grid(row=i, column=3)
            exitbutton = tkinter.Button(window2, text="Exit", command=window2.destroy, width=12, bg='Grey', fg='white')
            exitbutton.grid(row=i, column=6)
            i = i + 1

        # window1message.grid(row=i, column=2)

    updatebutton = tkinter.Button(window1, text="Press to update by ID", command=updateinfo, width=16, bg='Grey',
                                  fg='white')
    updatebutton.grid(row=i + 1, column=4)

    exitbutton = tkinter.Button(window1, text="Exit", command=window1.destroy, width=16, bg='Grey', fg='white')
    exitbutton.grid(row=i + 1, column=6)


btn0 = tkinter.Button(window, text="Save Work Time", command=save_time_of_work, width=15, bg='Grey', fg='white', )
btn0.grid(column=1, row=11)

btn0 = tkinter.Button(window, text="view all", command=view_all, width=15, bg='Grey', fg='white', )
btn0.grid(column=1, row=12)

windowmessage = Label(window, text="")
windowmessage.grid(column=1, row=13)

window.mainloop()
conn.close()
