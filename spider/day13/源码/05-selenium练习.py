#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-selenium练习.py    
# Author :   柏汌  


#  采集义务购商品网站

from selenium import webdriver
import time, random
from selenium.webdriver.common.by import By
import pymongo

class Yw:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=options)
        self.url = 'https://www.yiwugo.com/'

    def base(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'inputkey').send_keys('饰品')
        self.driver.find_element(By.XPATH, '//div[@class="search-index"]/span[last()]').click()

    def page_next(self):
        try:
            next = self.driver.find_element(By.XPATH, '//ul[@class="right"]/a[@class="page_next_yes"]')
            if next:
                next.click()
                self.spider()
            else:
                self.driver.close()

        except Exception as e:
            print(e)

    def spider(self):
        # self.base()
        self.drop_down()
        div_list = self.driver.find_elements(By.CLASS_NAME, 'pro_list_product_img2')
        for div in div_list:
            title = div.find_element(By.XPATH, './/li/a[@class="productloc"]')
            price = div.find_element(By.XPATH, './/li/span/em')
            address = div.find_element(By.XPATH, './/li[@class="shshopname"]')
            item = {
                '标题': title.text,
                '价格': price.text,
                '地址': address.text,
            }
            print(item)
        self.page_next()

    def drop_down(self):
        for i in range(1, 10):
            j = i / 10
            js_code = f'document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}'
            self.driver.execute_script(js_code)
            time.sleep(random.randint(400, 800)/1000)

if __name__ == '__main__':
    yw = Yw()
    yw.base()
    yw.spider()

