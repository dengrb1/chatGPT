import openai
import re

# 定义用于与API交互的OpenAI API密钥
openai.api_key = str(input('请输入你的API key:'))

# 定义所需模型，这里使用Davinci，是GPT-3.5中的最大模型
model_engine = "davinci"

# 定义对话处理函数
def chat(prompt):
    # 调用GPT-3.5 API生成对话回复
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.7,  # 控制对话生成的创造力
        max_tokens=4000,  # 控制最多可输出的token数
        n=1,
        stop=None,
        timeout=30,
    )

    # 获取生成回复文本
    answer = response.choices[0].text

    # 对回复进行处理，去除一些特殊字符和回车符
    answer = re.sub('[^0-9a-zA-Z.,!?/:;\"\'\s]|(\r?\n)+', '', answer).strip()

    return answer

# 测试代码
while True:
    prompt = input("You: ")
    if prompt.lower() in ['bye', 'goodbye']:
        print("chatGPT: Goodbye!")
        break
    else:
        answer = chat(prompt)
        print("chatGPT:", answer)
