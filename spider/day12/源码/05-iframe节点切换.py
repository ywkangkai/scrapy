#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-iframe节点切换.py    
# Author :   柏汌  


from selenium import webdriver
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get('https://www.douban.com/')
iframe = drive.find_element(By.XPATH, '//div[@class="login"]/iframe')
drive.switch_to.frame(iframe)

drive.find_element(By.NAME, 'phone').send_keys('12334453')

