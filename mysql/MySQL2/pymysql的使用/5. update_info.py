# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 8:17 下午
# @Author  : 顾安
# @File    : 5. update_info.py
# @Software: PyCharm


import pymysql


def update_table():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()

    # 对当前数据进行更新
    sql = "update employee set age=age+1 where sex='%s'" % '男'

    try:
        cursor.execute(sql)
        db.commit()
        print('数据更新成功...')
    except Exception as e:
        print('数据更新失败:', e)
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    update_table()
