# -*- encoding: utf-8 -*-
"""
@File    : QStackedWidget.py
@Time    :  2020/1/1 21:29
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class StackedExample(QWidget):
    def __int__(self):
        super(StackedExample, self).__int__()
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('堆栈窗口控件（QStackedWidget）')

    def initUI(self):
        self.list = QListWidget()
        self.list.insertItem(0, '联系方式')
        self.list.insertItem(1, '个人信息')
        self.list.insertItem(2, '教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab3UI()
        self.tab2UI()
        self.tab1UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())

        self.stack1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)

        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)

    def display(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.initUI()
    demo.show()
    sys.exit(app.exec_())