#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-王者荣耀皮肤采集.py    
# Author :   柏汌
import os

import aiohttp
import time
import asyncio


class Crawl_img():
    def __init__(self):
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        self.url = "https://pvp.qq.com/web201605/js/herolist.json"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

    async def img_get(self, session, ename, cname):
        for i in range(1, 10):
            response = await session.get(url=self.skin_url.format(ename, ename, i))
            if response.status == 200:
                # read 获取进制数据
                content = await response.read()
                with open('图片/' + cname + '-' + str(i) + '.jpg', 'wb')as f:
                    f.write(content)
                print('正在下载{}第{}张'.format(cname, i))
            else:
                break


    async def run(self):
        async with aiohttp.ClientSession()as session:
            response = await session.get(self.url, headers=self.headers)
            wzry_data = await response.json(content_type=None)
            tasks = []
            for i in wzry_data:
                ename = i['ename']
                cname = i['cname']
                res = self.img_get(session, ename, cname)
                task = asyncio.create_task(res)
                tasks.append(task)
            await asyncio.wait(tasks)


if __name__ == '__main__':
    if not os.path.exists('图片'):
        os.mkdir('图片')
    wzry = Crawl_img()

    loop = asyncio.get_event_loop()
    # 執行协程任务
    loop.run_until_complete(wzry.run())