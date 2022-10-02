# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 10:08 下午
# @Author  : 顾安
# @File    : 2. create_table.py
# @Software: PyCharm


import pymysql


def create_table():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()
    # 创建一个员工表
    cursor.execute("drop table if exists employee")

    # 编辑创建表的sql
    sql = """
        create table employee (
            first_name varchar(20) not null,
            last_name varchar(20),
            age int,
            sex varchar(1),
            income decimal(6, 2),
            create_time datetime
        );
    """

    # 执行创表语句
    try:
        cursor.execute(sql)
        print('表创建成功...')
    except Exception as e:
        print('创建表失败: ', e)
        # 如果创建失败使用回滚
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    create_table()
