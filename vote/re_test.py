# -*- coding: utf-8 -*-
import re

def match():
	print("匹配中请稍等")
	result =[]
	file = open("html.txt",'r', encoding='UTF-8')
	lines=file.readlines()
	for line in lines:
		rule1 = '.*class="photo-bottomMaterial"></div> <!----></a>.*>(.*)'
		searchObj = re.search(rule1, line, re.M|re.I)
		if searchObj:
			print ("匹配成功！"+"内容是："+searchObj.group(1))
			result.append(searchObj.group(1))
		else:
			pass
		rule2 = '.*class="c-rank">1<'
		searchObj2 = re.search(rule2, line, re.M|re.I)
		if searchObj2:
			print ("退出匹配...")
			break
		else:
			pass
		rule3 = '.* (.*)</span></div>.*助力规则'
		searchObj3 = re.search(rule3, line, re.M|re.I)
		if searchObj3:
			print ("当前剩余助力值:" + searchObj3.group(1))
		else:
			pass
	print("匹配结束！")
	print(result)
	return result
if __name__ == '__main__':
	match()

#16</span></div> <div class="vote-rule" data-pingback-id="80805777188139" style="color: rgb(36, 94, 255);">助力规则
#class="photo-bottomMaterial"></div> <!----></a> <div class="vote-perdetail" data-pingback-id="79221350196050"><div class="c-name" style="color: rgb(36, 94, 255);">许佳琪
#class="c-rank"
#16<.*助力规则