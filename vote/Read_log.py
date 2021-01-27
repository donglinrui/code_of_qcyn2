import re
def read():
	user = [0]
	password = [0]
	file = open("account_info.txt",'r') 
	lines=file.readlines()
	for line in lines:
		line = line.strip()
		out = re.split('----',line)
		user.append(out[0])
		password.append(out[1])
	file.close()
	user.remove(0)
	password.remove(0)
	return user,password
