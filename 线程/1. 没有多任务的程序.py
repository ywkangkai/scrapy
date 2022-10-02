# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 8:25 下午
# @Author  : 顾安
# @File    : 1. 没有多任务的程序.py
# @Software: PyCharm


import time


def sing():
    for i in range(5):
        print('正在唱歌...')
        # 可以通过time.sleep方法让程序休眠 暂停
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞...')
        time.sleep(1)


def main():
    sing()
    dance()


if __name__ == '__main__':
    main()
    """
    当前程序为单线程程序
        如果你先执行了sing()函数
            那么就必须等sing()执行完毕之后 才能执行dance()函数
    """
