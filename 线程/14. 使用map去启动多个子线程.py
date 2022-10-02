# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:38 下午
# @Author  : 顾安
# @File    : 14. 使用map去启动多个子线程.py
# @Software: PyCharm


from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(action, (50, 100, 150))
    print('--------------')
    for r in results:
        print(r)


'''
为什么python线程在同一时间内只能运行一个线程？
    GIL
    
    限制了程序线程的数量
    
    c java
'''