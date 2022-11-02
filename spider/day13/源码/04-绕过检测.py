#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-绕过检测.py    
# Author :   柏汌  

import time
from selenium import webdriver

# drive = webdriver.Chrome()
# drive.get('https://bot.sannysoft.com/')

# 设置屏蔽
options = webdriver.ChromeOptions()
# 绕过检测
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
driver.get('https://bot.sannysoft.com/')