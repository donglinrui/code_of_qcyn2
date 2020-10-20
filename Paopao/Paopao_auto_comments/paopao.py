# -*- coding: utf-8 -*-
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)
    url = ''#此处输入url地址
    browser.get(url)
    browser.delete_all_cookies()
    cookies = [{'domain': '.iqiyi.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '__dfp', 'path': '/', 'secure': False, 'value': 'a11b918a6f59a341dda1d481d4d6f0bb91c0317e76022ef68a42a2ba2ff72b6a83@1590995563269@1589699564269'}, {'domain': '.iqiyi.com', 'expiry': 1589785972, 'httpOnly': False, 'name': 'c241545878816', 'path': '/', 'secure': False, 'value': '1589699572769'}, {'domain': '.iqiyi.com', 'expiry': 1589703172, 'httpOnly': False, 'name': 'c11545878816', 'path': '/', 'secure': False, 'value': '1589699572768'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1589699573'}, {'domain': '.iqiyi.com', 'expiry': 1589785971, 'httpOnly': False, 'name': 'TQC022', 'path': '/', 'secure': False, 'value': '%7B%22au%22%3A%2260Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f%22%2C%22ak%22%3A%2245f7f4m1btKhtGjZfXJQudt0fv7ZPDbnZnH3zlBZaXDYSLjf4m4%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1589785971, 'httpOnly': False, 'name': 'QC163', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647988, 'httpOnly': False, 'name': 'P000email', 'path': '/', 'secure': False, 'value': '17841451518'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647968, 'httpOnly': False, 'name': 'P00002', 'path': '/', 'secure': False, 'value': '%7B%22uid%22%3A%221545878816%22%2C%22pru%22%3A1545878816%2C%22user_name%22%3A%2217841451518%22%2C%22nickname%22%3A%22%5Cu6728%5Cu6613%5Cu694a2000%22%2C%22pnickname%22%3A%22%5Cu6728%5Cu6613%5Cu694a2000%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1589958771, 'httpOnly': False, 'name': 'QC175', 'path': '/', 'secure': False, 'value': '%7B%22upd%22%3Atrue%2C%22ct%22%3A1589699571845%7D'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647938, 'httpOnly': False, 'name': 'P00PRU', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647891, 'httpOnly': False, 'name': 'P00010', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1589785963, 'httpOnly': False, 'name': 'QC001', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647907, 'httpOnly': False, 'name': 'P01010', 'path': '/', 'secure': False, 'value': '1589731200'}, {'domain': '.iqiyi.com', 'expiry': 1589731200, 'httpOnly': False, 'name': 'QC176', 'path': '/', 'secure': False, 'value': '%7B%22state%22%3A0%2C%22ct%22%3A1589699564149%7D'}, {'domain': '.iqiyi.com', 'expiry': 3737183213.161189, 'httpOnly': False, 'name': 'P00004', 'path': '/', 'secure': False, 'value': '.1589699566.e19b01231f'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'nu', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.iqiyi.com', 'expiry': 4427939572, 'httpOnly': False, 'name': 'QC173', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC010', 'path': '/', 'secure': False, 'value': '120059916'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647873, 'httpOnly': False, 'name': 'P00003', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'QC006', 'path': '/', 'secure': False, 'value': '4vld9ceg6sdf9a6xoqxat6u2'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC007', 'path': '/', 'secure': False, 'value': 'DIRECT'}, {'domain': '.iqiyi.com', 'expiry': 1592291570, 'httpOnly': False, 'name': 'QC160', 'path': '/', 'secure': False, 'value': '%7B%22u%22%3A%2217841451518%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A%2286%22%7D%2C%22type%22%3A%22p1%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647922, 'httpOnly': False, 'name': 'P00007', 'path': '/', 'secure': False, 'value': '60Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f'}, {'domain': '.iqiyi.com', 'expiry': 1621235563, 'httpOnly': False, 'name': 'QC008', 'path': '/', 'secure': False, 'value': '1589699563.1589699563.1589699563.1'}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1589699563'}, {'domain': '.iqiyi.com', 'expiry': 1589785972, 'httpOnly': False, 'name': 'QC179', 'path': '/', 'secure': False, 'value': '%7B%22userIcon%22%3A%22https%3A//img7.iqiyipic.com/passport/20190622/4f/b7/passport_1545878816_156116069575453_130_130.jpg%22%2C%22vipTypes%22%3A%221%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 4427939572, 'httpOnly': False, 'name': 'QC005', 'path': '/', 'secure': False, 'value': 'e57a350a9d5f300c5af27e7f5352625c'}, {'domain': '.iqiyi.com', 'expiry': 1621235571, 'httpOnly': False, 'name': 'QC116', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'QC170', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647833, 'httpOnly': False, 'name': 'P00001', 'path': '/', 'secure': False, 'value': '60Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f'}, {'domain': 'www.iqiyi.com', 'expiry': 1905059563, 'httpOnly': False, 'name': '__uuid', 'path': '/paopao', 'secure': False, 'value': 'e7f4c2f1-4900-0197-0fd8-6a44d09bea54'}]
    for cookie in cookies:
        browser.add_cookie(cookie)
    cookies = browser.get_cookies()
    browser.get(url)
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/a[2]/i").click()
    #/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/a[2]/i
    #                             /html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/d/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[4]/div[2]/a[2]/spaniv[1]/input
    count = 0
    textlist = ['1','2','3','4','5','6']#写入1~6为刷评论的内容
    flag = random.randint(0,1000)
    while 1 :
        count = count + 1
        if count%60 == 0:
            count = 1
            flag = flag + 1
            browser.quit()
            option = ChromeOptions()
            option.add_experimental_option('excludeSwitches', ['enable-automation'])
            browser = webdriver.Chrome(options=option)
            browser.get(url)#每60次重新刷新一遍网页
            #加载cookies进入网页，实行自动登录
            browser.delete_all_cookies()
            #cookies = [{'domain': '.iqiyi.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '__dfp', 'path': '/', 'secure': False, 'value': 'a11b918a6f59a341dda1d481d4d6f0bb91c0317e76022ef68a42a2ba2ff72b6a83@1590995563269@1589699564269'}, {'domain': '.iqiyi.com', 'expiry': 1589785972, 'httpOnly': False, 'name': 'c241545878816', 'path': '/', 'secure': False, 'value': '1589699572769'}, {'domain': '.iqiyi.com', 'expiry': 1589703172, 'httpOnly': False, 'name': 'c11545878816', 'path': '/', 'secure': False, 'value': '1589699572768'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1589699573'}, {'domain': '.iqiyi.com', 'expiry': 1589785971, 'httpOnly': False, 'name': 'TQC022', 'path': '/', 'secure': False, 'value': '%7B%22au%22%3A%2260Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f%22%2C%22ak%22%3A%2245f7f4m1btKhtGjZfXJQudt0fv7ZPDbnZnH3zlBZaXDYSLjf4m4%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1589785971, 'httpOnly': False, 'name': 'QC163', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647988, 'httpOnly': False, 'name': 'P000email', 'path': '/', 'secure': False, 'value': '17841451518'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647968, 'httpOnly': False, 'name': 'P00002', 'path': '/', 'secure': False, 'value': '%7B%22uid%22%3A%221545878816%22%2C%22pru%22%3A1545878816%2C%22user_name%22%3A%2217841451518%22%2C%22nickname%22%3A%22%5Cu6728%5Cu6613%5Cu694a2000%22%2C%22pnickname%22%3A%22%5Cu6728%5Cu6613%5Cu694a2000%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1589958771, 'httpOnly': False, 'name': 'QC175', 'path': '/', 'secure': False, 'value': '%7B%22upd%22%3Atrue%2C%22ct%22%3A1589699571845%7D'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647938, 'httpOnly': False, 'name': 'P00PRU', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647891, 'httpOnly': False, 'name': 'P00010', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1589785963, 'httpOnly': False, 'name': 'QC001', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647907, 'httpOnly': False, 'name': 'P01010', 'path': '/', 'secure': False, 'value': '1589731200'}, {'domain': '.iqiyi.com', 'expiry': 1589731200, 'httpOnly': False, 'name': 'QC176', 'path': '/', 'secure': False, 'value': '%7B%22state%22%3A0%2C%22ct%22%3A1589699564149%7D'}, {'domain': '.iqiyi.com', 'expiry': 3737183213.161189, 'httpOnly': False, 'name': 'P00004', 'path': '/', 'secure': False, 'value': '.1589699566.e19b01231f'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'nu', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.iqiyi.com', 'expiry': 4427939572, 'httpOnly': False, 'name': 'QC173', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC010', 'path': '/', 'secure': False, 'value': '120059916'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647873, 'httpOnly': False, 'name': 'P00003', 'path': '/', 'secure': False, 'value': '1545878816'}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'QC006', 'path': '/', 'secure': False, 'value': '4vld9ceg6sdf9a6xoqxat6u2'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC007', 'path': '/', 'secure': False, 'value': 'DIRECT'}, {'domain': '.iqiyi.com', 'expiry': 1592291570, 'httpOnly': False, 'name': 'QC160', 'path': '/', 'secure': False, 'value': '%7B%22u%22%3A%2217841451518%22%2C%22lang%22%3A%22%22%2C%22local%22%3A%7B%22name%22%3A%22%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%22%2C%22init%22%3A%22Z%22%2C%22rcode%22%3A48%2C%22acode%22%3A%2286%22%7D%2C%22type%22%3A%22p1%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647922, 'httpOnly': False, 'name': 'P00007', 'path': '/', 'secure': False, 'value': '60Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f'}, {'domain': '.iqiyi.com', 'expiry': 1621235563, 'httpOnly': False, 'name': 'QC008', 'path': '/', 'secure': False, 'value': '1589699563.1589699563.1589699563.1'}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1589699563'}, {'domain': '.iqiyi.com', 'expiry': 1589785972, 'httpOnly': False, 'name': 'QC179', 'path': '/', 'secure': False, 'value': '%7B%22userIcon%22%3A%22https%3A//img7.iqiyipic.com/passport/20190622/4f/b7/passport_1545878816_156116069575453_130_130.jpg%22%2C%22vipTypes%22%3A%221%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 4427939572, 'httpOnly': False, 'name': 'QC005', 'path': '/', 'secure': False, 'value': 'e57a350a9d5f300c5af27e7f5352625c'}, {'domain': '.iqiyi.com', 'expiry': 1621235571, 'httpOnly': False, 'name': 'QC116', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.iqiyi.com', 'expiry': 1621235572, 'httpOnly': False, 'name': 'QC170', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1597475570.647833, 'httpOnly': False, 'name': 'P00001', 'path': '/', 'secure': False, 'value': '60Kem1SjF9ej4GvefxxITxkfV1zM3SU27hQruGWhVqy1bA3nydxb7uCA5bm14kfaPdq33f'}, {'domain': 'www.iqiyi.com', 'expiry': 1905059563, 'httpOnly': False, 'name': '__uuid', 'path': '/paopao', 'secure': False, 'value': 'e7f4c2f1-4900-0197-0fd8-6a44d09bea54'}]
            for cookie in cookies:
                browser.add_cookie(cookie)
            cookies = browser.get_cookies()
            browser.get(url)
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/a[2]/i").click()
        try:
            input = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/div[1]/input")
            input.click()
            text = str(textlist[count%(len(textlist))]) + str(flag) + str(count)
            input.send_keys(text)
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/a").click()
            time.sleep(1)
            js_top = "var q=document.documentElement.scrollTop=0;"
            browser.execute_script(js_top)
            print(count)
        except Exception:
            count = count - 1