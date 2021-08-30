def f(btn1, r, btn2):
    btn1['text'], btn2['text'] = btn2['text'], btn1['text']


######################################
import tkinter
from tkinter import *
root = Tk()
root.geometry('370x200+200+100')
btn1 = Button(root, text='Привет', bg='white', fg='black', width=10, height=3)
btn2 = Button(root, text='Медвед', bg='white', fg='black', width=10, height=3)
btn1.place(x = 100, y = 50)
btn2.place(x = 200, y = 50)

btn1['command'] = lambda: f(btn1, root, btn2)
btn2['command'] = lambda: f(btn1, root, btn2)

root.mainloop()