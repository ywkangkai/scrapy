#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-mysql案例.py    
# Author :   柏汌  

# 要求：获取到百度招聘的数据信息
#
# 	网址：https://talent.baidu.com/jobs/social-list?search=
import requests
import pymysql


class Baidu(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='spiders')
        self.cursor = self.db.cursor()
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            # 'Cookie': 'BIDUPSID=9773AB57EF3AA57A2DB251475FC4301E; PSTM=1666078227; BAIDUID=9773AB57EF3AA57A99794F473F717CCC:FG=1; H_PS_PSSID=36547_37584_37299_36884_36804_36786_37498_26350_37479_37372_37464; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-158%3A; BAIDUID_BFESS=9773AB57EF3AA57A99794F473F717CCC:FG=1; ZFY=kiThmYN4TwRPhBKRV0srReGjYwWM8TukGWR:AMUDqdiU:C; delPer=0; log_chanel=ps; log_first_time=1666091290875; log_last_time=1666091290875; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1666167198; PSINO=7; BA_HECTOR=05a40l84ag0l2g04a5a53bqp1hkven01a; Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1666187091',
            # 'Host': 'talent.baidu.com',
            # 'Origin': 'https://talent.baidu.com',
            # 'Pragma': 'no-cache',
            'Referer': 'https://talent.baidu.com/jobs/social-list?search=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }

    def create_table(self):
        # 使用预处理语句创建表
        sql = '''
                            CREATE TABLE IF NOT EXISTS baidu(
                                id int primary key auto_increment not null,
                                education VARCHAR(255) NOT NULL, 
                                name VARCHAR(255) NOT NULL, 
                                serviceCondition TEXT)
                            '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")

    def get_data(self, page):
        data = {
            'recruitType':'SOCIAL',
            'pageSize':'10',
            'keyWord':'python',
            'curPage':page,
            'projectType':'',
        }
        response = requests.post(url=self.url, headers=self.headers, data=data)
        return response.json()

    def parase_data(self, data):
        data_list = data['data']['list']
        for node in data_list:
            # print(node)
            education = node['education'] if node['education'] else '空'
            name = node['name']
            serviceCondition = node['serviceCondition']
            self.save_data(education, name, serviceCondition)


    def save_data(self, education, name, serviceCondition):
        # sql 插入语法
        sql = 'insert into baidu(id, education, name, serviceCondition) values(%s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (0, education, name, serviceCondition))
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print('数据插入失败')
            self.db.rollback()




    def run(self):
        self.create_table()
        for i in range(1, 10):
            response = self.get_data(i)
            self.parase_data(response)




if __name__ == '__main__':
    bd = Baidu()
    bd.run()


