# -*- coding: utf-8 -*-
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
	time.sleep(1)
	offset = 0
	while browser.title != '青春有你第2季-助力榜' :
		pass
		#自动验证
		slider = browser.find_element_by_xpath('//*[@id="test"]')
		# 生成拖拽移动轨迹，加3是为了模拟滑过缺口位置后返回缺口的情况
		track_list=get_track((offset+150))
		print(track_list)
		time.sleep(2)
		ActionChains(browser).click_and_hold(slider).perform()
		time.sleep(0.2)
		# 根据轨迹拖拽圆球
		for track in track_list:
			ActionChains(browser).move_by_offset(xoffset=int(track),yoffset=0).perform()
			time.sleep(0.01)
		ActionChains(browser).release(slider).perform()
		offset += 5
	input("Waiting...")
	browser.quit()
#滑块移动轨迹
def get_track(distance):
	track=[]
	current=0
	mid=distance*7/8
	t=random.randint(2,3)/10
	v=0
	while current<distance:
		if current<mid:
			a=2
		else:
			a=-3
		v0=v
		v=v0+a*t
		move=v0*t+1/2*a*t*t
		current+=move
		track.append(round(move))
	return track
if __name__ == '__main__':
	login('18518150722','qwer12345')