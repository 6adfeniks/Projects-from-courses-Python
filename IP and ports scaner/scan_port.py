"""
в Перемнную ip нужно ввести свое ip чтобы видеть открыте порты свои
"""


##pogif
import socket
from datetime import datetime
import threading
from tkinter import *

lis = []
ls = ''
ip = ''
def create():
    root = Tk()
    root.geometry('600x400')
    root.resizable(0,0)
    root.title("Scan for open ports")

    btn = Button(root, text="Scan!)))",font=("Times New Roman", 20), width=20, height=3)
    btn.place(x=10, y=50)
    btn["command"]=lambda: btn_c()

    v= StringVar()
    v.set("Your IP")
    entry = Entry(root, width=20, textvariable=v)
    entry.place(x=10, y=10)


    def btn_c():
        global ip
        global lis
        ip = str(entry.get())
        calculate(ip)
        s = ''
        for el in lis:
            s +="Port :" + str(el)+" is open" + "\n"
        s += "\n" + ls + "\n"
        lbl = Label(text=s, font=("Times New Roman", 14, "bold"), bg="white", foreground="black", width=30)
        lbl.place(x=11, y=200)


    root.mainloop()

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        global lis
        connect = sock.connect((ip,port)) #0 -- 999
        lis.append(port)
        sock.close()
    except:
    #заглушка/пустое/ничего не делать/
        pass
#Адрес нашего маршрутизатор --> cmd -- ipconfig -->шлюз по умолчанию
def calculate(ip):
    global ls
    start = datetime.now()

    # 0 -- 10000
    # for i in range(10):
    #     scan_port(ip, i) #0--999 включит
    for i in range(10000):
        potoc = threading.Thread(target=scan_port, args=(ip, i))
        potoc.start()

    ends = datetime.now()
    # print("Time: start - ", start, "  end - ", ends)
    # print('Time : {}'.format(ends-start))
    ls = str('Time : {}'.format(ends - start))


def main():
    create()
main()
