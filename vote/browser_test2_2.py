from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import time

 
import sys
class MainWindow(QWidget):
    # noinspection PyUnresolvedReferences
    def run_js(self):
        list = []
        file = open("list.txt") 
        while 1:
            line = file.readline()
            line = line.strip()
            list.append(str(line))
            if not line:
                break
        pass 
        file.close()
        list.remove('')
        print("当前准备投序列(序号为训练生排名)：")
        print(list)
        for num in list:
            css = "body > div:nth-child(1) > section.h5-act-votePage-templetBox > section.h5ActTemplet-voteBox > section > ul > li:nth-child("+ num + ") > div > div.c-vote-btn"
            code = "document.querySelector(\""+css+"\").click()"
            self.browser.page().runJavaScript(code)
            time.sleep(2)
            print("NO."+num+ "  Done!")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('青你投票测试_浏览器_2')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))
        # 设置窗口大小900*600
        self.resize(1000, 800)
        #self.show()
        #self.showMaximized()
        wlayout=QHBoxLayout()
        layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        # 设置浏览器
        self.browser = QWebEngineView()
        url = 'https://m.iqiyi.com/h5base/act/QCYN2-ZL.html'
        self.browser.setUrl(QUrl(url))
        # 指定打开界面的 URL
        #QAction类提供了抽象的用户界面action，这些action可以被放置在窗口部件中
        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QPushButton('网页后退')
        next_button = QPushButton('网页前进')
        logout_button = QPushButton('退出登录')
        reload_button = QPushButton('网页刷新')
        js_button = QPushButton('运行脚本')
        login_button = QPushButton('返回登录页面')
#按钮事件
        back_button.clicked.connect(self.browser.back)
        next_button.clicked.connect(self.browser.forward)
        logout_button.clicked.connect(self.logout)
        reload_button.clicked.connect(self.browser.reload)
        logout_button.clicked.connect(self.logout)
        login_button.clicked.connect(self.login)
        js_button.clicked.connect(self.run_js)
#增加局部控件
        layout.addWidget(self.browser)
        layout1.addWidget(js_button)
        layout1.addWidget(back_button)
        layout1.addWidget(next_button)
        layout1.addWidget(reload_button)
        layout1.addWidget(logout_button)
        layout1.addWidget(login_button)
        #设置两个layout
        wg1=QWidget()
        wg2=QWidget()
        wg1.setLayout(layout)
        wg2.setLayout(layout1)
        wlayout.addWidget(wg1)
        wlayout.addWidget(wg2)
        self.setLayout(wlayout)
    def logout(self):
        print("logout")
        q = QUrl('https://passport.iqiyi.com/apis/user/logout.action')
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)
    def login(self):
        q = QUrl('https://m.iqiyi.com/h5base/act/QCYN2-ZL.html')
        if q.scheme() == '':
            q.setScheme('http')
        self.browser.setUrl(q)
    def get_html():
        pass
        html = self.browser.page().toHtml(lambda x: print(x))
        print(html)
 
# 创建应用
app = QApplication(sys.argv)
# 创建主窗口
window = MainWindow()
# 显示窗口
window.show()
#全屏显示
# 运行应用，并监听事件
app.exec_()