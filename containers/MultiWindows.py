# -*- encoding: utf-8 -*-
"""
@File    : MultiWindows.py
@Time    :  2020/1/2 21:43
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    容纳多文档窗口
    QMdiArea
    QMdiSubWindow
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    count = 0

    def __int__(self, parent=None):
        super(MultiWindows, self).__int__()

    def initUI(self):
        self.setWindowTitle('容纳多文档窗口')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction('New')
        file.addAction('cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowaction)

    def windowaction(self, q):
        if q.text() == "New":
            MultiWindows.count == MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == 'cascade':
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.initUI()
    demo.show()
    sys.exit(app.exec_())
