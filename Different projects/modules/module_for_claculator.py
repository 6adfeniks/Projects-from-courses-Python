# from tkinter import *
#
#
# def build(root):
#     formula = "0"
#     lbl = Label(text=formula, font=("Times New Roman", 21, "bold"), bg="#225", foreground="#FFF")
#     lbl.place(x=11, y=50)
#     btns = [
#         "1", "2", "3", "/",
#         "4", "5", "6", "+",
#         "7", "8", "9", "-",
#         "C", "0", "%", "*",
#         "del", "=",
#     ]
#     x = 10
#     y = 140
#     for bt in btns:
#         com = lambda x=bt: logical(formula, x)
#         Button(text=bt, bg="#FFF", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=115, height=79)
#         x += 117
#         if x > 400:
#             x = 10
#             y += 81
#
# def logical(formula, operation):
#     if operation == "C":
#         formula = ""
#     elif operation == "del":
#         formula = formula[0:-1]
#     elif operation == "=":
#         formula = str(eval(formula))
#     else:
#         if formula == "0":
#             formula = ""
#         formula += operation
#     update(formula)
#
#
#
#
#
# def update(formula):
#     global lbl
#     if formula == "":
#         formula = "0"
#     lbl.configure(text=formula)
#
#
# def main():
#     root = Tk()
#     root["bg"] = "#225"
#     root.geometry("485x550+200+200")
#     root.title("Калькулятор")
#     root.resizable(0, 0)
#     build(root)
#     root.mainloop()
#

"""
Выше не хочет работать почему-то, как надо, пришлось делать классы, хоть я в них не особо шарю еще, смотрел в инете
+- как что работает
"""
#def __init__(self, root):
     #   self.build()

from tkinter import *

class Main():


    def build(self):
        self.primer = "0"
        self.lbl = Label(text=self.primer, font=("Times New Roman", 21, "bold"), bg="#225", foreground="#FFF")
        self.lbl.place(x=11, y=50)
        buttns = [
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "C", "0", "%", "*",
            "del", "=",
        ]
        x = 10
        y = 140
        for but in buttns:
            comma = lambda x=but: self.reshenie(x, Button)
            Button(text=but, bg="#FFF", font=("Times New Roman", 17), command=comma).place(x=x, y=y, width=115, height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81


    def reshenie(self, operation, b):
        if operation == "C":
            self.primer = ""
        elif operation == "del":
            self.primer = self.primer[0:-1]
        elif operation == "=":
            self.primer = str(eval(self.primer))
        else:
            if self.primer == "0":
                self.primer = ""
            self.primer += operation
        self.update()

    def update(self):
        if self.primer == "":
            self.primer = "0"
        self.lbl.configure(text=self.primer)

def main():
    root = Tk()
    root["bg"] = "#225"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(0, 0)
    app = Main()
    app.build()
    root.mainloop()
