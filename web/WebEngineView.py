# -*- encoding: utf-8 -*-
"""
@File    : WebEngineView.py
@Time    :  2019/12/29 22:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class WebEngineView(QMainWindow):
    def __int__(self):
        super(WebEngineView, self).__int__()
    def initUI(self):
        self.setWindowTitle("打开外部网页列子")
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://www.baidu.com"))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WebEngineView()
    win.initUI()
    win.show()
    sys.exit(app.exec_())