# -*- encoding: utf-8 -*-
"""
@File    : PyQtCallJS.py
@Time    :  2019/12/30 0:06
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

        url = os.getcwd() + '/tt.html'
        self.browser.load(QUrl.fromLocalFile(url))

        self.layout.addWidget(self.browser)

        button = QPushButton('设置全名')
        button.clicked.connect(self.fullname)
        self.layout.addWidget(button)

    def js_callback(self, result):
        print(result)

    def fullname(self):
        self.value = 'hello world'
        self.browser.page().runJavaScript('fullname("' + self.value + '");', self.js_callback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyQtCallJS()
    main.initUI()
    main.show()
    sys.exit(app.exec_())