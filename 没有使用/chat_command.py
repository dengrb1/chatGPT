import openai
import os
from time import sleep
import sys

ml = os.getcwd()
file_path = os.path.join(ml, "api_key.txt")

# 设置openai库的API认证密钥
def api_key():
    if os.path.exists(os.path.join(ml, f"api_key.txt")):
        with open(file_path, 'r') as f:
            openai.api_key = f.read().strip()
    else:
        print('文件丢失，请重新输入api_key')
        sleep(1)
        if os.path.exists(os.path.join(ml, "chat_command_GUI.exe")):
            os.startfile("chat_command_GUI.exe")
        else:
            print('错误，文件不存在!?')
            sleep(1)
            sys.exit()
    pass


# 设置GPT-3.5模型要使用的API_key
api_key()

# 设置GPT-3.5模型的引擎ID
model_engine = 'text-davinci-003'

# 循环读入用户输入并输出聊天结果
while True:
    # 获取用户输入
    prompt = input("你好，请问有什么需要帮助的吗？\n")
    
    # 调用openai.ChatCompletion.create()方法来获取聊天结果
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=210,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response['choices'][0]['text'].strip()
    print(f"chatGPT：{result}")
