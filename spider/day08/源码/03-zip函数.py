#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-zip函数.py    
# Author :   柏汌  

a = [1, 2, 3, 4]
b = [6, 7, 8, 9, 10]
c = [6, 7, 8, 9, 10]
for x, y, z in zip(a, b, c):
    print(x)
    print(y)
    print(z)

