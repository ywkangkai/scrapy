# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 10:20 下午
# @Author  : 顾安
# @File    : 3. insert_data.py
# @Software: PyCharm


import pymysql
import datetime


def insert_record():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()

    # 数据插入语句
    create_time = datetime.datetime.now()
    sql = "insert into employee (first_name, last_name, age, sex, income, create_time) values" \
          "('%s', '%s', %d, '%s', %.2f, '%s')" % ('顾', '安', 22, '男', 3011.88, datetime.datetime.now())

    try:
        cursor.execute(sql)
        db.commit()
        print('数据插入成功...')
    except Exception as e:
        print('数据插入失败: ', e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    insert_record()
