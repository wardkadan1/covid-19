from tkinter import*

# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

window = Tk()
window.geometry('400x300')


#def Information():



label1=Label(window,text="Ambulance order call:  101",font=("arial",15))
label1.place(x=10,y=20)


label2=Label(window,text="Referral order call: *2700 ",font=("arial",15))
label2.place(x=10,y=50)

label3=Label(window,text="Medication order go to: https://www.drugstore.co.il ",font=("arial",15))
label3.place(x=10,y=80)



window.mainloop()
