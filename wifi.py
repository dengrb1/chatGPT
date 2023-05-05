import socket
from time import sleep
import os


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
sleep(0.22222)

if is_connected():
    print("网络已连接，正在启动主程序!!")
    sleep(0.33)
    open_exe('client')
else:
    print("网络未连接,无法使用")
