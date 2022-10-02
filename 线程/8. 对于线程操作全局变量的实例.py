# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:41 下午
# @Author  : 顾安
# @File    : 8. 对于线程操作全局变量的实例.py
# @Software: PyCharm


import time
import threading

g_nums = [11, 22]


def test_1(list_data):
    list_data.append(33)


def test_2(list_data):
    print(f'当前全局列表中的值为: {list_data}')


def main():
    t1 = threading.Thread(target=test_1, args=(g_nums,))
    t2 = threading.Thread(target=test_2, args=(g_nums,))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print(f'主线程获取的全局列表的值为: {g_nums}')


# 如果是windows电脑 必须写函数入口 否则线程启动失败
if __name__ == '__main__':
    main()
