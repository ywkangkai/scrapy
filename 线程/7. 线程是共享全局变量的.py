# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:36 下午
# @Author  : 顾安
# @File    : 7. 线程是共享全局变量的.py
# @Software: PyCharm


import threading

g_num = 100


def test_1():
    global g_num
    g_num += 1
    print(f'当前全局变量值为: {g_num}')


def test_2():
    print(f'当前全局变量为: {g_num}')


def main():
    t1 = threading.Thread(target=test_1)
    t2 = threading.Thread(target=test_2)

    t1.start()
    t2.start()
    print(f'在主线程中获取全局变量的值: {g_num}')


if __name__ == '__main__':
    main()
    # 在多线程中 全局变量是可以被多个线程共享获取的
