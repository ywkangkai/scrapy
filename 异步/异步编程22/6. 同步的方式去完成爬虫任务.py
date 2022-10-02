# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:18 下午
# @Author  : 顾安
# @File    : 6. 同步的方式去完成爬虫任务.py
# @Software: PyCharm

# pip install requests
import requests


def download_image(url):
    print('开始下载: ', url)
    response = requests.get(url)
    print('下载完成...')

    # 保存图片
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode='wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_list = [
        'http://pic.bizhi360.com/bbpic/98/10798.jpg',
        'http://pic.bizhi360.com/bbpic/92/10792.jpg',
        'http://pic.bizhi360.com/bbpic/86/10386.jpg'
    ]
    for item in url_list:
        download_image(item)
