# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 8:34 下午
# @Author  : 顾安
# @File    : 12.create_task对象的返回值.py
# @Software: PyCharm


import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '这是一个返回值'


async def main():
    print('开始任务...')
    # 创建task对象，将当前的func任务添加到事件循环中
    task_list = [
        # 在创建task对象时, 可以在task内部给协程对象取别名: name=别名名称
        # 当前name参数必须在python3.8及以上版本使用
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]
    print('任务结束...')
    # await 关键字之后只能连接可以等待的对象 列表不能在await之后
    # await task_list
    done, pending = await asyncio.wait(task_list, timeout=None)
    '''
    done: 接收协程函数所返回的值
    pending: 如果设置超时时间, 则接收在超时时间内没有执行完毕的函数的状态

    一般情况下不会使用pending参数
    '''
    print(done)  # 返回的类型为一个集合

    for item in done:
        print(item.result())


asyncio.run(main())

'''
done
    await asyncio.wait(task_list, timeout=None) 所返回的值
    
    asyncio.wait 会返回一个元组
        当前这个元组的一个值为协程函数中的返回
        第二个元素为在规定时间内没有执行完毕的函数的状态
        
'''
