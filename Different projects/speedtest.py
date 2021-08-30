from tkinter import *
import speedtest

def clicked():
    test = speedtest.Speedtest()
    download = test.download()
    upload = test.upload()
    lbl.congigure(text=f"Speed:{(download/1024)/1024} Mb/s \n Upload"
                       f"Speed:{(upload/1024)/1024} Mb/s")


window = Tk()
window.title("SpeedTest")
window.geometry('400x250')
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
btn = Button(window, text='Start test of speed!', command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
