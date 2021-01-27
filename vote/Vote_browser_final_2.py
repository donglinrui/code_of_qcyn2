from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtGui
import time
import sys
import re
import os 
class MainWindow(QWidget):
    # noinspection PyUnresolvedReferences
    def __init__(self, *args, **kwargs):#布局和控件初始化
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('青你2_投票浏览器-2')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(1200, 830)
        #状态记录
        self.load_state = 0#网页加载状态 1 为加载完成
        self.get_state = 0#获取数据状态 1为获取成功
        self.match_state = 0#匹配状态 1 为匹配完成
        self.over_state = 0#助力剩余状态，未剩余则为1
        self.clear_state = 0 #一键输入河组状态，0 为未输入
    #左边layout
        # 设置浏览器
        self.browser = QWebEngineView()
        url = 'https://m.iqiyi.com/h5base/act/QCYN2-ZL.html'
        self.browser.setUrl(QUrl(url))
        self.browser.loadFinished.connect(self.loadfinished)
    #右边layout3（最上面）
        self.logout_button = QPushButton('安全登出')
        self.reload_button = QPushButton('网页刷新')
        self.js_button = QPushButton('运行脚本')
        self.login_button = QPushButton('返回登录')
        self.f_logout_button = QPushButton('强制登出')
        self.input_quick_button = QPushButton('河组一键输入')

        self.reload_button.clicked.connect(self.browser.reload)
        self.logout_button.clicked.connect(self.logout)
        self.login_button.clicked.connect(self.login)
        self.js_button.clicked.connect(self.run_js)
        self.f_logout_button.clicked.connect(self.f_logout)
        self.input_quick_button.clicked.connect(self.input_quick)
    #右边1ayout1（中间）
        self.flo = QFormLayout()
        self.mem1 = QLineEdit()
        self.flo.addRow("训练生1: ", self.mem1)
        self.mem1.setPlaceholderText("许杨玉琢")
        self.mem1.setEchoMode(QLineEdit.Normal)
        self.mem1.setReadOnly(1);
        self.mem2 = QLineEdit()
        self.flo.addRow("训练生2: ", self.mem2)
        self.mem2.setPlaceholderText("")
        self.mem2.setEchoMode(QLineEdit.Normal)
        self.mem3 = QLineEdit()
        self.flo.addRow("训练生3: ", self.mem3)
        self.mem3.setPlaceholderText("")
        self.mem3.setEchoMode(QLineEdit.Normal)
        self.mem4 = QLineEdit()
        self.flo.addRow("训练生4: ", self.mem4)
        self.mem4.setPlaceholderText("")
        self.mem4.setEchoMode(QLineEdit.Normal)
        self.mem5 = QLineEdit()
        self.flo.addRow("训练生5: ", self.mem5)
        self.mem5.setPlaceholderText("")
        self.mem5.setEchoMode(QLineEdit.Normal)
        self.mem6 = QLineEdit()
        self.flo.addRow("训练生6: ", self.mem6)
        self.mem6.setPlaceholderText("")
        self.mem6.setEchoMode(QLineEdit.Normal)
        self.mem7 = QLineEdit()
        self.flo.addRow("训练生7: ", self.mem7)
        self.mem7.setPlaceholderText("")
        self.mem7.setEchoMode(QLineEdit.Normal)
        self.mem8 = QLineEdit()
        self.flo.addRow("训练生8: ", self.mem8)
        self.mem8.setPlaceholderText("")
        self.mem8.setEchoMode(QLineEdit.Normal)
        self.mem9 = QLineEdit()
        self.flo.addRow("训练生9: ", self.mem9)
        self.mem9.setPlaceholderText("")
        self.mem9.setEchoMode(QLineEdit.Normal)
    #右边layout2（下面）
        self.textEdit = QTextEdit()
        self.textEdit.resize(200,100)
        self.button_get = QPushButton('获取数据')
        self.button_get.clicked.connect(self.get_html)
        self.button_match = QPushButton('开始匹配')
        self.button_match.clicked.connect(self.match)
        self.button_make = QPushButton('打印脚本')
        self.button_make.clicked.connect(self.make_js)
        self.button_check = QPushButton('检查账号')
        self.button_check .clicked.connect(self.check)
        self.result = []
        self.qline1 = QLabel('')
        self.qline1.setWordWrap(True)
        self.qline2 = QLabel('Powered by Donglinrui') # 创建标签
        self.qline2.setAlignment(QtCore.Qt.AlignRight)
        self.qline2.setWordWrap(True)

        #设置最上面widget
        wg23 = QWidget()
        layout23 =QHBoxLayout()
        #设置中间widget
        layout = QHBoxLayout()
        layout.addWidget(self.browser)
        wg1 = QWidget()
        wg1.setLayout(layout)
        #设置下边widget
        wg2 = QWidget()
        layout2 =QVBoxLayout()
        #上面控件设置
        layout23.addWidget(self.login_button)
        layout23.addWidget(self.logout_button)
        layout23.addWidget(self.js_button)
        layout23.addWidget(self.reload_button)
        layout23.addWidget(self.f_logout_button)
        layout23.addWidget(self.input_quick_button)
        wg23.setLayout(layout23)
        #中间控件设置
        wg21 = QWidget()
        wg21.setLayout(self.flo)
        #下面控件设置
        wg22 = QWidget()
        layout22 = QVBoxLayout()
        layout22.addWidget(self.textEdit)
        layout22.addWidget(self.button_get)
        layout22.addWidget(self.button_match)
        layout22.addWidget(self.button_make)
        layout22.addWidget(self.button_check)
        layout22.addWidget(self.qline1)
        layout22.addWidget(self.qline2)
        wg22.setLayout(layout22)
    #右边整体设置
        layout2.addWidget(wg23)
        layout2.addWidget(wg21)
        layout2.addWidget(wg22)
        wg2.setLayout(layout2)
    #设置全局layout
        wlayout=QHBoxLayout()
        wlayout.addWidget(wg1)
        wlayout.addWidget(wg2)
        self.setLayout(wlayout)
    def input_quick(self):#河组成员一键输入
        if self.clear_state == 0: 
            self.clear_state = 1
            self.mem2.setText("许佳琪")
            self.mem3.setText("段艺璇")
            self.mem4.setText("张语格")
            self.mem5.setText("孙芮")
            self.mem6.setText("宋昕冉")
            self.mem7.setText("戴萌")
            self.mem8.setText("莫寒")
            self.mem9.setText("费沁源")
        else:
            self.clear_state = 0
            self.mem2.setText('')
            self.mem3.setText('')
            self.mem4.setText('')
            self.mem5.setText('')
            self.mem6.setText('')
            self.mem7.setText('')
            self.mem8.setText('')
            self.mem9.setText('')
    def get_html(self):#获取html数据并且找成员编号
        if self.load_state == 1:
            self.get_state = 1
            pass
            filename = "html.txt"
            f = open("html.txt","w",encoding='utf-8')
            self.html = self.browser.page().toHtml(lambda x: f.write(x))
            print("Successfully get Html!")
            self.textEdit.setPlainText("Successfully Done!")
        else:
            print("网页尚未加载完成，请等网页加载完成后重试")
    def get_name(self):#获取成员名字列表
        self.name = []
        t1 = self.mem2.text()
        t2 = self.mem3.text()
        t3 = self.mem4.text()
        t4 = self.mem5.text()
        t5 = self.mem6.text()
        t6 = self.mem7.text()
        t7 = self.mem8.text()
        t8 = self.mem9.text()
        self.name.append("许杨玉琢")#这里程序写死了，必须投许杨玉琢
        self.name.append(str(t1))
        self.name.append(str(t2))
        self.name.append(str(t3))
        self.name.append(str(t4))
        self.name.append(str(t5))
        self.name.append(str(t6))
        self.name.append(str(t7))
        self.name.append(str(t8))

    def match(self):#正则匹配
        if self.get_state == 1:
            self.match = 1
            print("匹配中请稍等")
            self.textEdit.setPlainText(" "+"\n")
            self.get_name()
            self.result =[]
            file = open("html.txt",'r', encoding='UTF-8')
            lines=file.readlines()
            real_name = []
            for n in self.name:
                if n != '':
                    real_name.append(n)
            print("有效名字："+str(real_name))
            self.qline1.setText("脚本已经生成，当前在投序列："+ str(real_name))
            for line in lines[21:]:
                for n in real_name :
                    rule = '.*>(.*)</div></a>.*'+n
                    searchObj = re.search(rule, line, re.M|re.I)
                    if searchObj:
                        print ("匹配成功！"+n+"序号是："+searchObj.group(1))
                        self.textEdit.insertPlainText("训练生"+n+"排名序号："+searchObj.group(1)+"\n")
                        self.result.append(searchObj.group(1))
                        real_name.remove(n)#匹配到一个，再序列中删掉此项
                        if (len(real_name)==0):#如果当前序列全都匹配完
                            break
                    else:
                        pass
            self.textEdit.insertPlainText("全部训练生排名序号序列："+str(self.result)+"\n")
            output =''
            for i in range(len(self.result)-1):
                output = output + self.result[i] + ','
            if len(self.result) != 0:
                output = output + self.result[len(self.result)-1]
            self.textEdit.insertPlainText(output + "\n")
            file.close()
        else:
            self.textEdit.setPlainText("请先获取数据！")
    def make_js(self):#生成js代码并输出，js代码可以用于其他浏览器投票
        if self.match == 1:
            line1 = 'var list = '+ str(self.result)+';'
            line2 = 'function doit(num){var css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ list[num] + ") > div > div.c-vote-btn";var clickit = document.querySelector(css);clickit.click();}var count = 0;function vote()\{console.log(count);doit(count);count++;if(count<9){setTimeout(vote,2000+count*100)\}\}'
            line3 = 'vote();'
            code = line1 + line2 +line3
            self.textEdit.setPlainText("脚本已打印！")
            self.textEdit.setPlainText(code)
        else:
            self.textEdit.setPlainText("请先匹配！")
    def loadfinished(self):
        self.load_state = 1
        self.textEdit.setPlainText("网页加载完成！")
    def logout(self):#安全登出，检查票量
        #检查剩余助力值
        print("检查是否符合退出标准中...")
        rest = ''
        login_state = 0 #登录状态
        try:#检查剩余票数
            file = open("html.txt",'r', encoding='UTF-8')
            lines=file.readlines()
            for line in lines[21:]:
                rule3 = '.* (.*)</span></div>.*助力规则'
                searchObj3 = re.search(rule3, line, re.M|re.I)
                if searchObj3:
                    print ("当前剩余助力值:" + searchObj3.group(1))
                    rest = searchObj3.group(1)
                    if searchObj3.group(1) == '0':
                        self.over_state = 1
                    if searchObj3.group(1) != '点击登录':
                        login_state = 1
                    break
                else:
                    pass
            print("检查结束！")
        except OSError as reason:
                msg_box = QMessageBox.warning(self,'警告','按照教程顺序操作',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if self.over_state == 1:
                self.over_state = 0
                print("Logout")
                q = QUrl('https://passport.iqiyi.com/apis/user/logout.action')
                if q.scheme() == '':
                    q.setScheme('http')
                self.browser.setUrl(q)
        else :
            if login_state == 0:
                msg_box = QMessageBox.warning(self,'警告','请登录！',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            else:
                msg_box = QMessageBox.warning(self,'警告',"当前剩余票数" + str(rest) + ",请手动投完再退出",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

    def login(self):#进入登录页面
        q = QUrl('https://m.iqiyi.com/h5base/act/QCYN2-ZL.html')
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)
    def run_js(self):#运行脚本
        self.textEdit.setPlainText("投票记录如上所示，请认真核对，并检查左侧剩余助力次数是否为0。")
        for num in self.result:
            css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ num + ") > div > div.c-vote-btn"
            code = "document.querySelector(\""+css+"\").click()"
            self.browser.page().runJavaScript(code)
            time.sleep(2)
            print("Finished num : " + num)
            self.textEdit.insertPlainText("已经完成排序为： " + num +"的训练生的投票。\n" )
        filename = "html.txt"
        f = open("html.txt","w",encoding='utf-8')
        self.html = self.browser.page().toHtml(lambda x: f.write(x))
        print("Successfully refresh Html!")
    def f_logout(self):#强制登出，不考虑剩余票量
        self.over = 0
        print("logout")
        q = QUrl('https://passport.iqiyi.com/apis/user/logout.action')
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)
    def check(self):
        print("检查账号中...")
        try:
            file = open("html.txt",'r', encoding='UTF-8')
            lines = file.readlines()
            result = []
            for line in lines[21:]:
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
                    break
                else:
                    pass
                rule3 = '.* (.*)</span></div>.*助力规则'
                searchObj3 = re.search(rule3, line, re.M|re.I)
                if searchObj3:
                    rest = searchObj3.group(1)
                    if rest == '0':
                        self.over_state = 1 #剩余助力值为0，可以结束该账号投票
                        print("投完了")
                    elif rest == '点击登录':
                        print("当前并非登录状态")
                        break
                    else:
                        print ("当前剩余助力值:" + searchObj3.group(1))
                else:
                    pass
            print("检查结束！")
            file.close()
            if rest == '点击登录':
                text = "当前未登录，请登录后再试！"
            else:
                text = "当前剩余助力值： " + rest + "\n"
                text = text +"\n历史投票信息： " + str(result) + "\n\n请认真核对！"
            self.textEdit.setPlainText(text)
        except OSError as reason:
            msg_box = QMessageBox.warning(self,'警告','按照教程顺序操作',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
    def closeEvent(self, event):#关闭程序时候删除缓存html
        try:
            os.remove("html.txt")
        except OSError as reason:
            print(reason)
        print("已经正常关闭！")
if __name__ == '__main__':
    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    window = MainWindow()
    # 显示窗口
    window.show()
    # 运行应用，并监听事件
    app.exec_()