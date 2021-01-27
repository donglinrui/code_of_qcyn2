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
    option.add_argument('user-agent=paopao_app')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options = option)
    #browser.get('http://paopao.m.iqiyi.com/youth/beautyRanking')
    #browser.delete_all_cookies()
    #cookies = [{'domain': '.iqiyi.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '__dfp', 'path': '/', 'secure': False, 'value': 'a0314f4685b04e49f195b23f784b38c8834f07ff2026e1d142f359fe49cdd4ccd5@1589900620900@1588604621900'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.193095, 'httpOnly': False, 'name': 'P00002', 'path': '/', 'secure': False, 'value': '%7B%22uid%22%3A%222477125437%22%2C%22pru%22%3A2477125437%2C%22user_name%22%3A%2218518150722%22%2C%22nickname%22%3A%22%5Cu4e1c%5Cu6797%5Cu4e1c%5Cu6797%5Cu777f%22%2C%22pnickname%22%3A%22%5Cu4e1c%5Cu6797%5Cu4e1c%5Cu6797%5Cu777f%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.193038, 'httpOnly': False, 'name': 'P00007', 'path': '/', 'secure': False, 'value': '9fFsem2YEm3AHkt1s29bYVDARTE4To6nXv4Q8IH6JSZDvsm3ChgszgOV8LfllBLAkLN7G6e'}, {'domain': '.iqiyi.com', 'expiry': 3736088269.877918, 'httpOnly': False, 'name': 'P00004', 'path': '/', 'secure': False, 'value': '.1588604622.642000c2c7'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.19302, 'httpOnly': False, 'name': 'P01010', 'path': '/', 'secure': False, 'value': '1588608000'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.193, 'httpOnly': False, 'name': 'P00010', 'path': '/', 'secure': False, 'value': '2477125437'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.192937, 'httpOnly': False, 'name': 'P00001', 'path': '/', 'secure': False, 'value': '9fFsem2YEm3AHkt1s29bYVDARTE4To6nXv4Q8IH6JSZDvsm3ChgszgOV8LfllBLAkLN7G6e'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC005', 'path': '/', 'secure': False, 'value': '327321c9388902b594601cbb1ae9c7f2'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.192978, 'httpOnly': False, 'name': 'P00003', 'path': '/', 'secure': False, 'value': '2477125437'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC007', 'path': '/', 'secure': False, 'value': 'https%3A%2F%2Fm.iqiyi.com%2Fh5base%2Fact%2FQCYN2-ZL.html'}, {'domain': '.iqiyi.com', 'expiry': 1596380637.193057, 'httpOnly': False, 'name': 'P00PRU', 'path': '/', 'secure': False, 'value': '2477125437'}, {'domain': 'm.iqiyi.com', 'expiry': 1903964635, 'httpOnly': False, 'name': '__uuid', 'path': '/', 'secure': False, 'value': '8a73b3a0-0afd-f950-f8a5-4715bf7b4a2e'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC112', 'path': '/', 'secure': False, 'value': '1dad3d8627ea051a7fe87c3d804254b0'}, {'domain': '.iqiyi.com', 'expiry': 1620140624, 'httpOnly': False, 'name': 'QC006', 'path': '/', 'secure': False, 'value': 'b1d0518b35d0f999c5aadcef6621ddb1'}, {'domain': 'm.iqiyi.com', 'expiry': 1903964620, 'httpOnly': False, 'name': '__uuid', 'path': '/h5base/act', 'secure': False, 'value': '6aaa18c4-ceb7-add3-cea1-8ac74486a6f2'}]
    #for cookie in cookies:
    #    browser.add_cookie(cookie)
    browser.get('https://m.iqiyi.com/h5base/act/QCYN2-ZL.html')
    js = " window.open('https://passport.iqiyi.com/apis/user/logout.action')"
    browser.execute_script(js)
    #js = " window.open('http://paopao.m.iqiyi.com/youth/beautyRanking')"
    #browser.execute_script(js)
    count = 0
    while 1 :
        while browser.title == '青春有你第2季-助力榜' :
                #list = [25]
                for num in list:
                    css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ str(num) + ") > div > div.c-vote-btn"
                    code = "document.querySelector(\""+css+"\").click()"
                    try:
                        browser.execute_script(code)
                    except Exception:
                        print(str(Exception))
                        print ("失败")
                    else:
                        if num == 25:
                            print("你已经完成训练生许杨玉琢的投票")
                        else:
                            print("你已经完成序号为："+ str(num) +"的训练生的投票") 
                    #time.sleep(float(2+int(num)*0.01))
                    #time.sleep(0.5)