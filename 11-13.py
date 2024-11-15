import tkinter as tk
from tkinter import *


window = Tk()

window.geometry("650x650")
textbox = Text(width = 60, height = 2)
textbox.place(x = 100, y = 100)


title = tk.Label(window, text = 'GUI Calculator', font = ("Arial", 20))
title.place(x = 255, y = 35)

def show(x):
    try:
        if x == '=':
            final_answer = eval(textbox.get(1.0, "end-1c"))
            textbox.delete(1.0, tk.END)
            textbox.insert(tk.INSERT, final_answer)
        else:
            textbox.insert(tk.INSERT, x)

    except:
        textbox.insert(tk.INSERT, '')

def clear():
    textbox.delete(1.0, tk.END)

b1 = Button(window, text = '1', width = 10, height=5, command=lambda : show("1"))
b1.place(x = 100, y = 150)

b2 = Button(window, text = '2', width= 10, height = 5, command=lambda : show("2"))
b2.place(x = 200, y = 150)

b3 = Button(window, text = '3', width = 10, height = 5, command=lambda : show("3"))
b3.place(x = 300, y = 150)


b4 = Button(window, text = '4', width = 10, height = 5, command=lambda : show("4"))
b4.place(x = 100, y = 250)

b5 = Button(window, text= '5', width = 10, height = 5, command=lambda : show("5"))
b5.place(x = 200, y=250)

b6 = Button(window, text='6', width = 10, height = 5, command=lambda : show("6"))
b6.place(x = 300, y = 250)


b7 = Button(window, text = '7', width = 10, height = 5, command=lambda : show("7"))
b7.place(x = 100, y = 350)

b8 = Button(window, text = '8', width = 10, height = 5, command=lambda : show("8"))
b8.place(x = 200, y = 350)

b9 = Button(window, text = '9', width = 10, height = 5, command=lambda : show("9"))
b9.place(x = 300, y = 350)


c = Button(window, text = 'C', width = 10, height=5, command=clear)
c.place(x=100, y=450)

b10 = Button(window, text = "0", width = 10, height = 5, command=lambda : show("0"))
b10.place(x = 200, y=450)


plus = Button(window, text = "+", width=10, height = 5, command=lambda : show("+"))
plus.place(x = 400, y = 150)

equal = Button(window, text='=', width = 10, height = 5, command=lambda :show("="))
equal.place(x = 300,y=450)

multiply = Button(window, text='X', width = 10, height = 5, command=lambda : show("*"))
multiply.place(x = 400, y = 350)

subtract = Button(window, text = '-', width = 10, height = 5, command=lambda : show("-"))
subtract.place(x = 400, y = 250)

divide = Button(window, text = '/', width = 10, height = 5, command=lambda : show("/"))
divide.place(x = 400, y = 450)
window.mainloop()


