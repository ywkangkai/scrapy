# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:06 下午
# @Author  : 顾安
# @File    : 4. 查看当前程序的线程数量.py
# @Software: PyCharm

import time
import threading


def test1():
    for i in range(5):
        print('test1')
        time.sleep(1)


def test2():
    for i in range(5):
        print('test2')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    # 如果在线程实例对象运行之后调用了join方法 则主线程等待这两个子线程执行完毕之后再执行
    print(len(threading.enumerate()))


if __name__ == '__main__':
    main()
