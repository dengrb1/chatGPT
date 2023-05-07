from tkinter import *
from tkinter import messagebox
import os
import webbrowser

# 定义内容和创建主窗口
root = Tk()
ml = os.getcwd()
ok = '安装成功'
install = 'pip install'
file_error = '文件丢失，请重新安装'


# 创建滚动区域的Canvas对象
canvas = Canvas(root, width=280, height=280, scrollregion=(0, 0, 500, 500))

# 创建可滚动区域的Frame对象，并将其添加到Canvas中
frame = Frame(canvas)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")

# 创建Scrollbar对象，并将其绑定到Canvas上
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# 显示Canvas和Scrollbar
canvas.pack(side="left", fill="both", expand=True)



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
def bnu120():
    open_exe('bnu120')
def lbbai():
    open_exe('lbbai')
def fh():
    root.destroy()


# Button
bt_wuguokai = Button(frame, text='wuguokai网站', command=wuguokai)
bt_extkj = Button(frame, text='extkj网站', command=extkj)
bt_qdymys = Button(frame, text='qdymys网站', command=qdymys)
bt_lbbai = Button(frame, text='lbbai网站', command=lbbai)
bt_bnu120 = Button(frame, text='bnu120网站', command=bnu120)
bt_fh = Button(frame, text='返回', command=fh)

# pack and Label
Label(root, text='选择界面').pack()
bt_wuguokai.pack()
bt_extkj.pack()
bt_lbbai.pack()
bt_qdymys.pack()
bt_bnu120.pack()
bt_fh.pack()


# mainloop
root.title('选择')
root.geometry('200x220+440+600')
root.mainloop()