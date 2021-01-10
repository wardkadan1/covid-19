from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import Menu
from tkinter import filedialog

window = Tk()

window.title("Welcome to the app")
window.geometry("1200x600")
menu = Menu(window)
new_item = Menu(menu)


def exit1():
    window.destroy()


def new_win():
    root = Tk()
    root.geometry("250x300")


new_item.add_command(label='the covid data', command=lambda: new_win())
menu.add_cascade(label='covid', menu=new_item)
new_item.add_command(label="Exit", command=exit1)


def Open_itch():
    webbrowser.open(
        "https://www.ox.ac.uk/")


tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

button = Button(tab1, text="oxford", command=Open_itch).grid(row=200, column=200, sticky=E, pady=2)
button2 = Button(tab1, text='test', command=lambda: new_win(), height=0, width=5).grid(row=250, column=200, sticky=E,
                                                                                       pady=2)
tab_control.pack(expand=1, fill='both')
window.config(menu=menu)
window.iconbitmap('/Users/HP/Downloads/p.ico')
window.mainloop()
# lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
