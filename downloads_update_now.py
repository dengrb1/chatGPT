import requests
import json
import os
from tqdm import tqdm
import threading
from time import sleep


print('在使用在线更新时，请安装steam++加速github才可以加速下载')
sleep(1)

url = 'https://api.github.com/repos/dengrb1/chatgpt/releases/latest'

response = requests.get(url, headers={'Accept': 'application/vnd.github.v3+json'})
release_info = json.loads(response.text)

new_version = release_info['tag_name']
current_version = '1.3' # 修改为你的已有版本号

if new_version != current_version:
    print('发现新版本: {}'.format(new_version))
    print('准备更新')

    # 下载最新程序并保存到本地
    download_url = release_info['assets'][0]['browser_download_url']  # 假设发布包第一个asset为我们要下载的程序
    file_name = download_url.split('/')[-1]
    file_path = os.path.join(os.getcwd(), file_name)

    print('开始下载：{}'.format(file_name))
    response = requests.get(download_url, stream=True)
    content_size = int(response.headers['Content-Length'])

    def write_data(start, end, url, file_path):
        headers = {'Range': f'bytes={start}-{end}', 'Accept-Encoding': None}
        res = requests.get(url, headers=headers, stream=True)
        with open(file_path, 'rb+') as f:
            f.seek(start)
            var = f.tell()
            f.write(res.content)

    thread_num = 10
    threads = []
    step = content_size // thread_num
    for i in range(thread_num):
        start = step * i
        if i == thread_num -1:
            end = content_size - 1
        else:
            end = (i+1) * step - 1
        t = threading.Thread(target=write_data, kwargs={"start": start, "end": end, "url": download_url, "file_path": file_path})
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print('下载完成！')
    # 打开更新程序
    os.startfile(file_path)
else:
    print('当前已是最新版本')
