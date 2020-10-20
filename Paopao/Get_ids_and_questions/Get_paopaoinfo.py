import xlwt
from bs4 import BeautifulSoup
import time
from selenium import webdriver
def get_from_internet():
    driver = webdriver.Chrome()
    url =''#输入话题页的url
    driver.get(url)
    html = ''
    while (1):  # 上下滑动网页，加载出所有页面，如果获取到的数据不全，请延长延时时间
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.5)  # 延时时间，为了能够让页面加载完全
        # 如果页面获取到的数据不再更新，即页面全部加载完，就停止采集
        if html == driver.execute_script("return document.documentElement.outerHTML"):
            break
        else:
            html = driver.execute_script("return document.documentElement.outerHTML")
    return html
def get_from_file():
    f = open('html.txt','r',encoding='utf-8')
    text = f.read()
    f.close()
    return text
if __name__ == '__main__':
    #paopao_info = request.urlopen('http://www.iqiyi.com/paopao/shijian_203635651.html')
    #html = paopao_info.read()
    html = get_from_internet()
    soup = BeautifulSoup(html, 'lxml' )
    html = soup.prettify()
    #print(html)
    f = open('html.txt', 'w', encoding='utf-8')
    f.write(html)
    soup = BeautifulSoup(html,'lxml')
    list = soup.html.contents[3].contents[11].contents[1].contents[7].contents[1].contents[1].contents[3].contents[5].contents[7]
    #thisone = list.contents[1]
    #name = thisone.contents[3].contents[3].contents[1].contents[1].contents[1].text.strip()
    #print(name)
    names = []
    questions =[]
    list1 = soup.find_all("div", {"class": "m-feedSection"})
    for node in list1:
        name = node.contents[3].contents[3].contents[1].contents[1].contents[1].text.strip()
        names.append(name)
    list2 =soup.find_all("span", {"data-paopao-ele": "dispalyContent"})
    for node in list2:
        questions.append(node.text.strip())
    for i in range(0,len(names)):
        print("第"+str(i+1)+"号："+names[i])
        print("\n"+questions[i])
        print("=================================================================================")
    workbook = xlwt.Workbook(encoding='uft-8')
    worksheet = workbook.add_sheet("id&questions")
    worksheet.write(0,0,"ID")
    worksheet.write(0,1,"题目")
    worksheet.col(0).width = 3000
    worksheet.col(1).width = 30000
    for i in range(0,len(names)):
        worksheet.write(i+1,0,names[i])
        worksheet.write(i+1,1,str(questions[i]))
    workbook.save("泡泡圈id和题目.xls")
    temp = []
    for i in names:
        if i not in temp:
            temp.append(i)
        else:
            pass
    names = temp
    for i in range(0, len(names)):
        print("第" + str(i + 1) + "号：" + names[i])