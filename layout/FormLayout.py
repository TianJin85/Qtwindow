# -*- encoding: utf-8 -*-
"""
@File    : FormLayout.py
@Time    :  2020/1/8 20:58
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    表单布局（QFormLayout）
'''
import sys
from PyQt5.QtWidgets import *


class FormForm(QWidget):
    def __init__(self):
        super(FormForm, self).__init__()

    def initUI(self):
        self.setWindowTitle("表单布局")
        self.resize(350, 300)

        formLayout = QFormLayout()

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        formLayout.addRow(titleLabel, titleEdit)
        formLayout.addRow(authorLabel, authorEdit)
        formLayout.addRow(contentLabel, contentEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormForm()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

