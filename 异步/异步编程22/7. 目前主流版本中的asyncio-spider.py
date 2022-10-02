# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 9:25 下午
# @Author  : 顾安
# @File    : 7. 目前主流版本中的asyncio-spider.py
# @Software: PyCharm


import aiohttp
import asyncio


async def download_image(session, url):
    print('发送请求: ', url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        print('下载完成...')
        with open(file_name, mode='wb') as f:
            f.write(content)


async def main():
    # 上下文管理器
    async with aiohttp.ClientSession() as session:
        url_list = [
            'http://pic.bizhi360.com/bbpic/98/10798.jpg',
            'http://pic.bizhi360.com/bbpic/92/10792.jpg',
            'http://pic.bizhi360.com/bbpic/86/10386.jpg'
        ]

        # 创建task对象 当前的这个task对象是写成运行的必备对象
        tasks = [asyncio.create_task(download_image(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())


'''
什么是协程对象
    就是协程函数() 所得到的对象被称之为协程对象
    普通方式不能执行协程函数
'''