# -*- encoding: utf-8 -*-
"""
@File    : LambdaSlotArg.py
@Time    :  2020/1/14 22:42
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    使用Lambda表达式为槽函数传递参数
    Lambda表达式：匿名函数，也就是没有名字的函数
    fun = lambda:print("Hello world")
    fun()
    fun1 = lambda x, y:print(x, y)
    fun1('a', 'b')
'''
import sys
from PyQt5.QtWidgets import *

class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super(LambdaSlotArg, self).__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')

        button1.clicked.connect(lambda :self.onButtonClick(10, 20))

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