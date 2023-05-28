from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()


def open_exe(exe_name):
    if exe_name == None:
        messagebox.showerror('程序错误：没有参数')
        pass
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('chatWEB', '重要文件丢失，请重新安装')
        pass