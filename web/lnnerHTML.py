# -*- encoding: utf-8 -*-
"""
@File    : lnnerHTML.py
@Time    :  2019/12/29 22:51
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

class InnerHTML(QMainWindow):

    def __int__(self):
        super(InnerHTML, self).__int__()
    def initUI(self):
        self.setWindowTitle("显示嵌入Web页面")
        self.setGeometry(5, 30, 1355, 730)

        self.browser = QWebEngineView()
        self.browser.setHtml("""
                <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <h1>添加</h1>
            <h1>删除</h1>
            <h1>查询</h1>
        </body>
        </html>
        """)
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = InnerHTML()
    main.initUI()
    main.show()
    sys.exit(app.exec_())