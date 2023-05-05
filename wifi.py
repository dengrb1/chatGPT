import socket
from time import sleep
import os
import platform
import sys


def is_connected():
    try:
        # 使用百度的IP地址进行连接测试
        socket.create_connection(("www.baidu.com", 80))
        return True
    except OSError:
        pass
    return False
def open_exe(exe_name):
    ml = os.getcwd()
    if os.path.exists(ml, f"{exe_name}.exe"):
        os.system(f"start {exe_name}.exe")
    else:
        pass
    pass


# mainloop
print('正在启动检测程序...')
s = platform.system()
sleep(0.22222)
if s == "Windows":
    pass
else:
    print("无法启动，不是Windows系统！！")
    sleep(1)
    sys.exit()
if is_connected():
    print("网络已连接，正在启动主程序!!")
    sleep(0.33)
    open_exe('client')
else:
    print("网络未连接,是否继续使用？")
    input_xz = str(input("选择:1.是 2.不是(必须选择数字)"))
    if input_xz == None:
        print("没有输入")
        sleep(0.5)
        print("默认退出")
        sleep(0.6)
        sys.exit()
        pass
    elif input_xz != '1' or '2':
        print("请输入数字！！")
        pass
    elif input_xz == '1':
        open_exe('client')
    elif input_xz == '2':
        sleep(0.4)
        sys.exit()
