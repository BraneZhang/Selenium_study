#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import os

fp = webdriver.FirefoxProfile()
# fp = webdriver.ChromeOptions()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # 下载文件的类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-2").click()
