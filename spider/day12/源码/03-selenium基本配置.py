#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-selenium基本配置.py    
# Author :   柏汌
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
# 禁用图片
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)

# 无头模式  在后台远行
# options.add_argument('-headless')

# 设置user-agent
# user = '1232342345345'
# options.add_argument('user-agent=%s' %user)

# 隐藏正在受到自动化控制
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 拓展的使用
# path = r'E:\BaiduNetdiskDownload\Chrome插件\iguge_2011\igg_2.0.11.crx'
# options.add_extension(path)

# 设置代理
# options.add_argument('--proxy-server=http://58.20.184.187:9091')

# 初始化配置信息
drive = webdriver.Chrome(options=options)
# 设置浏览器最大化
drive.maximize_window()
# 设置宽搞
drive.set_window_size(800, 800)

drive.get('https://www.baidu.com')

#通过js打开一个新的页面
drive.execute_script('window.open("http://httpbin.org/ip")')

time.sleep(2)
# drive.quit()
