# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
if __name__ == '__main__':
	option = ChromeOptions()
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	options.add_argument('--incognito')
	option.add_argument('--disable-infobars')#禁用正在被自动化程序控制提示
	browser = webdriver.Chrome(options=option)
	browser.set_window_size(600,1080)
	browser.get('https://m.iqiyi.com/h5base/act/QCYN2-ZL.html')
	print(browser.title)
	name = browser.find_element_by_xpath('/html/body/div[1]/section[3]/section[3]/section/ul/li[1]/div/div[1]/div')
	print(name)
	input("Waiting...")