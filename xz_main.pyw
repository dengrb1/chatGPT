import os
from tkinter import *
from tkinter import messagebox
from time import time
import sys

root = Tk()
ml = os.getcwd()

def open_exe(exe_name):
    if os.path.exists(os.path.join(ml,f"{exe_name}.exe")):
        os.system(f'start {exe_name}.exe')
    else:
        messagebox.showerror('system','文件丢失！')
    pass

def chat():
    open_exe("xz_chat")

def quit_exe():
    sys.exit()

chat_b = Button(root ,text='聊天网站', command=chat)
q_b = Button(root ,text='返回', command= quit_exe)

Label(root, text='选择模式').pack()
chat_b.pack()
q_b.pack()

# mainloop
root.title('选择')
root.geometry('200x220')
root.mainloop()