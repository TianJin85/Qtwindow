# -*- encoding: utf-8 -*-
"""
@File    : Splitter.py
@Time    :  2020/1/8 21:08
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from PyQt5.QtCore import Qt

'''
    拖动控件之间的边界（QSplitter）
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle('QSplitter 列子')
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Splitter()
    main.initUI()
    main.show()
    sys.exit(app.exec_())

