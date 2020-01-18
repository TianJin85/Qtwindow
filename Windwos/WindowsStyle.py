# -*- encoding: utf-8 -*-
"""
@File    : WindowsStyle.py
@Time    :  2020/1/18 13:54
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    窗口、绘图与特效：设置窗口风格
    QApplication.setStyle(...)
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

class WindowsStyle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置窗口风格")
        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel('设置窗口风格')
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        # 获取当前窗口的风格
        print(QApplication.style().objectName())
        index = self.styleComboBox.findText(QApplication.style().objectName(), QtCore.Qt.MatchFixedString)
        self.styleComboBox.setCurrentIndex(index)

        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        self.setLayout(horizontalLayout)


    def handleStyleChanged(self, style):
        QApplication.setStyle(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowsStyle()
    main.show()
    sys.exit(app.exec_())

