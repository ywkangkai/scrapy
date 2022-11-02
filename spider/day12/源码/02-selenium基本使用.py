#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-selenium基本使用.py    
# Author :   柏汌  

# selenium3   selenuim4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 打开指定的浏览器
browser = webdriver.Chrome()
# 指定访问的页面
browser.get('https://www.baidu.com')
# 选择文本输入框  然后输入问题  当前方法已经弃用
# browser.find_element_by_id('kw').send_keys('python')
# 选中文本输入框   输入数据
browser.find_element(By.ID, 'kw').send_keys('selenium')
# 获取到id属性为su的标签  然后点击
browser.find_element(By.ID, 'su').click()
# 提取页面源代码
print(browser.page_source)

# 提取cookie
print(browser.get_cookies())
# 获取当前的截屏
# print()
browser.get_screenshot_as_file('123.png')

print(browser.current_url)

time.sleep(3)
browser.quit()
