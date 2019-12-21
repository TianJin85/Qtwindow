# -*- encoding: utf-8 -*-
"""
@File    : QLabelBuddy.py
@Time    :  2019/12/21 21:54
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
QLabel与伙伴控件
mainLayout.addWidget(控件对象，rowIndex,columnIndex,row,column)
'''
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLableBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')
        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLableBuddy()
    main.show()
    sys.exit(app.exec_())
