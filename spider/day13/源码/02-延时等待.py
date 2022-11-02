#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-延时等待.py    
# Author :   柏汌

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drive = webdriver.Chrome()
drive.get('https://www.baidu.com')
wait = WebDriverWait(drive, 10)
input1 = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
button = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
print(input1)
print(button)
