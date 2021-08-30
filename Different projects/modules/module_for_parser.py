from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import pyperclip
import time
"""
Парсить будем инфу между тэгами
все почты
все ссылки
"""
url_1=''
def create():
    root = Tk()
    root.title("Parser")
    root['width'] = 600
    root['height'] = 400
    root.resizable(0,0)

    v = StringVar()
    v.set("Вставьте ссылку")
    entry = Entry(root, width=80, textvariable=v)
    entry.place(x=20, y=10)

    def del_lbl(lbl):
        time.sleep(3)
        lbl.destroy()

    def cmd_paste_btn():
        x=StringVar()
        x.set("")
        entry.config(textvariable=x)
        entry.insert(END, pyperclip.paste())
        paste_btn.destroy()
    paste_btn = Button(root, text="Вставить ссылку", command=lambda: cmd_paste_btn())
    paste_btn.place(x=200, y=40)

    btn = Button(root, text='1. Спарсить все почты в файл')
    btn.place(x=20, y=40)
    btn['command'] = lambda: btn_command()


    def btn_command():
        #lbl = Label(root)
        #lbl.place(x=10, y=6)
        url = str(entry.get())
        global url_1
        url_1=url
        #res = str(entry.get()) + "\nваша ссылка принята"
        #lbl['text'] = str(res)
       #entry.destroy()
        paste_btn.destroy()
        wow = Mails()
        wow.main(url, root)


    #####################################################################
    class Mails():

        def main(self, url, root):
            #url = 'https://www.belta.by/contacts/'
            response = requests.get(url).text
            soup = BeautifulSoup(response, 'lxml')
            items = soup.find_all('p')
            spisok = []
            for i in items:
                item_mail = i.text
                spisok.append(item_mail)
            #print(spisok)
            spiso4ek = []
            for word in spisok:
                item_m = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)+', word)
                if len(item_m) == 0:
                    continue
                else:
                    #print(item_m[0])
                    item_m[0] = re.sub(r'\d\d\d-\d\d-\d\d', '', item_m[0])
                    spiso4ek.append(item_m[0])
            #print(spiso4ek)

            ##############################################
            v_2 = StringVar()
            v_2.set("Имя файла для записи")
            entry_1 = Entry(root, width=30, textvariable=v_2)
            entry_1.place(x=200, y=40)
            btn_1 = Button(root, text='Записать в файл')
            btn_1.place(x=400, y= 40)
            btn_1["command"] = lambda: btn_1_command()
            def btn_1_command():
                text = str(entry_1.get())
                to_file(text, spiso4ek)
                entry_1.destroy()
                btn_1.destroy()
                lbl = Label(root)
                lbl.place(x=200, y=40)
                lbl['text'] = "Записано  в файл "+text+".txt \n(В той же директории где и файл)"
                #read_from_file(text)
                #по желаиню в консоль выводит почты

            ###################################################

    ##############################################################
    """След кнопки парсинга ссылок и функции"""
    btn_1 = Button(root, text='2. Спарсить все ссылки')
    btn_1.place(x=20, y=100)
    btn_1['command'] = lambda: btn_1_command()

    def btn_1_command():
        url = str(entry.get())
        global url_1
        url_1 = url
        wow_1= urls()
        wow_1.main(root)

        #entry.destroy()
        #wow = Mails()
        #wow.main(url, root)
    class urls():

        def main(self, root):
            spiso4ek_1 = []
            response = requests.get(url_1).text
            soup = BeautifulSoup(response, 'lxml')
            items = soup.find_all('div')
            spisok = []
            for i in items:
                item_mail = str(i)
                spisok.append(item_mail)

            for item in spisok:
                item_m = re.findall(r'<a href=".{,100}/"', item)
                if item_m:
                    it = re.sub(r'<a href="', '', item_m[0])
                    # item_m[0] = re.sub(r'^(/)".{0,100}','',item_m)
                    if 'https://' in it:
                        spiso4ek_1.append(it[:-1])


            v_3 = StringVar()
            v_3.set("Имя файла для записи")
            entry_2 = Entry(root, width=30, textvariable=v_3)
            entry_2.place(x=200, y=100)
            btn_2 = Button(root, text='Записать в файл')
            btn_2.place(x=400, y=100)
            btn_2["command"] = lambda: btn_2_command()

            def btn_2_command():
                text = str(entry_2.get())
                to_file(text, spiso4ek_1)
                entry_2.destroy()
                #btn_1.destroy()
                lbl = Label(root)
                lbl.place(x=200, y=100)
                lbl['text'] = "Записано  в файл " + text + ".txt \n(В той же директории где и файл)"
                btn_2.destroy()
    #####################################################################################################
    ####################################################################################################
    """Тут по тегам парсинг"""

    v_4 = StringVar()
    v_4.set("Введите тэг")
    entry_3 = Entry(root, width=30, textvariable=v_4)
    entry_3.place(x=20, y=150)


    btn_2 = Button(root, text='3. Спарсить по тэгу')
    btn_2.place(x=20, y=170)
    btn_2['command'] = lambda: btn_2_command()

    def btn_2_command():
        url = str(entry.get())
        global url_1
        url_1 = url
        tag = str(entry_3.get())
        entry_3.destroy()
        wow_2 = tags()
        wow_2.main(root, tag)


    class tags():

        def main(self, root, tag):
            spisokk = ''
            response = requests.get(url_1).text
            soup = BeautifulSoup(response, 'lxml')
            items = soup.find_all(tag)
            tekst = ''
            for i in items:
                tekst += str(i)
            tekst_11 = tekst[0:15000]


            v_5 = StringVar()
            v_5.set("Имя файла для записи")
            entry_5 = Entry(root, width=30, textvariable=v_5)
            entry_5.place(x=200, y=170)
            btn_5 = Button(root, text='Записать в файл')
            btn_5.place(x=400, y=170)
            btn_5["command"] = lambda: btn_5_command()

            def btn_5_command():
                text = str(entry_5.get())
                to_file_text(text, tekst_11)
                entry_5.destroy()
                lbl = Label(root)
                lbl.place(x=200, y=170)
                lbl['text'] = "Записано  в файл " + text + ".txt \n(В той же директории где и файл)"
                btn_5.destroy()

    root.mainloop()

def to_file(text, spiso4ek):
    with open(text + ".txt", "w") as f:
        count = 0
        for mail in spiso4ek:
            count += 1
            f.write(str(count) + ":" + mail)
            f.write('\n')

def to_file_text(text, soder):
    with open(text + ".txt", "w") as f:
        f.write(soder)
# def read_from_file(text):
#     with open(text+".txt", "r") as f:
#         print(f.read().replace(';', '\n'))


def main_1():
    create()
