# -*- coding: utf-8 -*-
# @Time    : 2022/8/26 9:04 下午
# @Author  : 顾安
# @File    : 4. 进程之间不共享全局变量.py
# @Software: PyCharm


import os
import time
from multiprocessing import Process

nums = [11, 22]


def work_1():
    print('子进程_1 获取到的初始列表的元素: ', nums)
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print('子进程_1 获取到的添加后的列表的元素: ', nums)


def work_2():
    print('子进程_2 获取到的全局列表的元素: ', nums)


if __name__ == '__main__':
    p_1 = Process(target=work_1)
    p_1.start()
    # 等待子进程_1任务完成

    p_2 = Process(target=work_2)
    time.sleep(4)
    p_2.start()

