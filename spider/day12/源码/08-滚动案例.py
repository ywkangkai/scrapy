#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   08-滚动案例.py    
# Author :   柏汌  


from selenium import webdriver
import time
import random

browser = webdriver.Chrome()
browser.get('https://36kr.com/')

for i in range(1, 10):
    time.sleep(random.randint(100, 300) / 1000)
    browser.execute_script(f'window.scrollTo({30 * i},document.body.scrollHeight * {i/9})')


