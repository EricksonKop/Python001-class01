#!usr/bin/env python3
# -*- encoding: utf-8 -*-
import time
import traceback
# import win32com
# from win32com import client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome('I:/chromedriver_win32/chromedriver.exe')
driver.get('https://shimo.im/login?from=home')
driver.implicitly_wait(10)
try:
    driver.find_element_by_css_selector("input[type='text']").send_keys('13628639530')
    driver.find_element_by_css_selector("input[type='password']").send_keys('54kopallmylife')
    driver.find_element_by_css_selector("button[type='black']").click()
    time.sleep(3)
    assert '石墨文档' in driver.title
except:
    print(traceback.format_exc())
finally:
    driver.quit()
