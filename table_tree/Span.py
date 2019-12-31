# -*- encoding: utf-8 -*-
"""
@File    : Span.py
@Time    :  2019/12/31 22:04
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    合并单元格
    setSpan(row, col, 要合并的行数， 要合并的列数)
'''
import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QBoxLayout, QApplication, QTableWidgetItem, QHBoxLayout)
from PyQt5.QtCore import Qt


class Span(QWidget):
    def __int__(self):
        super(Span, self).__int__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("合并单元格")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidaet = QTableWidget()
        tableWidaet.setRowCount(4)
        tableWidaet.setColumnCount(3)
        layout.addWidget(tableWidaet)

        tableWidaet.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem = QTableWidgetItem('雷神')
        tableWidaet.setItem(0, 0, newItem)
        # setSpan()
        tableWidaet.setSpan(0, 0, 3, 1)
        newItem = QTableWidgetItem('男')
        tableWidaet.setItem(0, 1, newItem)
        tableWidaet.setSpan(0, 1, 2, 1)

        newItem = QTableWidgetItem('160')
        tableWidaet.setItem(0, 2, newItem)
        tableWidaet.setSpan(0, 2, 3, 1)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Span()
    main.initUI()
    main.show()
    sys.exit(app.exec_())