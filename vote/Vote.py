# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import Read_log
def login(user,passwd):
	option = ChromeOptions()
	option.add_experimental_option('excludeSwitches', ['enable-automation'])
	browser = webdriver.Chrome(options=option)
	browser.get('https://m.iqiyi.com/h5base/act/QCYN2-ZL.html')
	print(browser.title)
	print("开始投票")
	login_btn = browser.find_element_by_css_selector('body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > div.myVote-box > div.h5ActTemplet-voteInfo > div.vote-nub > span.highlight')
	login_btn.click()
	user_id = browser.find_element_by_css_selector('#phoneNumber')
	pwd = browser.find_element_by_xpath('/html/body/div[1]/div[1]/form/section/div[1]/div[2]/div[3]/input')
	user_id.send_keys(user)
	pwd.send_keys(passwd)
	login = browser.find_element_by_css_selector('body > div.m-pc-resetBg > div:nth-child(2) > form > section > div:nth-child(1) > div:nth-child(4) > a')
	login.click()
	print("请手动输入验证码来验证")
	while browser.title != '青春有你第2季-助力榜' :
		pass
		time.sleep(1)
	print("success!")
	time.sleep(1)
	list = ["11","15","16","45","58","63","83","85","100"]
	for num in list:
		css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ num + ") > div > div.c-vote-btn"
		code = "document.querySelector(\""+css+"\").click()"
		browser.execute_script(code)
		if num =="85":
			print("你已经完成训练时许杨玉琢的投票")
		else:
			print("你已经完成序号为："+ num +"的训练生的投票") 
		time.sleep(float(2+int(num)*0.01))
	time.sleep(1)
	browser.quit()
if __name__ == '__main__':
	user,password = Read_log.read()
	for i in range(0,len(user)):
		print("====进行账号===="+user[i]+"====的投票====序号："+str(i)+"====")
		login(user[i],password[i])