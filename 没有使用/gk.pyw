from tkinter import *
from tkinter import messagebox
import webbrowser


root = Tk()
web = webbrowser


def fh():
    root.destroy()

def run_web():
    web.open("https://github.com/dengrb1/chatgpt")
    pass

Label(root, text='关于').pack()
Label(root ,text='程序官方下载地址:https://github.com/dengrb1/chatgpt/').pack()

# button
Button(root ,text='打开网站', command=run_web).pack()
Button(root ,text='返回', command=fh).pack()


# mainloop
