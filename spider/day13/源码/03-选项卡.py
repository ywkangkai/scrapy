#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-选项卡.py    
# Author :   柏汌  

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.baidu.com')
time.sleep(1)
# switch_to.window切换窗口
browser.switch_to.window(browser.window_handles[0])
browser.get('https://pic.netbian.com/4kmeinv/index.html')

time.sleep(3)
browser.quit()

