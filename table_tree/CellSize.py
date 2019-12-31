# -*- encoding: utf-8 -*-
"""
@File    : CellSize.py
@Time    :  2019/12/31 22:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys

from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (QWidget, QTableWidget, QBoxLayout, QApplication, QTableWidgetItem, QHBoxLayout)
from PyQt5.QtCore import Qt


class Span(QWidget):
    def __int__(self):
        super(Span, self).__int__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格尺寸")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（KG）'])
        tableWidget.setRowHeight(0, 80)
        tableWidget.setColumnWidth(2, 120)
        tableWidget.setRowHeight(2, 100)
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times', 14, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 0, 0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times', 20, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Span()
    main.initUI()
    main.show()
    sys.exit(app.exec_())