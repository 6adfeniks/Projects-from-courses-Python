import tkinter
from tkinter import *
def creating_window():

    root = Tk()
    root.title("Перевод в p-ую систему счисления")
    root['width'] = 400
    root['height'] = 200

    v = StringVar()
    v.set("10 to 2")
    entry = Entry(root, width=30, textvariable=v)
    entry.place(x=20, y=50)

    btn = Button(root, text='Вычислить')
    btn.place(x=20, y=70)

    label = Label(root)
    label.place(x=10, y=5)
    label.configure(text="10 to 2 (значит что 10 в двоичную систему)")

    lbl = Label(root)
    lbl.place(x=200, y=50)

    def btn_command():
        per = perevod()
        res = per.dec2k1(entry.get()) #entry.get()
        lbl['text'] = '= ' + str(res)

    btn['command'] = btn_command

    show_window(root)


def show_window(root):
    root.mainloop()
    pass


digits = '0123456789' + "".join([chr(i) for i in range(ord('A'), ord('Z') + 1)])
class perevod():
    # def __init__(self):
    #     print()

    def dec2k(self, num, k):
        if num < k:
            return digits[num]
        return self.dec2k(num // k, k) + digits[num % k]

    def dec2k1(self, s):
        lst = s.split(' to ')
        num = int(lst[0])
        k = int(lst[1])
        x = self.dec2k(num, k)
        return x


def main():
    creating_window()