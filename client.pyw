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
    open_exe("f1")

def lbb():
    open_exe("lbb")

def update():
    if os.path.exists(os.path.join(CURRENT_DIR, "update.exe")):
        os.system("start update.exe")
    else:
        messagebox.showerror('update', '更新日志文件丢失，请检查文件并重新安装')

def quit_exe():
    root.destroy()

# Create GUI
root = tk.Tk()
root.title('chatGPT')
root.geometry('200x200+400+400')
tk.Label(root, text='chatGPT').pack()

bt_w = tk.Button(root, text='wuguokai网站', command=wuguokai)
bt_e = tk.Button(root, text='extkj网站', command=extkj)
bt_f1 = tk.Button(root, text='f1网站', command=f1)
bt_update = tk.Button(root, text='更新日志', command=update)
quit_bt = tk.Button(root, text='退出', command=quit_exe)

bt_w.pack(side=tk.TOP, pady=5)
bt_e.pack(side=tk.TOP, pady=5)
bt_f1.pack(side=tk.TOP, pady=5)
bt_update.pack(side=tk.TOP, pady=5)
quit_bt.pack(side=tk.BOTTOM)

# mainloop
root.mainloop()
