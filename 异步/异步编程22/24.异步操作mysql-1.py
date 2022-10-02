# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 10:20 下午
# @Author  : 顾安
# @File    : 24.异步操作mysql-1.py
# @Software: PyCharm


import asyncio
import aiomysql


async def execute():
    # 网络IO操作 连接mysql
    conn = await aiomysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='python_test_1')

    # 网络IO操作 创建游标
    cursor = await conn.cursor()

    # 网络IO操作 执行sql
    await cursor.execute('select * from students')

    # 网络IO操作 获取sql结果
    result = await cursor.fetchall()
    print(result)

    # 网络IO操作
    await cursor.close()
    conn.close()


asyncio.run(execute())
