#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("appium")
time.sleep(2)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
