from tkinter import *


root = Tk()


def quit_exe():
    root.destroy()
    pass


# Label
Label(root, text='更新日志').pack()
Label(root, text='''1.0 DEMO制作完成
1.1 demo版本增加lbbAI网站
1.2 demo版本删除lbbAI网站，因为无法使用''').pack()

Label(root, text='当前版本:1.2 beta_demo').pack()

# Button
quit_bt = Button(root, text='返回', command=quit_exe).pack()


# mainloop
root.title('更新日志')
root.geometry('260x250+400+400')
root.mainloop()