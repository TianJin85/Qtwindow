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
    设置控件的对齐方式
'''
import sys
from PyQt5.QtWidgets import *


class HBoxLayoutAlign(QWidget):
    def __int__(self):
        super(HBoxLayoutAlign, self).__int__()

    def initUI(self):
        self.setWindowTitle("设置控件的对齐方式")
        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'), 2, Qt.AlignLeft | Qt.AlignBottom)
        hlayout.addWidget(QPushButton('按钮2'), 4, Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮3'), 1, Qt.AlignLeft | Qt.AlignTop)
        hlayout.addWidget(QPushButton('按钮4'), 1, Qt.AlignLeft | Qt.AlignRight)
        hlayout.addWidget(QPushButton('按钮5'), 1, Qt.AlignLeft | Qt.AlignBottom)

        # 设置按钮之间的间隔
        hlayout.setSpacing(40)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayoutAlign()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

