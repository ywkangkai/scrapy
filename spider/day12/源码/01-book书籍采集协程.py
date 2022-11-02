#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-book书籍采集协程.py    
# Author :   柏汌  

# 綫程池

import aiomysql
import asyncio
import aiohttp
import time


class Book_spider():
    def __init__(self):
        self.url = 'https://spa5.scrape.center/api/book/?limit=18&offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

    async def get_data(self, page, client, conn, cursor):
        response = await client.get(self.url.format(page * 18))
        json_data = await response.json()
        for data in json_data['results']:
            item = {}
            item['authors'] =','.join(''.join(x.strip() for x in i.strip().split('\n')) for i in data['authors'])
            item['score'] = data['score']
            item['title'] = data['name']
            print(item)
            await self.save_data(item, conn, cursor)

    async def save_data(self, item, conn, cursor):
        # sql插入语法
        sql = 'INSERT INTO books(id, authors, title, score) values(%s, %s, %s, %s)'
        try:
            print(item)
            await cursor.execute(sql, (0, item['authors'], item['title'], item['score']))
            await conn.commit()
        except Exception as e:
            print('插入失敗', e)
            await conn.rollback()


    async def main(self, loop):
        # 异步创建一个连接池
        loop = await aiomysql.create_pool(host='127.0.0.1', port=3306, user='root', password='root', db='spiders', loop=loop)
        async with loop.acquire()as conn:
            # 创建游标
            async with conn.cursor() as cursor:
                # 使用预处理语句创建表
                create_sql = '''
                           CREATE TABLE IF NOT EXISTS books(
                               id int primary key auto_increment not null,
                               authors VARCHAR(255) NOT NULL, 
                               title VARCHAR(255) NOT NULL, 
                               score VARCHAR(255) NOT NULL
                               );
                    '''
                await cursor.execute(create_sql)
                async with aiohttp.ClientSession()as session:
                    tasks = []
                    for i in range(1, 10):
                        res = self.get_data(i, session, conn, cursor)
                        tasks.append(asyncio.create_task(res))
                        await asyncio.sleep(0.2)
                    await asyncio.wait(tasks)
        loop.close()


if __name__ == '__main__':
    book = Book_spider()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(book.main(loop))
