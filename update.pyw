"""基本上，这个文件都是已经提前写好了下一个版本的内容的
之后几天基本上都会发布最新版本的内容的"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webbrowser

root = Tk()

def quit_exe():
    root.destroy()
def update_now():
    webbrowser.open("https://kgithub.com/dengrb1/chatgpt/releases/")
    messagebox.showinfo('update', '请选择最新版本并下载运行安装程序，然后就可以更新了！')

# Label
update_now_bt = Button(root ,text='在线更新', command=update_now).pack(side=RIGHT)
quit_bt = Button(root, text='返回', command=quit_exe).pack(side=RIGHT)
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
1.1.1 更新chatGPT网站;修改update文本显示设置。新增bnu120聊天网站
移除lbbai网站入口
1.2 加入网络检测和更好的操作界面

当前版本:1.2 (Not beta or demo)'''

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
