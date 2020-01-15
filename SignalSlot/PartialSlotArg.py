# -*- encoding: utf-8 -*-
"""
@File    : PartialSlotArg.py
@Time    :  2020/1/14 23:06
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import *
from functools import partial


class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super(LambdaSlotArg, self).__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')

        button1.clicked.connect(partial(self.onButtonClick, 10, 20))
        button2.clicked.connect(partial(self.onButtonClick, 123, 20))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print("m + n = ", m  + n)
        QMessageBox.information(self, "结果", str(m+n))


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    main = LambdaSlotArg()
    main.show()
    sys.exit(app.exec_())