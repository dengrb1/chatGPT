import os
import platform
import tkinter as tk
from tkinter import messagebox
from time import sleep
import sys

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
    os.system('taskkill -f -t -im qdymys.exe')
    os.system('taskkill -f -t -im wuguokai.exe')
    os.system('taskkill -f -t -im extkj.exe')
    os.system('taskkill -f -t -im bnu120.exe')
    os.system('taskkill -f -t -im lbbai.exe')
    os.system('taskkill -f -t -im chat_command.exe')
    os.system('taskkill -f -t -im python.exe')
    sys.exit()

def jc():
    messagebox.showerror('system', '检测程序暂时无法使用！！！(应该以后都不会写完了......)')
    pass

def gk():
    open_exe("gk")

def sittings():
    st = tk.Tk()
    bt_update = tk.Button(st, text='更新日志', command=update)
    bt_gk = tk.Button(st, text='关于', command=gk)
    bt_jc = tk.Button(st, text='检测文件完整度', command=jc)
    # pack
    bt_jc.pack()
    bt_update.pack()
    bt_gk.pack()
    # mainloop
    st.title('设置')
    st.geometry("200x200+400+600")
    st.mainloop()


# Create GUI
root = tk.Tk()
root.title('chatGPT')
root.geometry('200x200+400+400')
tk.Label(root, text='chatGPT').pack()

bt_web_xz = tk.Button(root, text='网站选择', command=web_xz)
bt_st = tk.Button(root, text='其他内容', command=sittings)
quit_bt = tk.Button(root, text='退出', command=quit_exe)

bt_web_xz.pack()
bt_st.pack()
quit_bt.pack()

# mainloop
root.mainloop()