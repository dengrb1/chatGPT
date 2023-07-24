import os
import webbrowser
from tkinter import *
from tkinter import messagebox
import sys

root = Tk()
ml = os.getcwd()


# def
def china_github():
    webbrowser.open('https://kgithub.com/dengrb1/chatgpt')
    sys.exit()

def github():
    webbrowser.open('https://github.com/dengrb1/chatgpt')
    sys.exit()

def quit_exe():
    sys.exit()


# Button
cg_b = Button(root, text='国内镜像官网', command=china_github)
g_b = Button(root , text='国外官网', command=github)
q_b = Button(root ,text='返回', command=quit_exe)

# pack
Label(root , text='官网').pack()
cg_b.pack()
g_b.pack()
q_b.pack()


# mainloop
root.title('官网')
root.geometry('200x220')
root.mainloop()