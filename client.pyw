import os
import platform
import tkinter as tk
from tkinter import messagebox

# Define constants
CURRENT_DIR = os.getcwd()
FILE_ERROR = '文件丢失，请检查文件内容并重新安装'
system = platform.system()

# Define functions
def open_exe(exe_name):
    if os.path.exists(os.path.join(CURRENT_DIR, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('system', FILE_ERROR)

def extkj():
    open_exe("extkj")

def wuguokai():
    open_exe("wuguokai")

def f1():
    open_exe("aiyunos")

def update():
    if os.path.exists(os.path.join(CURRENT_DIR, "update.exe")):
        os.system("start update.exe")
    else:
        messagebox.showerror('update', '更新日志文件丢失，请检查文件并重新安装')

def user_xy():
    if os.path.exists(os.path.join(CURRENT_DIR, "使用协议.docx")):
        os.system("start 使用协议.docx")
    else:
        messagebox.showerror('使用协议','文档丢失，请检查文件内容并重新安装')
        pass
    pass

def quit_exe():
    os.system('taskkill -f -t -im aiyunos.exe')
    os.system('taskkill -f -t -im extkj.exe')
    os.system('taskkill -f -t -im gk.exe')
    os.system('taskkill -f -t -im update.exe')
    os.system('taskkill -f -t -im wuguokai.exe')
    root.destroy()

# Create GUI
root = tk.Tk()
root.title('chatGPT')
root.geometry('200x200+400+400')
tk.Label(root, text='chatGPT').pack()

bt_w = tk.Button(root, text='wuguokai网站', command=wuguokai)
bt_e = tk.Button(root, text='extkj网站', command=extkj)
bt_f1 = tk.Button(root, text='aitianhu网站', command=f1)
bt_xy = tk.Button(root, text='使用协议（使用前必看）', command=user_xy)
bt_update = tk.Button(root, text='更新日志', command=update)
quit_bt = tk.Button(root, text='退出', command=quit_exe)

bt_w.pack()
bt_e.pack()
bt_f1.pack()
# bt_xy.pack()
bt_update.pack()
quit_bt.pack()

# mainloop
root.mainloop()