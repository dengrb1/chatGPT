from tkinter import *
from tkinter import messagebox
import os


root = Tk()
ml = os.getcwd()


def open_exe(exe_name):
    if exe_name == None:
        messagebox.showerror('程序错误：没有参数')
        pass
    if os.path.exists(ml, f"{exe_name}.exe"):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('chatWEB', '重要文件丢失，请重新安装')
        pass
    
def chat():
    open_exe('xz_chat')
def doc():
    messagebox.showerror('ChatWEB', '暂时无法使用，请耐心等待......')
def fh():
    root.destroy()


# Button
chat_bt = Button(root, text='Chat网站', command=chat)
doc_bt = Button(root, text='doc和pdf网站', command=doc)
fh_bt = Button(root, text='返回', command=fh)

# pack
Label(root, text='选择界面').pack()
chat_bt.pack()
doc_bt.pack()
fh_bt.pack()


# mainloop
root.title('选择')
root.geometry('200x200+400+600')
root.mainloop()