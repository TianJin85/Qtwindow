# -*- encoding: utf-8 -*-
"""
@File    : Stretch.py
@Time    :  2020/1/5 15:00
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    设置伸缩量（addStretch）
'''
import sys
from PyQt5.QtWidgets import *


class Stretch(QWidget):
    def __int__(self):
        super(Stretch, self).__int__()

    def initUI(self):
        self.setWindowTitle('设置伸缩量')
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)

        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮3")
        btn4.setText("按钮4")
        btn5.setText("按钮5")


        layout = QHBoxLayout()

        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)

        btnOK = QPushButton(self)
        btnOK.setText("确定")
        btnCancel = QPushButton(self)
        btnCancel.setText("取消")
        layout.addStretch(1)

        layout.addWidget(btnOK)
        layout.addWidget(btnCancel)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.initUI()
    main.show()
    sys.exit(app.exec_())
