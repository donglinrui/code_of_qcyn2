import re
 
line = '>20</div></a> <div class="vote-perdetail" data-pingback-id="52280343802995"><div class="c-name" style="color: rgb(36, 94, 255);">许杨玉琢';
 
#searchObj = re.search( r'.* (.*) are.*', line, re.M|re.I)
searchObj = re.search( r'.*>(.*)</div></a>.*许杨玉琢', line, re.M|re.I)
if searchObj:
	print ("searchObj.group() : ", searchObj.group())
	print ("searchObj.group(1) : ", searchObj.group(1))
else:
	print ("Nothing found!!")

#>20</div></a> <div class="vote-perdetail" data-pingback-id="52280343802995"><div class="c-name" style="color: rgb(36, 94, 255);">许杨玉琢
#.*>(.*)</div></a>.*许杨玉琢