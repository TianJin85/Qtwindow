# -*- encoding: utf-8 -*-
"""
@File    : WindowPattern.py
@Time    :  2020/1/19 10:59
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from PyQt5.QtCore import *
import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口的样式')
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(r'D:\360MoveData\Users\asus\Desktop\Qtwindow\web\tt.html'))
        self.setCentralWidget(self.browser)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        # self.setObjectName("MainWindow")
        # self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WindowPattern()
    form.show()
    sys.exit(app.exec_())