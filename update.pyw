from tkinter import *


root = Tk()


def quit_exe():
    root.destroy()
    pass


# Label
Label(root, text='更新日志').pack()
Label(root, text='''0.1.0 DEMO制作完成
0.1.1 demo版本增加lbbAI网站
0.1.2 demo版本删除lbbAI网站，因为无法使用
0.1.3 修复BUG
1.0 正式版，加入关于模块，更新网站aitianhu.top；修复“退出”按钮的问题；优化了代码''').pack()

Label(root, text='当前版本:1.0 official version').pack()

# Button
quit_bt = Button(root, text='返回', command=quit_exe).pack()


# mainloop
root.title('更新日志')
root.geometry('260x250+400+400')
root.mainloop()