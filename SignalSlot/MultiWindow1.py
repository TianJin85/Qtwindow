# -*- encoding: utf-8 -*-
"""
@File    : MultiWindow1.py
@Time    :  2020/1/15 22:30
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog import DateDialog


class MultWindow1(QWidget):
    def __init__(self, parent=None):
        super(MultWindow1, self).__init__(parent)
        self.setWindowTitle("多窗口交互（1）：不使用信号与槽")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.noButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog()
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def noButton2Click(self):
        date, item, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('单击取消按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MultWindow1()
    form.show()
    sys.exit(app.exec_())
