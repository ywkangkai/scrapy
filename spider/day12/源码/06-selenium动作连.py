#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-selenium动作连.py    
# Author :   柏汌  


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
drive.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
iframe= drive.find_element(By.XPATH, '//div[@id="iframewrapper"]/iframe')
drive.switch_to.frame(iframe)
sou = drive.find_element(By.CSS_SELECTOR, '#draggable')
tag = drive.find_element(By.CSS_SELECTOR, '#droppable')
action = ActionChains(drive)
action.drag_and_drop(sou, tag)
# 执行动作连

action.perform()
