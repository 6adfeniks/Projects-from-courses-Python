from tkinter import *
import tkinter.font as tkFont
import time
from PIL import ImageTk, Image

counter = 0
list_x_o_v2 = [
        '0', '1', '2',
        '3', '4', '5',
        '6', '7', '8',
    ]
buttons = []
buttons_hod = {}
runing = True
def create():
    root = Tk()
    root.title("TIC TAC TOE")
    root['width'] = 600
    root['height'] = 338
    ##на фон картинку
    img = Image.open('D:\PYTHON\HM_17_Akulich_Nikolay\modules\photo\Поле.jpg')
    image = ImageTk.PhotoImage(img)
    panel = Label(root, image=image)
    panel.pack()
    root.resizable(0, 0)
    ######################1111111###########################

    size = 3
    x = 150
    y = 10
    count = 1
    for i in range(size):
        for j in range(size):

            #img_1 = PhotoImage()
            btn = Button(root, fg='black', bd=3)

            btn['width'] = 9
            btn['height'] = 4
            btn.place(x=x, y=y)
            buttons.append(btn)
            buttons_hod[btn] = count
            count += 1

            x += 140

        x = 150
        y += 105
    # print(buttons_hod)
    # for i in range(size**2):
    #     buttons[i]['command'] = lambda: put_x_o(root, buttons[i])
    buttons[0]['command'] = lambda: put_x_o(root, buttons[0])
    buttons[1]['command'] = lambda: put_x_o(root, buttons[1])
    buttons[2]['command'] = lambda: put_x_o(root, buttons[2])
    buttons[3]['command'] = lambda: put_x_o(root, buttons[3])
    buttons[4]['command'] = lambda: put_x_o(root, buttons[4])
    buttons[5]['command'] = lambda: put_x_o(root, buttons[5])
    buttons[6]['command'] = lambda: put_x_o(root, buttons[6])
    buttons[7]['command'] = lambda: put_x_o(root, buttons[7])
    buttons[8]['command'] = lambda: put_x_o(root, buttons[8])
    root.mainloop()


def run(root, butn):
    def quit():
        root.destroy()
    butn["command"]=lambda: quit

def restart_button(root, bt):
    restart = Button(root, text='Exit(but i wanted restart)', font=("Times New Roman", 40), bg="#FFB6C1", fg="black")
    restart['width'] = 19
    restart['height'] = 2
    restart['command'] = lambda: root.destroy()
    restart.place(x=10, y=150)

    run(root, bt)



def put_x_o(root, bt):

    global counter
    global buttons_hod
    global list_x_o_v2
    x = 0
    o = 0

    if counter % 2 == 0:
        bt.config(text='X')
        list_x_o_v2[buttons_hod[bt]-1]='X'
        if len(list_x_o_v2) >= 3:
            x = check_win(list_x_o_v2)
            if x:
                primer = "X wins"

                lbl = Label(text=primer, font=("Times New Roman", 60, "bold"), bg="green", foreground="#FFF", width = 12)
                lbl.place(x=11, y=50)

                #img = PhotoImage() image = img,
                restart_button(root, bt)

        bt.config(state='disabled')

    else:
        bt.config(text='O')
        list_x_o_v2[buttons_hod[bt]-1]='O'
        if len(list_x_o_v2) >= 3:
            o = check_win(list_x_o_v2)
            if o:
                primer = "O wins"

                lbl = Label(text=primer, font=("Times New Roman", 60, "bold"), bg="green", foreground="#FFF", width = 12)
                lbl.place(x=11, y=50)

                restart_button(root, bt)

        bt.config(state='disabled')
    counter += 1

    if counter == 9:
        primer = "Draw"
        lbl = Label(text=primer, font=("Times New Roman", 60, "bold"), bg="yellow", foreground="black", width=12)
        lbl.place(x=11, y=50)
        restart_button(root, bt)


def check_win(board):
    #print(board)
    stat_for_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in stat_for_win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main():
    create()
###################################################






