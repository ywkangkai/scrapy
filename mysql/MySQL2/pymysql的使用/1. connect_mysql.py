# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 9:57 下午
# @Author  : 顾安
# @File    : 1. connect_mysql.py
# @Software: PyCharm

# pip install pymysql -i https://pypi.douban.com/simple

# 数据库连接
import pymysql


def db_connect():
    # 1. 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    # 2. 创建游标对象 使用游标对象进行数据的增啥改查
    cursor = db.cursor()
    # 3. 是用游标对象进行sql查询
    cursor.execute('select now()')
    # 4. 获取数据
    data = cursor.fetchone()  # fetchone() 返回值类型为一个元组
    print(data)
    # 5. 打印数据
    print(f'当前时间为: {data[0]}')
    # 6. 关闭连接
    cursor.close()


if __name__ == '__main__':
    db_connect()
