#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-csv表格操作.py    
# Author :   柏汌  

import csv
# with open('data.csv', 'w', newline='')as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


# 字典写入

# with open('data.csv', 'w')as csvf:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvf, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'name': 'Mike', 'age': 20, 'id': '10001'})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

with open('data.csv','w')as f:
    f.write('{},{},{}'.format('aa', 'bb', 'cc'))

