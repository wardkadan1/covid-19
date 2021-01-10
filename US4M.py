import sqlite3
conn = sqlite3.connect('C:/Users/abedh/PycharmProjects/US2M+US5M+US6M/Employee_list.db')
import tkinter as tk
from tkinter import *
import sqlite3
c = conn.cursor()


# c.execute("""CREATE TABLE Schedule (
#     First_name text,
#     Last_name text,
#     ID integer,
#     Job text,
#     test_day text,
#     test_time text,
#     sick text
#     )""")

window = tk.Tk()
window.geometry("300x100")
window.title("")

def viewfull():
    window1 = tk.Tk()
    window1.geometry("780x400")
    window1.title("Employee tests")
    top1 = Label(window1, text="First",width=15)
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Last",width=15)
    top2.grid(row=0, column=1)
    top3 = Label(window1, text="ID",width=15)
    top3.grid(row=0, column=2)
    top4 = Label(window1, text="Job",width=15)
    top4.grid(row=0, column=3)
    top5 = Label(window1, text="Test day",width=15)
    top5.grid(row=0, column=4)
    top6 = Label(window1, text="Test time",width=15)
    top6.grid(row=0, column=5)
    top7 = Label(window1, text="Sick",width=15)
    top7.grid(row=0, column=6)

    r_set = conn.execute("SELECT First_name, Last_name, ID, Job, test_day,test_time,sick FROM Schedule")
    i = 1  # row value inside the loop
    for Schedule in r_set:
        for j in range(len(Schedule)):
            e = Entry(window1, width=18, fg='blue')
            e.grid(row=i, column=j)
            if(Schedule[j]==None):
                e.insert(END,"")
            else:
                e.insert(END, Schedule[j])
            e["state"] = 'readonly'

        i = i + 1

    label = Label(window1, text="", width=15)
    label.grid(row=i+1,column=3)

    def updateinfo():




        requested_id=ID_Entry.get()





        if requested_id==""or requested_id==None:
            label.config(text="Invalid\ninput",width=15,fg="red")
        else:
            try:
                int(requested_id)
                val3 = requested_id
            except ValueError:
                label.config(text="Invalid\ninput", fg="red")
                return 0

            flag=0
            c.execute("SELECT ID FROM Schedule")
            for i in c.fetchall():
                if i[0] == int(val3):
                    flag = 1

            if flag==1:
                window2 = tk.Tk()
                window2.geometry("780x400")
                window2.title("update")
                top1 = Label(window2, text="First", width=15)
                top1.grid(row=0, column=0)
                top2 = Label(window2, text="Last", width=15)
                top2.grid(row=0, column=1)
                top3 = Label(window2, text="ID", width=15)
                top3.grid(row=0, column=2)
                top4 = Label(window2, text="Job", width=15)
                top4.grid(row=0, column=3)
                top5 = Label(window2, text="Test day", width=15)
                top5.grid(row=0, column=4)
                top6 = Label(window2, text="Test time", width=15)
                top6.grid(row=0, column=5)
                top7 = Label(window2, text="Sick", width=15)
                top7.grid(row=0, column=6)

                r_set = conn.execute(
                    "SELECT First_name, Last_name, ID, Job, test_day,test_time,sick FROM Schedule WHERE ID=:ID",
                    {'ID': requested_id})
                i = 1  # row value inside the loop
                for Schedule in r_set:
                    for j in range(len(Schedule)):
                        e = Entry(window2, width=18, fg='blue')
                        e.grid(row=i, column=j, pady=2)
                        if (Schedule[j] == None):
                            e.insert(END, "")
                        else:
                            e.insert(END, Schedule[j])
                        e["state"] = 'readonly'
                    i = i + 1

                j = 0
                i = i + 1

                top1 = Label(window2, text="First", width=15)
                top1.grid(row=2, column=0)
                top2 = Label(window2, text="Last", width=15)
                top2.grid(row=2, column=1)
                top3 = Label(window2, text="ID", width=15)
                top3.grid(row=2, column=2)
                top4 = Label(window2, text="Job", width=15)
                top4.grid(row=2, column=3)
                top5 = Label(window2, text="New date", width=15)
                top5.grid(row=2, column=4)
                top6 = Label(window2, text="New time", width=15)
                top6.grid(row=2, column=5)
                top7 = Label(window2, text="Sick", width=15)
                top7.grid(row=2, column=6)

                new = Entry(window2, width=18, fg='blue')
                new.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                new["state"] = 'readonly'

                new1 = Entry(window2, width=18, fg='blue')
                new1.grid(row=i, column=j + 1, pady=2)
                new1.insert(END, Schedule[1])
                new1["state"] = 'readonly'

                new2 = Entry(window2, width=18, fg='blue')
                new2.grid(row=i, column=j + 2, pady=2)
                new2.insert(END, Schedule[2])
                new2["state"] = 'readonly'

                new3 = Entry(window2, width=18, fg='blue')
                new3.grid(row=i, column=j + 3, pady=2)
                new3.insert(END, Schedule[3])
                new3["state"] = 'readonly'

                new4 = Entry(window2, width=18, fg='blue')
                new4.grid(row=i, column=j + 4, pady=2)

                new5 = Entry(window2, width=18, fg='blue')
                new5.grid(row=i, column=j + 5, pady=2)

                new6 = Entry(window2, width=18, fg='blue')
                new6.grid(row=i, column=j + 6, pady=2)

                x = Schedule[4]
                y = Schedule[5]
                z = Schedule[6]

                def updateinfobutton():
                    val4 = new4.get().lower().capitalize()
                    if val4 == "" or val4 == None:
                        val4 = x
                    val5 = new5.get().lower().capitalize()
                    if val5 == "" or val5 == None:
                        val5 = y
                    val6 = new6.get().lower().capitalize()
                    if val6 == "" or val6 == None:
                        val6 = 6
                    ID = new2.get()
                    with conn:
                        c.execute("""UPDATE Schedule SET test_day = ?, test_time = ?, sick = ? WHERE ID = ?""",
                                  (val4, val5, val6, ID))

                    r_set = conn.execute("SELECT First_name, Last_name, ID, Job, test_day,test_time,sick FROM Schedule")
                    i = 1  # row value inside the loop
                    for Schedule in r_set:
                        for j in range(len(Schedule)):
                            e = Entry(window1, width=18, fg='blue')
                            e.grid(row=i, column=j)
                            if (Schedule[j] == None):
                                e.insert(END, "")
                            else:
                                e.insert(END, Schedule[j])
                            e["state"] = 'readonly'

                        i = i + 1

                    window2.destroy()
                    ID_Entry.delete(0, "end")

                def resetbutton():
                    val4 = ""
                    val5 = ""
                    val6 = "No"
                    ID = new2.get()
                    with conn:
                        c.execute("""UPDATE Schedule SET test_day = ?, test_time = ?, sick = ? WHERE ID = ?""",
                                  (val4, val5, val6, ID))

                    r_set = conn.execute("SELECT First_name, Last_name, ID, Job, test_day,test_time,sick FROM Schedule")
                    i = 1  # row value inside the loop
                    for Schedule in r_set:
                        for j in range(len(Schedule)):
                            e = Entry(window1, width=18, fg='blue')
                            e.grid(row=i, column=j)
                            if (Schedule[j] == None):
                                e.insert(END, "")
                            else:
                                e.insert(END, Schedule[j])
                            e["state"] = 'readonly'

                        i = i + 1

                    window2.destroy()
                    ID_Entry.delete(0, "end")

                i = i + 1
                Resetbutton = tk.Button(window2, text="Reset", command=resetbutton, width=15, bg='Grey', fg='white')
                Resetbutton.grid(row=i, column=1)
                Updatebutton = tk.Button(window2, text="Update", command=updateinfobutton, width=15, bg='Grey',
                                         fg='white')
                Updatebutton.grid(row=i, column=3)
                exitbutton = tk.Button(window2, text="Exit", command=window2.destroy, width=15, bg='Grey', fg='white')
                exitbutton.grid(row=i, column=5)

            elif flag==0:
                label.config(text="Invalid\ninput", fg="red")






    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=15, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)
    updatebutton = tk.Button(window1, text="UPDATE", command=updateinfo, width=15, bg='Grey', fg='white')
    updatebutton.grid(row=i, column=4)
    ID_Entry = Entry(window1, width=18, fg='blue')
    ID_Entry.grid(row=i, column=5)


viewall=tk.Button(window, text="View Schedule", command=viewfull,width=12,bg='Grey', fg="white")
viewall.pack()
window.mainloop()