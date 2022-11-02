#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-页面滚动.py    
# Author :   柏汌  


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get('https://www.icswb.com/channel-list-channel-161.html')
# drive.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 相对坐标滚动
# drive.execute_script('window.scrollBy(0, 700)')
# #  移动到 1500的位置
# drive.execute_script('window.scrollBy(0, 800)')

# 绝对坐标

# drive.execute_script('window.scrollTo(0, 800)')
# drive.execute_script('window.scrollTo(0, 1600)')
