# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:50 下午
# @Author  : 顾安
# @File    : run_go_python.py
# @Software: PyCharm


from ctypes import cdll


main = cdll.LoadLibrary('./main.so')
result = main.Add(2, 3)
print(result)
