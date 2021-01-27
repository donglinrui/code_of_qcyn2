from selenium import webdriver
driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)

# 通过js新打开一个窗口
new_page='window.open("https://www.baidu.com");'
driver.execute_script(new_page)
input("Waiting...")

	new_page='window.open("https://passport.iqiyi.com/apis/user/logout.action");'
	browser.execute_script(new_page)
	input("Waiting...")
	# 最大化浏览器
	#browser.maximize_window()
	# 定位到页面顶部
	js='window.scrollTo(0,0)'
	browser.execute_script(js)
	time.sleep(2)
	# 获取所有的打开的浏览器窗口
	windowstabs=browser.window_handles
	print(windowstabs)
	# 获取当前浏览器的窗口
	currenttab=browser.current_window_handle
	print(currenttab)
	# 切换到新窗口
	browser.switch_to.window(windowstabs[0])
driver.quit()
