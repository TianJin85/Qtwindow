# -*- encoding: utf-8 -*-
"""
@File    : QRadioButtonDemo.py
@Time    :  2019/12/23 23:43
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

'''
    单选按钮控件（QRadioButton）
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __int__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()
        self.button1 = QRadioButton("单选按钮1")
        self.button1.setCheckable(True)

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '>被选中')
        else:
            print('<' +radioButton.text() + '>被取消选中转态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

