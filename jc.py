import os
from time import sleep


file_error = '文件丢失，请检查目录文件完整度'
ml = os.getcwd
maths = 0
error = 0


def file_jx(exe_name):
    maths += 1
    if os.path.exists(os.path.join(ml, f"{exe_name}")):
        pass
    else:
        error += 1
    pass

def extkj():
    file_jx("extkj")

def wuguokai():
    file_jx("wuguokai")

def f1():
    file_jx("aiyunos")

def update():
    if os.path.exists(os.path.join(ml, "update.exe")):
        maths += 1
        print(f'文件{maths}正常存在')
    else:
        error += 1
        print(f"丢失{error}文件")
        pass
    pass

def gk():
    file_jx("gk")


# mainloop
print('检查中')
sleep(0.85555)

extkj()
wuguokai()
f1()
update()
gk()

sleep(0.5)
print('检查完成，共有{maths}个文件正常,{error}个文件丢失')

if str(input('是否退出？（Y.是 B.不是')) == "Y" or 'y' or '1':
    exit()
else:
    print('请手动退出')
    while True:
        sleep(1)
        pass
    