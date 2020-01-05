# -*- encoding: utf-8 -*-
"""
@File    : HBoxLayoutAlign.py
@Time    :  2020/1/5 14:34
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from PyQt5.QtCore import Qt

'''
    垂直盒布局
'''
import sys
from PyQt5.QtWidgets import *


class VBoxLayout(QWidget):
    def __int__(self):
        super(VBoxLayout, self).__int__()

    def initUI(self):
        self.setWindowTitle("垂直和布局")
        layout = QVBoxLayout()
        layout.addWidget(QPushButton('按钮1'))
        layout.addWidget(QPushButton('按钮2'))
        layout.addWidget(QPushButton('按钮3'))
        layout.addWidget(QPushButton('按钮4'))
        layout.addWidget(QPushButton('按钮5'))

        # 设置按钮之间的间隔
        layout.setSpacing(40)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

