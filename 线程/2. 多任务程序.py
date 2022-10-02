# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 8:30 下午
# @Author  : 顾安
# @File    : 2. 多任务程序.py
# @Software: PyCharm


# 让python完成多任务，需要使用python的内置包: threading
import time
import threading


def sing():
    for i in range(5):
        print('正在唱歌...')
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞...')
        time.sleep(1)


def main():
    # 1. 创建线程对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    """
    在实例化线程对象时, 需要指定当前创建的线程对象要运行什么任务？
        通过target参数去指定一个任务
    """
    # 2. 运行线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
