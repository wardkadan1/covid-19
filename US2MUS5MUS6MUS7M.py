import sqlite3

conn = sqlite3.connect('Employee_list.db')
import tkinter as tk
from tkinter import *
import sqlite3

c = conn.cursor()


# ABED ALHAFEED
# 318849866


def add_employee():
    val1 = entry1.get().lower().capitalize()
    a = c.execute("SELECT ID FROM Schedule")
    val2 = entry2.get().lower().capitalize()
    val3 = entry3.get()
    val4 = entry4.get().lower().capitalize()
    val5 = "No"
    val6=0
    temp = ""

    flag=0
    for i in a.fetchall():
        if (val3!="" and val3!=None):
            if i[0] == val3:
                flag = 1

    if (flag==1) or (val1=="" or val1==None) or (val2=="" or val2==None) or (val3=="" or val3==None) or (val4=="" or val4==None):
        windowmessage.config(text="invalid input", fg="red")

    else:
        try:
            int(entry3.get())
            val3 = entry3.get()
        except ValueError:
            windowmessage.config(text="Not a valid input", fg="red")
            return 0
        with conn:
            c.execute(
                "INSERT INTO Schedule (First_name, Last_name, ID, Job, test_day, test_time, sick, trainee1_id, trainee2_id, trainee3_id) VALUES (:First_name, :Last_name, :ID, :Job, :test_day, :test_time, :sick, :trainee1_id, :trainee2_id, :trainee3_id)",
                {'First_name': val1, 'Last_name': val2, 'ID': val3, 'Job': val4, 'test_day': temp, 'test_time':temp ,'sick': val5, 'trainee1_id': temp, 'trainee2_id':temp, 'trainee3_id': temp})

        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)

        windowmessage.config(text="Added")



def remove_emp():
    val1 = entry1.get().lower().capitalize()
    if val1=="" or val1==None:
        windowmessage.config(text="Not a valid input", fg="red")
        flag=1
    val2 = entry2.get().lower().capitalize()
    if val2 == "" or val2 == None:
        windowmessage.config(text="Not a valid input", fg="red")
        flag = 1
    val3 = entry3.get()
    if val3 == "" or val2 == None:
        windowmessage.config(text="Not a valid input", fg="red")
        flag = 1
    val4 = entry4.get().lower().capitalize()
    if val4 == "" or val4 == None:
        windowmessage.config(text="Not a valid input", fg="red")
        flag = 1

    if flag!=1:
        try:
            int(entry3.get())
            val3 = entry3.get()
        except ValueError:
            windowmessage.config(text="Not a valid input", fg="red")
            return 0
        with conn:
            c.execute("DELETE from Schedule WHERE ID = :ID",
                      {'ID': val3})
        windowmessage.config(text="Deleted")

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)


def updateinfo():
    val1 = entry1.get().lower().capitalize()
    a = c.execute("SELECT ID FROM Schedule")
    val2 = entry2.get().lower().capitalize()
    val3 = entry3.get()
    val4 = entry4.get().lower().capitalize()
    val5 = "No"
    val6 = 0

    flag = 0
    for i in a.fetchall():
        if (val3 != "" and val3 != None):
            if i[0] == val3:
                flag = 1

    if (flag == 1) or (val1 == "" or val1 == None) or (val2 == "" or val2 == None) or (val3 == "" or val3 == None) or (
            val4 == "" or val4 == None):
        windowmessage.config(text="invalid input", fg="red")
    else:
        try:
            int(entry3.get())
            val3 = entry3.get()
        except ValueError:
            windowmessage.config(text="Not a valid input", fg="red")
            return 0

        window1 = tk.Tk()
        window1.geometry("500x400")
        window1.title("yes")

        top1 = Label(window1, text="First")
        top1.grid(row=0, column=0)
        top2 = Label(window1, text="Last")
        top2.grid(row=0, column=1)
        top3 = Label(window1, text="ID")
        top3.grid(row=0, column=2)
        top4 = Label(window1, text="Job")
        top4.grid(row=0, column=3)
        top5 = Label(window1, text="Sick")
        top5.grid(row=0, column=4)

        r_set = conn.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE ID=:ID", {'ID': val3})
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=15, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'
            i = i + 1

        j = 0
        i = i + 1

        top1 = Label(window1, text="New First_name")
        top1.grid(row=2, column=0)
        top2 = Label(window1, text="New Last_name")
        top2.grid(row=2, column=1)
        top3 = Label(window1, text="ID")
        top3.grid(row=2, column=2)
        top4 = Label(window1, text="New Job")
        top4.grid(row=2, column=3)
        top5 = Label(window1, text="Sick (Yes/No)")
        top5.grid(row=2, column=4)

        new1 = Entry(window1, width=15, fg='blue')
        new1.grid(row=i, column=j, pady=2)
        new2 = Entry(window1, width=15, fg='blue')
        new2.grid(row=i, column=j + 1, pady=2)
        new3 = Entry(window1, width=15, fg='blue')
        new3.grid(row=i, column=j + 2, pady=2)

        if (Schedule[2] == None):
            new3.insert(END, "")
        else:
            new3.insert(END, Schedule[2])
        new3["state"] = 'readonly'
        new4 = Entry(window1, width=15, fg='blue')
        new4.grid(row=i, column=j + 3, pady=2)
        new5 = Entry(window1, width=15, fg='blue')
        new5.grid(row=i, column=j + 4, pady=2)

        def updateinfobutton():
            val1 = new1.get().lower().capitalize()
            if val1 == "" or val1 == None:
                val1 = Schedule[0]
            val2 = new2.get().lower().capitalize()
            if val2 == "" or val2 == None:
                val2 = Schedule[1]
            val3 = new3.get()
            val4 = new4.get().lower().capitalize()
            if val4 == "" or val4 == None:
                val4 = Schedule[3]
            val5 = new5.get().lower().capitalize()
            if val5 == "" or val5 == None:
                val5 = Schedule[4]

            with conn:
                c.execute("""UPDATE Schedule SET First_name = ?, Last_name = ?, Job = ?, sick = ? WHERE ID = ?""",
                          (val1, val2, val4, val5, val3))
            window1.destroy()

        i = i + 1
        Updatebutton = tk.Button(window1, text="Update", command=updateinfobutton, width=12, bg='Grey', fg='white')
        Updatebutton.grid(row=i, column=1)
        exitbutton = tk.Button(window1, text="Exit", command=window1.destroy, width=12, bg='Grey', fg='white')
        exitbutton.grid(row=i, column=3)
        i = i + 1




def find_employee_first(first):
    return c.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE First_name=:First_name", {'First_name': first})
    # var2= c.fetchall()
    # print(var2)


def find_employee_last(last):
    return c.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE Last_name=:Last_name", {'Last_name': last})
    # var3= c.fetchall()
    # print(var3)


def find_employee_id(id):
    return c.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE ID=:ID", {'ID': id})
    # var4= c.fetchall()
    # print(var4)


def find_employee_job(job):
    return c.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE Job=:Job", {'Job': job})
    # var5= c.fetchall()
    # print(var5)


def find_employee_sick(sick):
    return c.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule WHERE sick=:sick", {'sick': sick})


conn = sqlite3.connect('Employee_list.db')
c = conn.cursor()

window = tk.Tk()
window.geometry("475x500")
window.title("Schedule list")
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

    r_set = conn.execute("SELECT First_name, Last_name, ID, Job, sick FROM Schedule")
    i = 1  # row value inside the loop
    for Schedule in r_set:
        for j in range(len(Schedule)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            if (Schedule[j] == None):
                e.insert(END, "")
            else:
                e.insert(END, Schedule[j])
            e["state"] = 'readonly'

        i = i + 1

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


btn1 = tk.Button(window, text="View entire list", command=viewfull, width=15, bg='Grey', fg='White')
btn1.pack(pady=3)
entry1 = tk.Entry(window, width=25)
entry1.place(x=300, y=135)


def getfirst():

    first_name = entry1.get().lower().capitalize()

    if first_name=="" or first_name==None:
        windowmessage.config(text="invalid input", fg="red")
    else:
        window1 = tk.Tk()
        window1.geometry("500x400")
        window1.title("")
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
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        r_set = find_employee_first(first_name)
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=15, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'

            i = i + 1

        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
        exitbutton.grid(row=i, column=2)


btn2 = tk.Button(window, text="Search by First name", command=getfirst, width=15, bg='Grey', fg='white')
btn2.pack(pady=3)

entry2 = tk.Entry(window, width=25)
entry2.place(x=300, y=165)


def getfinal():


    final_name = entry2.get().lower().capitalize()
    if final_name=="" or final_name==None:
        windowmessage.config(text="invalid input", fg="red")
    else:
        window1 = tk.Tk()
        window1.geometry("500x400")
        window1.title("")
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
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        r_set = find_employee_last(final_name)
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=15, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'

            i = i + 1

        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
        exitbutton.grid(row=i, column=2)


btn3 = tk.Button(window, text="Search by Last name", command=getfinal, width=15, bg='Grey', fg='white')
btn3.pack(pady=3)

entry3 = tk.Entry(window, width=25)
entry3.place(x=300, y=200)


def getid():




    id = entry3.get().lower().capitalize()


    try:
        int(entry3.get())
        val3 = entry3.get()
    except ValueError:
        windowmessage.config(text="Invalid\ninput", fg="red")
        return 0
    flag=0
    c=conn.execute("SELECT ID FROM Schedule")
    if id != "":
        id = int(id)
    for i in c.fetchall():

        if (id != "" or id != None):
            if i[0] == id:
                flag = 1

    if id == "" or id == None or flag == 0:
        windowmessage.config(text="Invalid\ninput", fg="red")

    else:
        window1 = tk.Tk()
        window1.geometry("500x400")
        window1.title("")
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
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        r_set = find_employee_id(id)
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=15, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'
            i = i + 1

        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
        exitbutton.grid(row=i, column=2)


btn4 = tk.Button(window, text="Search by ID", command=getid, width=15, bg='Grey', fg='white')
btn4.pack(pady=3)

entry4 = tk.Entry(window, width=25)
entry4.place(x=300, y=230)


def getjob():

    job = entry4.get().lower().capitalize()

    if job=="" or job==None:
        windowmessage.config(text="Not a valid input", fg="red")
    else:
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

        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0, END)
        r_set = find_employee_job(job)
        i = 1  # row value inside the loop
        for Schedule in r_set:
            for j in range(len(Schedule)):
                e = Entry(window1, width=15, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'
            i = i + 1

        exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
        exitbutton.grid(row=i, column=2)



def create_teams():



    window1 = tk.Tk()
    window1.geometry("300x400")
    window1.title("Create Teams")
    top1 = Label(window1, text="Doctor's First")
    top1.grid(row=0, column=0)
    top2 = Label(window1, text="Doctor's Last")
    top2.grid(row=0, column=1)
    top3 = Label(window1, text="Doctor's ID")
    top3.grid(row=0, column=2)


    r_set = conn.execute("SELECT First_name, Last_name, ID FROM Schedule WHERE Job = ?", ("Doctor",))  # gets only doctors
    i = 1  # row value inside the loop
    for Schedule in r_set:
        for j in range(len(Schedule)):
            e = Entry(window1, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            if (Schedule[j] == None):
                e.insert(END, "")
            else:
                e.insert(END, Schedule[j])
            e["state"] = 'readonly'
        i = i + 1

    Doc_id = Entry(window1, width=16, fg='blue')
    Doc_id.grid(row=i, column=1)

    L=Label(window1,text="",fg="red")
    L.grid(row=i+1,column=1)



    def updateteams():
        id = Doc_id.get()

        try:
            int(Doc_id.get())
            id = Doc_id.get()
        except ValueError:
            L.config(text="Invalid\ninput")
            return 0


        flag = 0
        a = conn.execute("SELECT ID FROM Schedule WHERE Job = ?", ("Doctor",))

        if id != "":
            id = int(id)


        for i in a.fetchall():

            if (id != "" or id != None):
                if i[0] == id:
                    flag = 1



        if id=="" or id == None or flag == 0:
            L.config(text="Invalid\ninput")

        else:
            window2 = tk.Tk()
            window2.geometry("900x400")
            window2.title("Create Teams")
            top1 = Label(window2, text="Doctor's First")
            top1.grid(row=0, column=0)
            top2 = Label(window2, text="Doctor's ID")
            top2.grid(row=0, column=1)
            top3 = Label(window2, text="1st Trainee's First")
            top3.grid(row=0, column=2)
            top4 = Label(window2, text="1st Trainee's ID")
            top4.grid(row=0, column=3)
            top5 = Label(window2, text="2nd Trainee's First")
            top5.grid(row=0, column=4)
            top6 = Label(window2, text="2nd Trainee's ID")
            top6.grid(row=0, column=5)
            top7 = Label(window2, text="3rd Trainee's First")
            top7.grid(row=0, column=6)
            top8 = Label(window2, text="3rd Trainee's ID")
            top8.grid(row=0, column=7)

            doc_row = c.execute(
                "SELECT First_name, ID, trainee1_ID, trainee2_ID, trainee3_ID FROM Schedule WHERE ID=:ID",
                {'ID': id})

            i = 1  # row value inside the loop
            for Schedule in doc_row:
                for j in range(len(Schedule)):
                    if (j < 2):
                        e = Entry(window2, width=16, fg='blue')
                        e.grid(row=1, column=j, pady=2)
                        if (Schedule[j] == None):
                            e.insert(END, "")

                        else:
                            e.insert(END, Schedule[j])
                            e["state"] = 'readonly'

                i = i + 1

            trainee1_id = Schedule[2]
            trainee2_id = Schedule[3]
            trainee3_id = Schedule[4]

            if (trainee1_id == "" or trainee1_id == None):
                e1 = Entry(window2, width=16, fg='blue')
                e1.grid(row=1, column=2, pady=2)
                e1["state"] = 'readonly'
                e2 = Entry(window2, width=16, fg='blue')
                e2.grid(row=1, column=3, pady=2)
                e2["state"] = 'readonly'

            else:
                trainee1 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=:ID AND ID=:ID",
                                        {'ID': id, 'ID': trainee1_id})
                i = 1  # row value inside the loop
                for Employees1 in trainee1:
                    for j in range(len(Employees1)):
                        e = Entry(window2, width=16, fg='blue')
                        e.grid(row=1, column=j + 2, pady=2)
                        e.insert(END, Employees1[j])
                        e["state"] = 'readonly'
                    i = i + 1

            if (trainee2_id == "" or trainee2_id == None):
                e1 = Entry(window2, width=16, fg='blue')
                e1.grid(row=1, column=4, pady=2)
                e1["state"] = 'readonly'
                e2 = Entry(window2, width=16, fg='blue')
                e2.grid(row=1, column=5, pady=2)
                e2["state"] = 'readonly'
            else:
                trainee2 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=:ID AND ID=:ID",
                                        {'ID': id, 'ID': trainee2_id})
                i = 1  # row value inside the loop
                for Employees2 in trainee2:
                    for j in range(len(Employees2)):
                        e = Entry(window2, width=16, fg='blue')
                        e.grid(row=1, column=j + 4, pady=2)
                        e.insert(END, Employees2[j])
                        e["state"] = 'readonly'
                    i = i + 1

            if (trainee3_id == "" or trainee3_id == None):
                e1 = Entry(window2, width=16, fg='blue')
                e1.grid(row=1, column=6, pady=2)
                e1["state"] = 'readonly'
                e2 = Entry(window2, width=16, fg='blue')
                e2.grid(row=1, column=7, pady=2)
                e2["state"] = 'readonly'
            else:
                trainee3 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=:ID AND ID=:ID",
                                        {'ID': id, 'ID': trainee3_id})
                i = 1  # row value inside the loop
                for Employees3 in trainee3:
                    for j in range(len(Employees3)):
                        e = Entry(window2, width=16, fg='blue')
                        e.grid(row=1, column=j + 6, pady=2)
                        e.insert(END, Employees3[j])
                        e["state"] = 'readonly'
                    i = i + 1

            top1 = Label(window2, text="Doctor's First")
            top1.grid(row=2, column=0)
            top2 = Label(window2, text="Doctor's ID")
            top2.grid(row=2, column=1)
            top3 = Label(window2, text="1st Trainee's First")
            top3.grid(row=2, column=2)
            top4 = Label(window2, text="1st Trainee's ID")
            top4.grid(row=2, column=3)
            top5 = Label(window2, text="2nd Trainee's First")
            top5.grid(row=2, column=4)
            top6 = Label(window2, text="2nd Trainee's ID")
            top6.grid(row=2, column=5)
            top7 = Label(window2, text="3rd Trainee's First")
            top7.grid(row=2, column=6)
            top8 = Label(window2, text="3rd Trainee's ID")
            top8.grid(row=2, column=7)

            e1 = Entry(window2, width=16, fg='blue')
            e1.grid(row=3, column=0, pady=2)
            e1.insert(END, Schedule[0])
            e1["state"] = 'readonly'
            e2 = Entry(window2, width=16, fg='blue')
            e2.grid(row=3, column=1, pady=2)
            e2.insert(END, Schedule[1])
            e2["state"] = 'readonly'
            e3 = Entry(window2, width=16, fg='blue')
            e3.grid(row=3, column=2, pady=2)
            e3["state"] = 'disabled'
            e4 = Entry(window2, width=16, fg='blue')
            e4.grid(row=3, column=3, pady=2)
            e5 = Entry(window2, width=16, fg='blue')
            e5.grid(row=3, column=4, pady=2)
            e5["state"] = 'disabled'
            e6 = Entry(window2, width=16, fg='blue')
            e6.grid(row=3, column=5, pady=2)
            e7 = Entry(window2, width=16, fg='blue')
            e7.grid(row=3, column=6, pady=2)
            e7["state"] = 'disabled'
            e8 = Entry(window2, width=16, fg='blue')
            e8.grid(row=3, column=7, pady=2)

            def update_button():
                id1 = e4.get().lower().capitalize()
                if id1 == "" or id1 == None:
                    id1 = trainee1_id
                id2 = e6.get().lower().capitalize()
                if id2 == "" or id2 == None:
                    id2 = trainee2_id
                id3 = e8.get().lower().capitalize()
                if id3 == "" or id2 == None:
                    id3 = trainee3_id

                with conn:
                    c.execute(
                        """UPDATE Schedule SET trainee1_ID = ?, trainee2_ID = ?, trainee3_ID=? WHERE ID = ?""",
                        (id1, id2, id3, id))

                window2.destroy()

            def reset_button():
                id1 = 0
                id2 = 0
                id3 = 0

                with conn:
                    c.execute(
                        """UPDATE Schedule SET trainee1_ID = ?, trainee2_ID = ?, trainee3_ID=? WHERE ID = ?""",
                        (id1, id2, id3, id))

                window2.destroy()

            i = i + 1

            reset_Button = tk.Button(window2, text="Reset", command=reset_button, width=12, bg="grey", fg="white")
            reset_Button.grid(row=i + 1, column=2)

            Updatebutton = tk.Button(window2, text="Update", command=update_button, width=12, bg='Grey', fg='white')
            Updatebutton.grid(row=i + 1, column=3)

            exitbutton = tk.Button(window2, text="EXIT", command=window2.destroy, width=12, bg='Grey', fg='white')
            exitbutton.grid(row=i + 1, column=4)

    Updatebutton = tk.Button(window1, text="Update by ID", command=updateteams, width=12, bg='grey', fg='white')
    Updatebutton.grid(row=i, column=0)

    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=2)


def get_teams():
    window1 = tk.Tk()
    window1.geometry("900x400")
    window1.title("View Teams")
    top1 = Label(window1, text="Doc's First")
    top1.grid(row=0, column=0)

    top3 = Label(window1, text="Doc's ID")
    top3.grid(row=0, column=1)

    top5 = Label(window1, text="Trainee 1")
    top5.grid(row=0, column=2)
    top6 = Label(window1, text="Trainee 1 ID")
    top6.grid(row=0, column=3)
    top7 = Label(window1, text="Trainee 2")
    top7.grid(row=0, column=4)
    top8 = Label(window1, text="Trainee 2 ID")
    top8.grid(row=0, column=5)
    top9 = Label(window1, text="Trainee 3")
    top9.grid(row=0, column=6)
    top10 = Label(window1, text="Trainee 3 ID")
    top10.grid(row=0, column=7)

    doc_row = conn.execute(
        "SELECT First_name, ID,trainee1_ID, trainee2_ID, trainee3_ID FROM Schedule WHERE trainee1_ID!=? AND trainee2_ID!=? AND trainee3_ID!=? AND Job=?",
        ("","","", "Doctor",))
    i = 1  # row value inside the loop
    for Schedule in doc_row:
        for j in range(len(Schedule)):
            id1 = Schedule[2]
            id2 = Schedule[3]
            id3 = Schedule[4]
            if j < 2:
                e = Entry(window1, width=16, fg='blue')
                e.grid(row=i, column=j, pady=2)
                if (Schedule[j] == None):
                    e.insert(END, "")
                else:
                    e.insert(END, Schedule[j])
                e["state"] = 'readonly'
            if j == 2:
                e1 = Entry(window1,text="", width=16, fg='blue')
                e1.grid(row=i, column=2, pady=2)
                e2 = Entry(window1,text="", width=16, fg='blue')
                e2.grid(row=i, column=3, pady=2)

                if (Schedule[2] == "" or Schedule[2] == None):
                    e1["state"] = 'readonly'
                    e2["state"] = 'readonly'

                else:
                    trainee1 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=?", (id1,))
                    x=trainee1.fetchall()
                    e1.insert(END, x[0][0])
                    e2.insert(END, x[0][1])
                    e1["state"] = 'readonly'
                    e2["state"] = 'readonly'

            if j == 3:
                e3 = Entry(window1, width=16, fg='blue')
                e3.grid(row=i, column=4, pady=2)
                e4 = Entry(window1, width=16, fg='blue')
                e4.grid(row=i, column=5, pady=2)
                if (Schedule[3] == "" or Schedule[3] == None):
                    e3["state"] = 'readonly'
                    e4["state"] = 'readonly'

                else:
                    trainee2 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=?", (id2,))
                    y=trainee2.fetchall()
                    e3.insert(END, y[0][0])
                    e4.insert(END, y[0][1])
                    e3["state"] = 'readonly'
                    e4["state"] = 'readonly'

            if j == 4:
                e5 = Entry(window1, width=16, fg='blue')
                e5.grid(row=i, column=6, pady=2)
                e6 = Entry(window1, width=16, fg='blue')
                e6.grid(row=i, column=7, pady=2)

                if (Schedule[4] == "" or Schedule[4] == None):
                    e5["state"] = 'readonly'
                    e6["state"] = 'readonly'

                else:
                    trainee3 = conn.execute("SELECT First_name, ID FROM Schedule WHERE ID=?", (id3,))
                    z=trainee3.fetchall()
                    e5.insert(END, z[0][0])
                    e6.insert(END, z[0][1])
                    e5["state"] = 'readonly'
                    e6["state"] = 'readonly'

        i = i + 1
    exitbutton = tk.Button(window1, text="EXIT", command=window1.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i + 1, column=4)


btn5 = tk.Button(window, text="Search by Job", command=getjob, width=15, bg='Grey', fg='white', )
btn5.pack(pady=3)

btn6 = tk.Button(window, text="add employee", command=add_employee, width=15, bg='Grey', fg='white')
btn6.pack(pady=3)

btn6 = tk.Button(window, text="remove employee", command=remove_emp, width=15, bg='Grey', fg='white')
btn6.pack(pady=3)

btn7 = tk.Button(window, text="Update info by ID", command=updateinfo, width=15, bg='Grey', fg='white')
btn7.pack(pady=3)

btn8 = tk.Button(window, text="View teams", command=get_teams, width=15, bg='Grey', fg='white')
btn8.pack(pady=3)

btn9 = tk.Button(window, text="create teams", command=create_teams, width=15, bg='Grey', fg='white')
btn9.pack(pady=3)

windowmessage = Label(window, text="")
windowmessage.pack(pady=3)

window.mainloop()
