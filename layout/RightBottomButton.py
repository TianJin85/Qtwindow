# -*- encoding: utf-8 -*-
"""
@File    : RightBottomButton.py
@Time    :  2020/1/5 15:25
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    让按钮永远在窗口右下角
'''
import sys
from PyQt5.QtWidgets import *


class RightBottomButton(QWidget):
    def __int__(self):
        super(RightBottomButton, self).__int__()

    def initUI(self):
        self.setWindowTitle("让按钮永远在右下角")
        self.resize(400, 300)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')

        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(0)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottomButton()
    main.initUI()
    main.show()
    sys.exit(app.exec_())