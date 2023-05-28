import sys
from tkinter import *
from tkinter import messagebox
import os
import requests

root = Tk()
ml = os.getcwd()
file_path = os.path.join(ml, "api_key.txt")


def open_exe(exe_name):
    if os.path.exists(os.path.join(ml ,f"{exe_name}.exe")):
        os.system(f"start {exe_name}.exe")
    else:
        messagebox.showerror('chatGPT','错误：命令行文件不存在!')
    pass
def chat_command():
    API_key = entry_APIkey.get()
    if API_key != None:
        with open(file_path,'w') as f:
            f.write(API_key)
            pass
        open_exe('chat_command')
        pass
    else:
        messagebox.showerror('错误','API_key不存在！无法使用！')

def fh():
    sys.exit()


# Button
run_command = Button(root,  text='chatGPT启动', command=chat_command)
fh_bt = Button(root, text='返回', command=fh)

# entry
entry_APIkey = Entry(root)

# grid
Label(root, text='api_key:').grid(row=0,column=0)
entry_APIkey.grid(row=0, column=1)
run_command.grid(row=2,column=0)
fh_bt.grid(row=2,column=1)


# mainloop
root.title('chatGPT')
root.geometry('200x250+100+100')
root.mainloop()