# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    :  2019/12/30 10:14
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


class PyQtCallJS(QWidget):

    def __int__(self):
        super(PyQtCallJS, self).__int__()

    def initUI(self):
        self.setWindowTitle("PyQt5调用JavaScript")
        self.setGeometry(0, 0, 1920, 1080)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.browser = QWebEngineView()

        self.browser.load(QUrl('https://www.baidu.com'))
        self.textEdit = QTextEdit()


        self.layout.addWidget(self.browser, stretch=5)
        self.layout.addWidget(self.textEdit)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyQtCallJS()
    main.initUI()
    main.show()
    sys.exit(app.exec_())