import os
import webbrowser
from tkinter import *
from tkinter import messagebox


root = Tk()
ml = os.getcwd()


def jc(exe_name):
    if os.path.exists(os.path.join(ml,f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror("sittings", '系统文件丢失！请重新安装')
        pass
    pass

def gk():
    jc("gk")

def update():
    jc("update")

def fh():
    root.destroy()


# Button, Label and pack
Label(root, text='其他内容').pack()
bt_update = Button(root, text='更新日志', command=update).pack()
bt_gk = Button(root, text='关于', command=gk).pack()


# mainloop
root.title("其他")
root.geometry("200x200+400+400")
root.mainloop()