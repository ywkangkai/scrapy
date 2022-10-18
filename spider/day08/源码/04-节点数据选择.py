#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-节点数据选择.py    
# Author :   柏汌  

from lxml import etree
text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''

html = etree.HTML(text)

li_list = html.xpath("//li[@class='item-1']")
print(li_list)
for i in li_list:
    print(i.xpath('//text()'))

