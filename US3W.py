import tkinter as tk
import random
from tkinter import *

window = tk.Tk()
window.geometry("475x400")
window.title("")
window.resizable(False, False)

choice=random.randrange(0,7)
def tips(choice):
    if(choice==0):
        Label(window, text='Make sure to keep your distance from other people at the workplace.').pack(side="bottom")
    elif(choice==1):
        Label(window, text='Make sure to wash your hands regularly in order to maintain your hygiene.').pack(side="bottom")
    elif(choice==2):
        Label(window, text='Make sure to maintain the hygiene of the workplace and the tools used.').pack(side="bottom")
    elif(choice==3):
        Label(window, text='Make wearing a mask a normal part of being around other people.').pack(side="bottom")
    elif(choice==4):
        Label(window, text='Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze.').pack(side="bottom")
    elif(choice==5):
        Label(window, text='Stay home and self-isolate even if you have minor symptoms such as cough, headache, mild fever.').pack(side="bottom")
    elif(choice==6):
        Label(window, text='Keep up to date on the latest information from trusted sources, such as WHO or your local and national health authorities.').pack(side="bottom")


tips(choice)
window.mainloop()