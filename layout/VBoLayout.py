# -*- encoding: utf-8 -*-
"""
@File    : VBoLayout.py
@Time    :  2020/1/5 14:52
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    水平盒布局（QHBoxLayout）
'''
import sys
from PyQt5.QtWidgets import *


class HBoxLayout(QWidget):
    def __int__(self):
        super(HBoxLayout, self).__int__()

    def initUI(self):
        self.setWindowTitle("水平盒布局")
        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))

        # 设置按钮之间的间隔
        hlayout.setSpacing(40)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayout()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

