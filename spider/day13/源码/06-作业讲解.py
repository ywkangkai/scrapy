# _*_ CODING:UTF-8 _*_
# @Author    : icecold
# @time      :  22:46
# @File      : day5-存储2作业.py
# @Software  : PyCharm
import requests
import pymysql
from lxml import etree


class Qq(object):
    def __init__(self):
        # 拿到套接字对象
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='spiders')
        # 拿到游标 mysql>
        self.cursor = self.db.cursor()
        self.url = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=tv&feature=7&iarea=814&listpage=1&offset=30&pagesize=30'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        # response = requests.get(url, headers=headers)
        # response.encoding = 'utf-8'
        # print(response.text)

    def create_table(self):
        sql = '''
                        CREATE TABLE IF NOT EXISTS qq(
                            id int primary key auto_increment not null,
                            title VARCHAR(255) NOT NULL,
                            figure_caption VARCHAR(255) NOT NULL,
                            info VARCHAR(255) NOT NULL,
                            descr TEXT)
        '''
        try:
            self.cursor.execute(sql)
            print('CREATE TABLE SUCCESS!')
        except Exception as e:
            print(f'CREATE TABLE FAILED,CASE:{e}')

    def get_data(self, page):
        data = {
            'append': '1',
            'channel': 'tv',
            'feature': '7',
            'iarea': '814',
            'listpage': '2',
            'offset': {page},
            'pagesize': '30'
        }

        res = requests.get(self.url, headers=self.headers, data=data)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        return html

    def parase_data(self, html):
        count = len(html.xpath('//div[@class="list_item"]/a/@title'))
        # i = 0
        div_list = html.xpath('//div[@class="list_item"]')
        for i in div_list:
            # print(i.tosting())
            title = i.xpath('./a/@title')[0] if i.xpath('./a/@title') else None
            figure_caption = i.xpath('./a/div/text()')[0] if i.xpath('./a/div/text()')  else None
            descr = i.xpath('./div/div[@class="figure_desc"]/text()')[0] if i.xpath('./div/div[@class="figure_desc"]/text()') else None
            info = i.xpath('./a/@href')[0] if i.xpath('./a/@href') else None
            # i += 1
            # title = str(title)
            # figure_caption = str(figure_caption)
            # descr = str(descr)
            # info = str(info)
            print(title, figure_caption, info, descr)
            # self.save_data(title, figure_caption, info, descr)

    def save_data(self, title, figure_caption, info, descr):
        #sql 插入
        sql = 'insert into qq(id, title, figure_caption, info, descr) values(%s, %s, %s, %s, %s)'
        try:
            self.cursor.execute(sql, (0, title, figure_caption, info, descr))
            self.db.commit()
            print('数据插入成功!')
        except Exception as e:
            print('数据插入失败！')
            self.db.rollback()
            print(e)

    # 资源回收
    def recycle(self):
        # 关闭游标连接# 相当与exit，关闭mysql
        self.cursor.close()
        # 关闭数据库连接# 回收资源
        self.db.close()


    def main(self):
        self.create_table()
        for i in range(1, 20):
            page = i*30
            res = self.get_data(page)
            print(res)
            self.parase_data(res)
        # self.recycle()


if __name__ == '__main__':
    qq = Qq()
    qq.main()