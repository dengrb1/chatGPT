import requests
import json
import os

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
    response = requests.get(download_url)
    with open(file_path, 'wb') as f:
        f.write(response.content)
        print('下载完成！')
        # 打开更新程序
        os.startfile(file_path)
else:
    print('当前已是最新版本')