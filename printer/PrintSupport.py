# -*- encoding: utf-8 -*-
"""
@File    : PrintSupport.py
@Time    :  2019/12/28 16:43
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

import sys
from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *



class PrintSupport(QWidget):
    def __int__(self):
        super(PrintSupport, self).__int__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容')
        self.button.setGeometry(20, 20, 260, 30)
        self.editor = QTextEdit('默认文本', self)
        self.editor.setGeometry(20, 60, 260, 200)

        self.button.clicked.connect(self.print)


    def print(self):
        printer = QtPrintSupport.QPrinter()

        painter = QtGui.QPainter()
        painter.begin(printer)
        screen =self.editor.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PrintSupport()
    main.show()
    sys.exit(app.exec_())