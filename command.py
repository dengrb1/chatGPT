import os
from time import sleep

def run_cmd():
    print("正在启动")
    sleep(0.5)
    for i in range(3):
        os.system("start powershell")
        pass
    pass

sleep(0.2)
run_cmd()
