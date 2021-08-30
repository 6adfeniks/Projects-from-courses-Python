
import os
import platform

#для многопоточности
import threading
import socket

from datetime import datetime

from tkinter import *
def create():
    root = Tk()
    root.title("ip scan")
    root.geometry('400x300')
    root.resizable(0,0)
    btn = Button(root, text='Узнать IP', bg='white', fg='black', width=20, height=2)
    btn['command']=lambda: btn_1()
    btn.place(x=10, y=20)
    def btn_1():
        net = getMyIp()
        lbl = Label(root)
        lbl.config(text="Your IP:"+str(net))
        lbl.place(x=200, y=20)
    root.mainloop()



def getMyIp():
    #Создаем сокет (UDP)
    #socket.AF_INET  - сокет для IPv4
    #SOCK_DGRAM - UDP сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Настраиваем сокет на BROADCAST вещание.
    #SOCK_DGRAM - широковещательная рассылочка
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    s.connect(('<broadcast>', 0))
    #s.getsockname() - вернет ваш IP адрес
    return s.getsockname()[0]


def main():
    create()
main()