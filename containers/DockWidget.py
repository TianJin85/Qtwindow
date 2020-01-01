# -*- encoding: utf-8 -*-
"""
@File    : DockWidget.py
@Time    :  2020/1/1 21:52
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    停靠控件（QDockWidget）
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __int__(self, parent=None):
        super(DockDemo, self).__int__()

        self.setWindowTitle('停靠控件（QDocWidget）')
    def initUI(self):
        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        self.items.setWidget(self.listWidget)

        self.setCentralWidget(QLineEdit())

        # self.items.setFloating(True)

        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.initUI()
    demo.show()
    sys.exit(app.exec_())