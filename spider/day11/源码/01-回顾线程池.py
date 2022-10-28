#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-回顾线程池.py    
# Author :   柏汌  


from concurrent.futures import ThreadPoolExecutor
import threading


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# print(action(50))
# 创建一个包含两个线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
futrue = pool.submit(action, 50)
print(futrue.result())
futrue2 = pool.submit(action, 100)
# 判断是否执行结束
print(futrue2.result())
# print(futrue.done())

pool.shutdown()

















