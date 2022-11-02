#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-selenium获取属性.py    
# Author :   柏汌  

from selenium import webdriver
from selenium.webdriver.common.by import By


drive = webdriver.Chrome()
drive.get('https://pic.netbian.com/4kmeinv/index.html')
src = drive.find_elements(By.XPATH, '//ul[@class="clearfix"]/li/a/img')
for i in src:
    print(i.get_attribute('src'))


