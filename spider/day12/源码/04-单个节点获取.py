#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-单个节点获取.py    
# Author :   柏汌  


# from selenium import webdriver
from selenium.webdriver.common.by import By
#
# from selenium.webdriver.common.keys import Keys  # 模拟键盘操作
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# s = browser.find_element(By.NAME, 'wd')
# s.send_keys('衣服')
# s.send_keys(Keys.ENTER)

# 多节点
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.icswb.com/channel-list-channel-161.html')
lis = browser.find_element(By.CSS_SELECTOR,'#NewsListContainer li')

print(lis)

