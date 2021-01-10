import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("C:/Users/WARD/PycharmProjects/pythonProject3/my_data.db")
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Tools (
#                 Tool_SN text,
#                 Tool_name text,
#                 Worker_f_name text,
#                 Worker_l_name text,
#                 Worker_ID int
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

top = Label(window, text="Tool_SN")
top.grid(row=0, column=0)
top1 = Label(window, text="Tool_name")
top1.grid(row=1, column=0)
top2 = Label(window, text="Worker_first")
top2.grid(row=2, column=0)
top3 = Label(window, text="Worker_last")
top3.grid(row=3, column=0)
top4 = Label(window, text="Worker_ID")
top4.grid(row=4, column=0)


def save_time_of_work():
    try:
        int(entry.get())
        val = entry.get()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    windowmessage.config(text="")
    val1 = entry1.get().lower().capitalize()
    val2 = entry2.get().lower().capitalize()
    val3 = entry3.get().lower().capitalize()
    try:
        int(entry4.get())
        val4 = entry4.get()
    except ValueError:
        windowmessage.config(text="Not a valid input")
        return 0
    windowmessage.config(text="")

    with conn:
        cursor.execute("INSERT INTO Tools VALUES (:Tool_SN, :Tool_name, :Worker_f_name, :Worker_l_name, :Worker_ID)",
                       {'Tool_SN': val, 'Tool_name': val1, 'Worker_f_name': val2, 'Worker_l_name': val3,
                        'Worker_ID': val4})


def view_all():
    window1 = tkinter.Tk()
    window1.geometry("620x400")
    window1.title("Schedule list")

    top = Label(window1, text="Tool_SN")
    top.grid(row=0, column=0)
    top1 = Label(window1, text="Tool_name")
    top1.grid(row=0, column=1)
    top2 = Label(window1, text="Worker_first")
    top2.grid(row=0, column=2)
    top3 = Label(window1, text="Worker_last")
    top3.grid(row=0, column=3)
    top4 = Label(window1, text="Worker_ID")
    top4.grid(row=0, column=4)

    r_set = cursor.execute("SELECT Tool_SN, Tool_name, Worker_f_name, Worker_l_name, Worker_ID FROM Tools;")
    i = 1  # row value inside the loop
    for Tools in r_set:
        for j in range(len(Tools)):
            e = Entry(window1, width=20, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Tools[j])
            e["state"] = 'readonly'
        i = i + 1

    requested_id = Entry(window1, width=20, fg='blue')
    requested_id.grid(row=i + 1, column=2)
    row_temp=i
    def updateinfo():
        Worker_ID = requested_id.get()
        r = cursor.execute("SELECT Worker_ID FROM Tools;")
        if Worker_ID != "":
            Worker_ID = int(Worker_ID)
        flag = 0
        for row in r.fetchall():
            if row[0] == Worker_ID:
                flag = 1

        if flag == 0 or Worker_ID == None or Worker_ID == "":
            warning = Label(window1, text="Not a valid input", fg="Red")
            warning.grid(row=row_temp + 3, column=2)

            def after_time():
                warning.config(text="")

            warning.after(3000, after_time)


        elif flag == 1:
            window2 = tkinter.Tk()
            window2.geometry("620x400")
            window2.title("Info update")
            # window1message = Label(window2, text="")

            top = Label(window2, text="Tool_SN")
            top.grid(row=0, column=0)
            top1 = Label(window2, text="Tool_name")
            top1.grid(row=0, column=1)
            top2 = Label(window2, text="Worker_first")
            top2.grid(row=0, column=2)
            top3 = Label(window2, text="Worker_last")
            top3.grid(row=0, column=3)
            top4 = Label(window2, text="Worker_ID")
            top4.grid(row=0, column=4)

            r_set = cursor.execute(
                "SELECT Tool_SN, Tool_name, Worker_f_name, Worker_l_name, Worker_ID FROM Tools WHERE "
                "Worker_ID=:ID ", {'ID': requested_id.get()})
            i = 1  # row value inside the loop
            for Tools in r_set:
                for j in range(len(Tools)):
                    e = Entry(window2, width=20, fg='blue')
                    e.grid(row=i, column=j, pady=2)
                    e.insert(END, Tools[j])
                    e["state"] = 'readonly'
                i = i + 1

            j = 0
            i = i + 1

            top = Label(window2, text="Tool_SN")
            top.grid(row=2, column=0)
            top1 = Label(window2, text="Tool_name")
            top1.grid(row=2, column=1)
            top2 = Label(window2, text="Worker_first")
            top2.grid(row=2, column=2)
            top3 = Label(window2, text="Worker_last")
            top3.grid(row=2, column=3)
            top4 = Label(window2, text="Worker_ID")
            top4.grid(row=2, column=4)

            new = Entry(window2, width=20, fg='blue')
            new.grid(row=i, column=j, pady=2)

            new1 = Entry(window2, width=20, fg='blue')
            new1.grid(row=i, column=j + 1, pady=2)
            new1.insert(END, Tools[1])
            new1["state"] = 'readonly'

            new2 = Entry(window2, width=20, fg='blue')
            new2.grid(row=i, column=j + 2, pady=2)
            new2.insert(END, Tools[2])
            new2["state"] = 'readonly'

            new3 = Entry(window2, width=20, fg='blue')
            new3.grid(row=i, column=j + 3, pady=2)
            new3.insert(END, Tools[3])
            new3["state"] = 'readonly'

            new4 = Entry(window2, width=20, fg='blue')
            new4.grid(row=i, column=j + 4, pady=2)
            new4.insert(END, Tools[4])
            new4["state"] = 'readonly'

            def updateinfobutton():
                val = new.get()
                val4 = new4.get()

                with conn:
                    cursor.execute("""UPDATE Tools SET Tool_SN = ? WHERE Worker_ID = ?""", (val, val4))
                # window1message.config(text="Updated")

                window2.destroy()
                r_set = cursor.execute(
                    "SELECT Tool_SN, Tool_name, Worker_f_name, Worker_l_name, Worker_ID FROM Tools WHERE "
                    "Worker_ID=:ID ", {'ID': requested_id.get()})
                i = 1  # row value inside the loop
                for Tools in r_set:
                    for j in range(len(Tools)):
                        e = Entry(window1, width=20, fg='blue')
                        e.grid(row=i, column=j, pady=2)
                        e.insert(END, Tools[j])
                        e["state"] = 'readonly'
                    i = i + 1
                requested_id.delete(0, 'end')

            i = i + 1
            Updatebutton = tkinter.Button(window2, text="Update", command=updateinfobutton, width=12, bg='Grey',
                                          fg='white')
            Updatebutton.grid(row=i, column=1)
            exitbutton = tkinter.Button(window2, text="Exit", command=window2.destroy, width=12, bg='Grey', fg='white')
            exitbutton.grid(row=i, column=3)
            i = i + 1

    def deletebutton():
        ID = requested_id.get()
        with conn:
            cursor.execute("DELETE from Tools WHERE Worker_ID = :Worker_ID", {'Worker_ID': ID})

    DELETE = tkinter.Button(window1, text="DELETE", command=deletebutton, width=15, bg='Grey', fg='white')
    DELETE.grid(row=i + 2, column=2)

    updatebutton = tkinter.Button(window1, text="Press to update by ID", command=updateinfo, width=16, bg='Grey',
                                      fg='white')
    updatebutton.grid(row=i + 1, column=1)

    exitbutton = tkinter.Button(window1, text="Exit", command=window1.destroy, width=16, bg='Grey', fg='white')
    exitbutton.grid(row=i + 1, column=3)




btn0 = tkinter.Button(window, text="Save Work Time", command=save_time_of_work, width=15, bg='Grey', fg='white', )
btn0.grid(column=1, row=11)

btn0 = tkinter.Button(window, text="view all", command=view_all, width=15, bg='Grey', fg='white', )
btn0.grid(column=1, row=12)

windowmessage = Label(window, text="")
windowmessage.grid(column=1, row=13)

window.mainloop()
conn.close()
