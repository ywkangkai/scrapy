# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 8:01 下午
# @Author  : 顾安
# @File    : 4. select_info.py
# @Software: PyCharm


import pymysql


def query_data():
    # 1. 数据库连接
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')

    # 2. 获取游标
    cursor = db.cursor()

    # 3. 查询当前工资收入大于1000元的员工信息
    sql = "select * from employee where income > %d" % 1000

    # 4. 通过pymysql去执行自定义的sql语句
    try:
        cursor.execute(sql)
        # 获取查询到的结果集
        results = cursor.fetchall()
        # result = cursor.fetchone()
        # print(result)
        # fetchall() 方法返回的是元组类型数据
        # print(results)
        for row in results:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            gender = row[3]
            income = row[4]
            create_time = row[5]
            print(
                f'first_name: {first_name}, last_name: {last_name}, age: {age}, gender: {gender}, income: {income}, '
                f'create_time: {create_time}')
    except Exception as e:
        print('查询错误:', e)
    finally:
        db.close()


if __name__ == '__main__':
    query_data()


'''
对于数据查询无需进行commit提交
'''