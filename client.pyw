import os
from tkinter import *
from tkinter import ttk, messagebox
import platform


root = Tk()
ml = os.getcwd()
system = platform.system()
flie_error = '文件丢失，请检查文件内容并重新安装'


def extkj():
    if os.path.exists("{ml}\extkj.exe"):
        os.system('start {ml}\extkj.exe')
    else:
        messagebox.showerror('system', flie_error)
        pass
    pass

def wuguokai():
    if os.path.exists("{ml}\wuguokai.exe"):
        os.system("start {ml}\wuguokai.exe")
    else:
        messagebox.showerror('system', flie_error)
        pass
    pass

def f1():
    if os.path.exists("{ml}\\f1.exe"):
        os.system("start {ml}\\f1.exe")
    else:
        messagebox.showerror('system', flie_error)
        pass
    pass

def lbb():
    if os.path.exists("{ml}\lbb.exe"):
        os.system("start {ml}\lbb.exe")
    else:
        messagebox.showerror('system', flie_error)
        pass
    pass

def update():
    if os.path.exists("{ml}\update.exe"):
        os.system("start {ml}\update.exe")
    else:
        messagebox.showerror('update', '更新日志文件丢失，请检查文件并重新安装')
        pass
    pass

def quit_exe():
    root.destroy()
    pass


# button
bt_e = Button(root ,text='extkj网站', command=extkj)
bt_w = Button(root ,text='wuguokai网站', command=wuguokai)
bt_f1 = Button(root, text='f1网站', command=f1)
bt_update = Button(root, text='更新日志', command=update)
quit_bt = Button(root, text='退出', command=quit_exe)


# Label
Label(root, text='chatGPT').pack()


# pack_2
bt_w.pack()
bt_e.pack()
bt_f1.pack()
bt_update.pack()
quit_bt.pack()


# mainloop
root.title('chatGPT')
root.geometry('200x200+400+400')
root.mainloop()