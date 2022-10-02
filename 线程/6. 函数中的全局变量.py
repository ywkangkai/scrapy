# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:33 下午
# @Author  : 顾安
# @File    : 6. 函数中的全局变量.py
# @Software: PyCharm


num = 100
list_data = [11, 22]


def test_1():
    global num
    num += 100


def test_2():
    list_data.append(33)


print(num)
print(list_data)

test_1()
test_2()

print(num)
print(list_data)
