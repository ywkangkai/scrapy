# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 10:26 下午
# @Author  : 顾安
# @File    : 异步操作mysql-2.py
# @Software: PyCharm


import asyncio
import aiomysql


async def execute(host, password):
    print('开始连接:', host)
    # 网络IO操作 连接mysql
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='python_test_1')

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
    print('结束:', host)


task_list = [
    execute('localhost', 'root'),
    execute('localhost', 'root')
]


asyncio.run(asyncio.wait(task_list))


'''
现在通过网络请求一张图片的数据
将图片数据写入到本地变成一张图片

    1.在读取图片数据时需不需要花费时间？
    2.在写入图片数据时需不需要等图片数据全部获取到？
    
    哪怕是异步也无法完成，因为数据都没有请求到你怎么写？
    
    在写图片的时候我必须要等待
        那么在等待的这个期间 我能不能再发送下一张图片的请求？
            其他的事情就是进行网络请求图片数据
            
            
            写一张图片要3秒
            
            发送一个网络请求数据1秒
            
            在等待的这个期间我能不能发送三个链接？
            
            回来的数据有三条
            并且是切换获取的
            
            await的原因
                等待是一个
                任务切换
                    await只要有检测到有堵塞的情况 则让asyncio去检查事件循环中有没有可以执行的任务
                    
'''
