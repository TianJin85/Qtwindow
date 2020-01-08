# -*- encoding: utf-8 -*-
"""
@File    : Calc.py
@Time    :  2020/1/5 15:59
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    栅格布局，实现计算器UI
'''
import sys
from PyQt5.QtWidgets import *


class Calc(QWidget):
    def __int__(self):
        super(Calc, self).__int__()
        self.setWindowTitle('栅格布局')

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue

            button = QPushButton(name)
            grid.addWidget(button, *position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calc()
    main.initUI()
    main.show()
    sys.exit(app.exec_())