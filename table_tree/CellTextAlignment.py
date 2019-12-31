# -*- encoding: utf-8 -*-
"""
@File    : CellTextAlignment.py
@Time    :  2019/12/31 21:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    设置单元格的文本对齐方式
    setTextAlignment
    Qt.AlignRight   Qt.AlignBotton
'''
import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QBoxLayout, QApplication, QTableWidgetItem, QHBoxLayout)
from PyQt5.QtCore import Qt


class CellTextAlignment(QWidget):
    def __int__(self):
        super(CellTextAlignment, self).__int__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格的文本对齐方式")
        self.resize(430, 230)
        layout = QHBoxLayout()
        tableWidaet = QTableWidget()
        tableWidaet.setRowCount(4)
        tableWidaet.setColumnCount(3)
        layout.addWidget(tableWidaet)

        tableWidaet.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem = QTableWidgetItem('雷神')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidaet.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('男')
        newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignBottom)
        tableWidaet.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('190')
        newItem.setTextAlignment(Qt.AlignRight)
        tableWidaet.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.initUI()
    main.show()
    sys.exit(app.exec_())