import openai
import os
from time import sleep
import sys

ml = os.getcwd()
file_path = os.path.join(ml, "api_key.txt")

# 设置openai库的API认证密钥
def api_key():
    input1 = input("请输入API_key:")
    if input1 == None:
        print('error: Not input')
        sleep(4)
        sys.exit()
    else:
        openai.api_key = input1

# 设置GPT-3.5模型的引擎ID
model_engine = 'text-davinci-003'

# 循环读入用户输入并输出聊天结果
def input_print():
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

if __name__  == "__main__":
    print('注意，本程序是测试程序，如有问题，非常正常')
    sleep(2)
    api_key()
    # 设置GPT-3.5模型的引擎ID
    model_engine = 'text-davinci-003'
    input_print()