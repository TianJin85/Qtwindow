# -*- encoding: utf-8 -*-
"""
@File    : QComboBoxDemo.py
@Time    :  2019/12/24 21:14
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
下拉列表（QComboBox）
1.如果将列表项添加到QComboBox控件中
2.如何获取选中的列表项
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __int__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300,100)

        layout = QVBoxLayout()

        self.label = QLabel('请选中语言')

        self.cd = QComboBox()
        self.cd.addItem('C++')
        self.cd.addItem('Python')
        self.cd.addItems(['Java', 'C#', 'Ruby'])

        self.cd.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cd)

        self.setLayout(layout)

    def selectionChange(self,i):
        self.label.setText(self.cd.currentText())

        self.label.adjustSize()

        for count in range(self.cd.count()):
            print('item' + str(count) + '=' + self.cd.itemText(count))
            print('current index', i, 'selection changed', self.cd.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

