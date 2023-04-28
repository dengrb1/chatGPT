import tkinter as tk
from tkinter import messagebox

def quit_exe():
    root.destroy()

root = tk.Tk()
root.title('Error 422')
root.geometry('100x100')

messagebox.showerror('System', '别看了，已经废弃了')

btn_quit = tk.Button(root, text='退出', command=quit_exe)
btn_quit.pack()

root.mainloop() 
