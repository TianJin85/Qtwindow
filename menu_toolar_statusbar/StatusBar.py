# -*- encoding: utf-8 -*-
"""
@File    : StatusBar.py
@Time    :  2019/12/28 16:28
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class StatusBar(QMainWindow):
    def __int__(self):
        super(StatusBar, self).__int__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300, 200)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction('show')
        file.triggered.connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单被点击了")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.initUI()
    main.show()
    sys.exit(app.exec_())