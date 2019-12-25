# -*- encoding: utf-8 -*-
"""
@File    : QMessageBox.py
@Time    :  2019/12/25 22:31
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    消息对话框：QMessageBox
    
    1.关于对话框
    2.错误对话框
    3.警告对话框
    4.提问对话框
有2点差异
1.显示的对话框图标可能不同
2.显示的按钮是不一样的
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QMessageBoxDemo(QWidget):
    def __int__(self):
        super(QMessageBoxDemo, self).__init__()

    def initUI(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)

        layout = QVBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText("显示关于对话框")
        self.button1.clicked.connect(self.showDialog)
            
        layout.addWidget(self.button1)
        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == "显示关于对话框":
            QMessageBox.about(self, '关于', '这是一个关于对话框')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

