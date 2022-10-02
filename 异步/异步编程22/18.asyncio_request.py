# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:42 下午
# @Author  : 顾安
# @File    : 18.asyncio_request.py
# @Software: PyCharm


import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动切换到其他任务）
    print('开始下载: ', url)

    loop = asyncio.get_event_loop()
    # requests 模块默认不支持异步操作，所以使用线程池来配合实现
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
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

    tasks = [download_image(url) for url in url_list]
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))

    # 事件循环发现是协程对象则自动创建task对象
    asyncio.run(asyncio.wait(tasks))
