#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome()

# 访问百度首页
first_url = 'http://www.baidu.com'
print("now access %s" % (first_url))
driver.get(first_url)

# 访问新闻页面
second_url = 'http://news.baidu.com'
print("now access %s" % (second_url))
driver.get(second_url)

# 返回（后退）到百度首页
print("back to %s " % (first_url))
driver.back()
time.sleep(3)

# 前进到新闻页
print("forward to %s" % (second_url))
driver.forward()
time.sleep(5)
driver.quit()
