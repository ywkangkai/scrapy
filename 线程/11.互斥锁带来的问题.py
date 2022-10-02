# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:18 下午
# @Author  : 顾安
# @File    : 11.互斥锁带来的问题.py
# @Software: PyCharm


# coding=utf-8
import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()


class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程 把mutexB上锁
        print(self.name + '----do1---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name + '----do1---down----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程 把mutexA上锁
        print(self.name + '----do2---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name + '----do2---down----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release()


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
