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
def aiyunos():
    open_exe("aiyunos")
def wuguokai():
    open_exe("wuguokai")
def chatkey():
    open_exe("chatkey")
def bnu120():
    open_exe('bnu120')
def free2gpt():
    open_exe('free2gpt')
def fh():
    root.destroy()


# Button
bt_wuguokai = Button(frame, text='wuguokai网站', command=wuguokai)
bt_aiyunos = Button(frame, text='aiyunos网站', command=aiyunos)
bt_chatkey = Button(frame, text='chatkey网站', command=chatkey)
bt_free2gpt = Button(frame, text='free2gpt网站', command=free2gpt)
bt_bnu120 = Button(frame, text='bnu120网站', command=bnu120)
bt_fh = Button(frame, text='返回', command=fh)

# pack and Label
Label(root, text='选择界面').pack()
bt_wuguokai.pack()
bt_aiyunos.pack()
bt_free2gpt.pack()
bt_chatkey.pack()
bt_bnu120.pack()
bt_fh.pack()


# mainloop
root.title('chatWEB')
root.geometry('200x220+440+600')
root.mainloop()