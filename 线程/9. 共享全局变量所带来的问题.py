# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:49 下午
# @Author  : 顾安
# @File    : 9. 共享全局变量所带来的问题.py
# @Software: PyCharm


import time
import threading

g_num = 0


def test_1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(f'test_1中的g_num = {g_num}')


def test_2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(f'test_2中的g_num = {g_num}')


def main():
    t1 = threading.Thread(target=test_1, args=(1000000,))
    t2 = threading.Thread(target=test_2, args=(1000000,))

    t1.start()
    t2.start()

    print(f'主线程获取全局变量值为: {g_num}')


if __name__ == '__main__':
    main()

'''
线程1在去执行计算时得出的结果没有来得及赋值就进行了任务切换
会导致计算结果错误

如何解决？
    互斥锁
'''
