from tkinter import *
from tkinter import messagebox
import os
import webbrowser


root = Tk()
file_error = '重要文件丢失！请重新安装'
ml = os.getcwd()

# Define functions
def open_exe(exe_name):
    if os.path.exists(os.path.join(ml, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('system', file_error)

def extkj():
    open_exe("extkj")

def wuguokai():
    open_exe("wuguokai")

def qdymys():
    open_exe("qdymys")

def lbbai():
    webbrowser.open("https://link.lbbai.com")

def fh():
    root.destroy()


# Button
bt_wuguokai = Button(root, text='wuguokai网站', command=wuguokai)
bt_extkj = Button(root, text='extkj网站', command=extkj)
bt_qdymys = Button(root, text='qdymys网站', command=qdymys)
bt_lbbai = Button(root, text='lbbai网站', command=lbbai)
bt_fh = Button(root, text='返回', command=fh)

# pack and Label
Label(root, text='选择界面').pack()
bt_wuguokai.pack()
bt_extkj.pack()
bt_qdymys.pack()
bt_lbbai.pack()
bt_fh.pack()


# mainloop
root.title('选择')
root.geometry('200x200+440+600')
root.mainloop()