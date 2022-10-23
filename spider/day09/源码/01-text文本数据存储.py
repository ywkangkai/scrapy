#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-text文本数据存储.py    
# Author :   柏汌  

# 获取到知乎发现里的问题
#
# 	网址：https://www.zhihu.com/explore
import requests
from bs4 import BeautifulSoup


# # 获取到资源地址
# url = 'https://www.zhihu.com/explore'
# # 伪装请求头
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'lxml')
# title_list = soup.select('div .css-1g4zjtl a')
# # print(title_list)
# for title in title_list:
#     print(title.get_text())
with open(r'D:\spider_vip\day05\data.txt', 'a+', encoding='utf-8')as f:
    # f.write(title.get_text() + '\n')
    data = f.readline()

print(data)