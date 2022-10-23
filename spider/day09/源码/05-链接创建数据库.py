#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-链接创建数据库.py    
# Author :   柏汌  

import pymysql

def db_connect():
    # 链接数据库
    db = pymysql.connect(host='localhost', user='root', password='root')
    # 创建游标
    cursor = db.cursor()
    cursor.execute('select version()')
    data = cursor.fetchall()
    print(data)
    # 创建数据库
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
    db.close()


def main():
    db_connect()


if __name__ == '__main__':
    main()


