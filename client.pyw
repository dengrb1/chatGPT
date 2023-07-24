import os
from tkinter import *
from tkinter import messagebox
from time import sleep
import sys
import webbrowser

# Define constants
CURRENT_DIR = os.getcwd()
FILE_ERROR = '文件丢失，请检查文件内容并重新安装'
task = f'taskkill -f -t -im '

# Define functions
def open_exe(exe_name):
    if os.path.exists(os.path.join(CURRENT_DIR, f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('system', FILE_ERROR)
def open_cmd(cmd_name):
    if os.path.exists(os.path.join(CURRENT_DIR, f"{cmd_name}.cmd")):
        os.system(f"start {cmd_name}.cmd")
    else:
        messagebox.showerror('system', 'cmd服务启动失败，请重新安装')
        pass
    pass

def web_xz():
    open_exe("xz_main")

def update():
    open_exe("update")

def quit_exe():
    os.system('taskkill -f -t -im free2gpt.exe')
    os.system('taskkill -f -t -im wuguokai.exe')
    os.system('taskkill -f -t -im chatkey.exe')
    os.system('taskkill -f -t -im bnu120.exe')
    os.system('taskkill -f -t -im 1chat.exe')
    os.system('taskkill -f -t -im chat_command.exe')
    os.system('taskkill -f -t -im sittings.exe')
    os.system('taskkill -f -t -im update.exe')
    os.system('taskkill -f -t -im xz_chat.exe')
    os.system('taskkill -f -t -im xz_main.exe')
    sys.exit()

def ol_web():
    open_exe('ol_web')

# Create GUI
root = Tk()
root.title('chatWEB')
root.geometry('200x200+400+400')
Label(root, text='chatGPT').pack()

bt_web_xz = Button(root, text='网站选择', command=web_xz)
ol_web_b = Button(root ,text='官网', command=ol_web)
quit_bt = Button(root, text='退出', command=quit_exe)

Label(root, text='chatWEB')
bt_web_xz.pack()
ol_web_b.pack()
quit_bt.pack()
Label(root,text='version 1.4 @2023-2024 dengrb1').pack()

# mainloop
root.mainloop()