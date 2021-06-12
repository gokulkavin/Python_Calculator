from tkinter import *

window = Tk()
window.geometry('350x350')

entry = Entry(window, width=56, borderwidth=5)
entry.place(x=0, y=0)


def btclick(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))


def clear():
    entry.delete(0, END)


button = Button(window, text='C', width=12, command=clear)
button.place(x=10, y=60)


def div():
    firstno = entry.get()
    global math, f
    math = 'division'
    f = int(firstno)
    entry.delete(0, END)


button = Button(window, text='/', width=12, command=div)
button.place(x=80, y=60)


def mul():
    firstno = entry.get()
    global math, f
    math = 'multiplication'
    f = int(firstno)
    entry.delete(0, END)


button = Button(window, text='*', width=12, command=mul)
button.place(x=170, y=60)


def sub():
    firstno = entry.get()
    global math, f
    math = 'subtraction'
    f = int(firstno)
    entry.delete(0, END)


button = Button(window, text='-', width=12, command=sub)
button.place(x=240, y=60)
button = Button(window, text='7', width=12, command=lambda: btclick(7))
button.place(x=10, y=120)
button = Button(window, text='8', width=12, command=lambda: btclick(8))
button.place(x=80, y=120)
button = Button(window, text='9', width=12, command=lambda: btclick(9))
button.place(x=170, y=120)


def add():
    firstno = entry.get()
    global math, f
    math = 'addition'
    f = int(firstno)
    entry.delete(0, END)


button = Button(window, text='+', width=12, command=add)
button.place(x=240, y=120)
button = Button(window, text='4', width=12, command=lambda: btclick(3))
button.place(x=10, y=180)
button = Button(window, text='5', width=12, command=lambda: btclick(5))
button.place(x=80, y=180)
button = Button(window, text='6', width=12, command=lambda: btclick(6))
button.place(x=170, y=180)


def equal():
    secondno = entry.get()
    entry.delete(0, END)
    if math == 'addition':
        entry.insert(0, f + int(secondno))
    elif math == 'subtraction':
        entry.insert(0, f - int(secondno))
    elif math == 'multiplication':
        entry.insert(0, f * int(secondno))
    elif math == 'division':
        entry.insert(0, f / int(secondno))


button = Button(window, text='=', width=12, command=equal)
button.place(x=240, y=180)
button = Button(window, text='0', width=12, command=lambda: btclick(0))
button.place(x=10, y=240)
button = Button(window, text='1', width=12, command=lambda: btclick(1))
button.place(x=80, y=240)
button = Button(window, text='2', width=12, command=lambda: btclick(2))
button.place(x=170, y=240)
button = Button(window, text='3', width=12, command=lambda: btclick(3))
button.place(x=240, y=240)
window.mainloop()
