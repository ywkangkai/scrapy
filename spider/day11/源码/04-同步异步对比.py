#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-同步异步对比.py    
# Author :   柏汌  

# import time
# import requests
# def main():
#     for i in range(30):
#         res = requests.get('https://www.baidu.com')
#         print(f'第{i + 1}次请求，status_code = {res.status_code}')
#
# if __name__ == '__main__':
#     start = time.time()
#     main()
#     end = time.time()
#     print(f'同步发送30次请求，耗时：{end - start}')


# 异步

import asyncio
import aiohttp
import time


async def requests_data(client, i):
    res = await client.get('https://www.baidu.com')
    print('第{}次请求'.format(i))
    return res

async def main():
    # aiohttp.ClientSession 类似于requests的session()
    async with aiohttp.ClientSession() as client:
        task_list = []
        for i in range(30):
            # 获取的是协程对象
            res = requests_data(client, i)
            # 创建成task对象 让事件循环可以判断当前是否是一个可执行对象
            task = asyncio.create_task(res)
            task_list.append(task)
            # 直接执行异步对象任务  会阻塞
            # await requests_data(client, i)
        # 等待执行的异步   将task交由event_loop来进行控制
        await asyncio.wait(task_list)


if __name__ == '__main__':
    t1 = time.time()
    # 开启事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('耗费的时间是：', time.time() - t1)










