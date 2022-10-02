# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:24 下午
# @Author  : 顾安
# @File    : 5. 关于线程的创建时间.py
# @Software: PyCharm


import time
import threading


def test():
    for i in range(10):
        print('test')
        time.sleep(1)


def main():
    print('主线程运行时的线程信息: ', threading.enumerate())
    # 创建线程对象并不回产生线程  线程对象只是一个对象
    t = threading.Thread(target=test)
    print('线程对象创建后的线程信息: ', threading.enumerate())
    t.start()
    print('子线程运行之后的线程信息: ', threading.enumerate())


if __name__ == '__main__':
    main()
