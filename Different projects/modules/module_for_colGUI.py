import tkinter
from tkinter import *
def creating_window():
    root = Tk()
    root.title("Перевод в p-ую систему счисления")
    root['width'] = 650
    root['height'] = 200
    btn1 = Button(root, text='Красный', bg='white', fg='black', width=20)
    btn1.place(x=50, y=20)

    btn2 = Button(root, text='Синий', bg='white', fg='black', width=20)
    btn2.place(x=250, y=20)

    btn3 = Button(root, text='Зеленый', bg='white', fg='black', width=20)
    btn3.place(x=450, y=20)

    btn4 = Button(root, text='Очистить', bg='white', fg='black', width=20)
    btn4.place(x=450, y=170)

    btn1['command'] = lambda: btn_red(root)
    btn2['command'] = lambda: btn_blue(root)
    btn3['command'] = lambda: btn_green(root)
    btn4['command'] = lambda: btn_clear(root)

    root.mainloop()

def btn_red(root):
    root["bg"] = "red"

def btn_blue(root):
    root["bg"] = "blue"

def btn_green(root):
    root["bg"] = "green"

def btn_clear(root):
    root["bg"] = "white"

def main():
    creating_window()