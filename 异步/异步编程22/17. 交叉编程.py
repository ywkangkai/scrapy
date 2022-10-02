# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:34 下午
# @Author  : 顾安
# @File    : 17. 交叉编程.py
# @Software: PyCharm


import time
import asyncio
import concurrent.futures


def func_1():
    time.sleep(2)
    return '测试'


async def main():
    loop = asyncio.get_running_loop()

    # 在协程函数中运行普通函数 在执行函数时，协程内部会自动创建一个线程池来运行任务
    # run_in_executor()方法第一个参数为None时则默认创建一个线程池
    fut = loop.run_in_executor(None, func_1)
    result = await fut
    print('当前方式会自动创建一个线程池去执行普通函数: ', result)

    # 在协程函数中运行基于线程池的任务, 效果与以上代码一致
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func_1)
        print('在线程池中得到的执行结果: ', result)

    # 在协程函数中运行基于进程池的任务
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func_1)
        print('在进程池中得到的执行结果: ', result)


if __name__ == "__main__":
    asyncio.run(main())
