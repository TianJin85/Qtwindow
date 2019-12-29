# -*- encoding: utf-8 -*-
"""
@File    : LocalHTML.py
@Time    :  2019/12/29 22:30
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WebEngineView(QMainWindow):
    def __int__(self):
        super(WebEngineView, self).__int__()

    def initUI(self):
        self.setWindowTitle("装载本地页面")
        self.setGeometry(5, 30, 1355, 730)
        url = os.getcwd() + '/test.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.initUI()
    main.show()
    sys.exit(app.exec_())