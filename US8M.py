import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("C:/Users/WARD/PycharmProjects/pythonProject3/my_data.db")
cursor = conn.cursor()

window = tkinter.Tk()
window.geometry("750x500")
window.title("salary list")


def salary():
    top1 = Label(window, text="Doctor_First")
    top1.grid(row=0, column=0)
    top2 = Label(window, text="Doctor_Last")
    top2.grid(row=0, column=1)
    top3 = Label(window, text="Doctor_ID")
    top3.grid(row=0, column=2)
    top4 = Label(window, text="Job")
    top4.grid(row=0, column=3)
    top5 = Label(window, text="hours")
    top5.grid(row=0, column=4)
    top6 = Label(window, text="overtime_hours")
    top6.grid(row=0, column=5)
    top7 = Label(window, text="patients_treated")
    top7.grid(row=0, column=6)
    top8 = Label(window, text="salary")
    top8.grid(row=0, column=7)

    r_set = conn.execute("SELECT First_name,Last_name,ID,Job,hours,overtime_hours,patients_treated,salary FROM "
                         "Schedule;")
    i = 1  # row value inside the loop
    for Salary in r_set:
        for j in range(len(Salary)):
            e = Entry(window, width=15, fg='blue')
            e.grid(row=i, column=j, pady=2)
            e.insert(END, Salary[j])
            e["state"] = 'readonly'
        i = i + 1

    exitbutton = tkinter.Button(window, text="Exit", command=window.destroy, width=12, bg='Grey', fg='white')
    exitbutton.grid(row=i, column=4)
    row_temp = i

    def update():
        window1 = tkinter.Tk()
        window1.geometry("1200x400")
        window1.title("update salary")

        r = cursor.execute("SELECT ID FROM Schedule;")
        flag = 0
        # print(r.fetchall())
        for row in r.fetchall():
            if entry13.get()!='':
                if row[0] == int(entry13.get()):
                    flag = 1

        if flag == 0 :
            window1.destroy()
            entry13.delete(0, "end")
            warning = Label(window, text="This employee\n does'nt exist!", fg="Red")
            warning.grid(row=row_temp + 2, column=3)

            def after_time():
                warning.config(text="")

            warning.after(3000, after_time)
        else:
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

            ID = entry13.get()
            r_set = conn.execute(
                "SELECT First_name, Last_name, ID, Job, hours, overtime_hours,patients_treated,salary FROM Schedule "
                "Where "
                "ID=:ID",
                {'ID': ID})
            i = 1  # row value inside the loop
            for Schedule in r_set:
                for j in range(len(Schedule)):
                    e = Entry(window1, width=17, fg='blue')
                    e.grid(row=i, column=j, pady=2)
                    e.insert(END, Schedule[j])
                    e["state"] = 'readonly'
                i = i + 1

            top1 = Label(window1, text="Doctor_First")
            top1.grid(row=2, column=0)
            top2 = Label(window1, text="Doctor_Last")
            top2.grid(row=2, column=1)
            top3 = Label(window1, text="Doctor_ID")
            top3.grid(row=2, column=2)
            top4 = Label(window1, text="Job")
            top4.grid(row=2, column=3)
            top5 = Label(window1, text="New hours")
            top5.grid(row=2, column=4)
            top6 = Label(window1, text="New overtime hours")
            top6.grid(row=2, column=5)
            top7 = Label(window1, text="New patients treated")
            top7.grid(row=2, column=6)
            top8 = Label(window1, text="New salary")
            top8.grid(row=2, column=7)

            new1 = Entry(window1, width=17, fg='blue')
            new1.grid(row=3, column=0, pady=2)
            new1.insert(END, Schedule[0])
            new1["state"] = 'readonly'

            new2 = Entry(window1, width=17, fg='blue')
            new2.grid(row=3, column=1, pady=2)
            new2.insert(END, Schedule[1])
            new2["state"] = 'readonly'

            new3 = Entry(window1, width=17, fg='blue')
            new3.grid(row=3, column=2, pady=2)
            new3.insert(END, Schedule[2])
            new3["state"] = 'readonly'

            new4 = Entry(window1, width=17, fg='blue')
            new4.grid(row=3, column=3, pady=2)
            new4.insert(END, Schedule[3])
            new4["state"] = 'readonly'

            new5 = Entry(window1, width=17, fg='blue')
            new5.grid(row=3, column=4, pady=2)

            new6 = Entry(window1, width=17, fg='blue')
            new6.grid(row=3, column=5, pady=2)

            new7 = Entry(window1, width=17, fg='blue')
            new7.grid(row=3, column=6, pady=2)

            new8 = Entry(window1, width=17, fg='blue', text="")
            new8.grid(row=3, column=7, pady=2)
            new8["state"] = 'readonly'

            def updateinfobutton():

                job = new4.get().lower().capitalize()
                val5 = new5.get()
                val5 = float(val5)
                val6 = new6.get()
                val6 = float(val6)
                val7 = new7.get()
                val7 = float(val7)
                val_id = new3.get()

                new_salary = 0

                if job == "Doctor":
                    new_salary = (100 * val5) + (100 * 1.5 * val6) + (100 * 2 * val7)
                elif job == "Surgeon":
                    new_salary = (150 * val5) + (150 * 1.5 * val6) + (150 * 2 * val7)
                elif job == "Nurse":
                    new_salary = (75 * val5) + (75 * 1.5 * val6) + (75 * 2 * val7)
                else:
                    new_salary = (50 * val5) + (50 * 1.5 * val6) + (50 * 2 * val7)
                with conn:
                    cursor.execute(
                        """UPDATE Schedule SET hours = ?, overtime_hours = ?, patients_treated=?, salary=? WHERE ID = ?""",
                        (val5, val6, val7, int(new_salary), val_id))

                window1.destroy()

                r_set = conn.execute(
                    "SELECT First_name,Last_name,ID,Job,hours,overtime_hours,patients_treated,salary FROM Schedule")
                i = 1  # row value inside the loop
                for Salary in r_set:
                    for j in range(len(Salary)):
                        e = Entry(window, width=15, fg='blue')
                        e.grid(row=i, column=j, pady=2)
                        e.insert(END, Salary[j])
                        e["state"] = 'readonly'
                    i = i + 1

                entry13.delete(0, "end")

            Updatebutton = tkinter.Button(window1, text="Update", command=updateinfobutton, width=12, bg='Grey',
                                          fg='white')
            Updatebutton.grid(row=4, column=2)

            exitbutton = tkinter.Button(window1, text="Exit", command=window1.destroy, width=12, bg='Grey', fg='white')
            exitbutton.grid(row=4, column=5)

    btn3 = tkinter.Button(window, text="Update by id", command=update, width=12, bg='Grey', fg='white')
    btn3.grid(column=2, row=i, pady=2)

    entry13 = tkinter.Entry(window, width=15, fg='blue')
    entry13.grid(row=i, column=3, pady=2)


salary()
window.mainloop()
