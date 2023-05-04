from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()

def quit_exe():
    root.destroy()

# Label
Label(root, text='更新日志').pack()
text = '''0.1.0 DEMO制作完成
0.1.1 demo版本增加lbbAI网站
0.1.2 demo版本删除lbbAI网站，因为无法使用
0.1.3 修复BUG
1.0 加入关于模块，更新网站aitianhu.top；修复“退出”按钮
的问题
1.0.1 修复BUG：移除“检查文件完整度”程序使用
（可以在github仓库的old文件夹里面看；修复其他BUG......
1.1 修复BUG;紧急修复Windows7无法使用情况!；重新修正UI界面
1.1.1 更新chatGPT网站;修改update文本显示设置

当前版本:1.1 (Not beta or demo)'''

text_box = ScrolledText(root)
text_box.pack(fill=BOTH, expand=1)
text_box.insert(END, text)
text_box.configure(state='disabled')


# Button
quit_bt = Button(root, text='返回', command=quit_exe).pack()

# mainloop
root.title('更新日志')
root.geometry('355x250+400+400')
root.mainloop()
