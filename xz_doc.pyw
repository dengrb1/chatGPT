from tkinter import *
from tkinter import messagebox
import os
import webbrowser


root = Tk()
ml = os.getcwd()


def open_exe(exe_name):
    if exe_name == None:
        messagebox.showerror('chatWEB', '程序错误：没有参数')
    if os.path.exists(ml, f"{exe_name}.exe"):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror("ChatWEB", '重要文件丢失，请重新安装')
    pass
def chat2doc():
    webbrowser.open("https://chat2doc.cn")
    pass
def fh():
    root.destroy()


# Button
chat2doc_bt = Button(root, text='chat2doc网站', command=chat2doc)
fh_bt = Button(root, text='返回', command=fh)

# pack
Label(root, text='选择').pack()
chat2doc_bt.pack()
fh_bt.pack()


# mainloop
root.title('选择')
root.geometry('200x200+700+400')
root.mainloop()