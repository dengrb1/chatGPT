"""基本上，这个文件都是已经提前写好了下一个版本的内容的
之后几天基本上都会发布最新版本的内容的"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webbrowser
import os
import json
import requests
from tkinter import messagebox

root = Tk()
ml = os.getcwd()

def quit_exe():
    root.destroy()
def update_now():
    webbrowser.open("https://kgithub.com/dengrb1/chatgpt/releases/")
    messagebox.showinfo('update', '请选择最新版本并下载运行安装程序，然后就可以更新了！')
'''def downloads_update_now():
    if os.path.exists(os.path.join(ml, "downloads_update_now.exe")):
        os.startfile("downloads_update_now")

    else:
        messagebox.showerror(':( error','在线更新模块错误：文件不存在')
'''


# Label
update_now_bt = Button(root ,text='在线更新', command=update_now).pack(side=RIGHT)
quit_bt = Button(root, text='返回', command=quit_exe).pack(side=RIGHT)
Label(root, text='更新日志').pack()
text = '''
当前版本:1.3 (Not beta or demo)


1.3 加入aiyunos、free2gpt、chatkey网站；删除qdymys、extkj等网站；加入在程序内
访问官网，加入cmd版本的chatGPT(测试版);修复一些很明显的BUG

1.2 增加lbbai网站；修复BUG;完全移除“关于”模块......

1.1.1 更新chatGPT网站;修改update文本显示设置。新增bnu120聊天网站
1.1 修复BUG;紧急修复Windows7无法使用情况!；重新修正UI界面

1.0.1 修复BUG：移除“检查文件完整度”程序使用
1.0 加入关于模块，更新网站aitianhu.top；修复“退出”按钮
的问题

0.1.3 修复BUG
0.1.2 demo版本删除lbbAI网站，因为无法使用
0.1.1 demo版本增加lbbAI网站
0.1 DEMO制作完成
'''

text_box = ScrolledText(root)
text_box.pack(fill=BOTH, expand=1)
text_box.insert(END, text)
text_box.configure(state='disabled')


# Button
quit_bt = Button(root, text='返回', command=quit_exe).pack()
update_now_bt = Button(root, text='在线更新', command=update_now).pack()

# mainloop
root.title('更新日志')
root.geometry('355x250+400+400')
root.mainloop()
