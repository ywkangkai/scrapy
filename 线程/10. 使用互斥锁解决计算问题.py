# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:03 下午
# @Author  : 顾安
# @File    : 10. 使用互斥锁解决计算问题.py
# @Software: PyCharm


"""
之前的计算错误问题是因为计算步骤缺失导致了计算误差
所以只要保证计算步骤都完整性就可以解决问题
"""

import time
import threading

g_num = 0
# 声明一个互斥锁
mutex = threading.Lock()


def test_1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 在代码中调用acquire代表上锁
        g_num += 1
        mutex.release()  # 在代码中调用release代表释放锁
    print(f'test_1中的g_num = {g_num}')


def test_2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print(f'test_2中的g_num = {g_num}')


def main():
    t1 = threading.Thread(target=test_1, args=(1000000,))
    t2 = threading.Thread(target=test_2, args=(1000000,))

    t1.start()
    t2.start()
    time.sleep(1)
    print(f'主线程获取的全局列表的值为: {g_num}')


if __name__ == '__main__':
    main()
