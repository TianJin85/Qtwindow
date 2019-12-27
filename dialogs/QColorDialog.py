# -*- encoding: utf-8 -*-
"""
@File    : QColorDialog.py
@Time    :  2019/12/26 19:25
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QColorDialogDemo(QWidget):
    def __int__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Color Dialog列子')
        layout = QVBoxLayout()
        self.ColorButton = QPushButton('设置颜色')
        self.ColorButton.clicked.connect(self.getColor)
        layout.addWidget(self.ColorButton)

        self.ColorButton1 = QPushButton('设置背景颜色')
        self.ColorButton1.clicked.connect(self.getBGColory)
        layout.addWidget(self.ColorButton1)

        self.ColorLabel = QLabel("Hello 测试颜色列子")
        layout.addWidget(self.ColorLabel)

        self.setLayout(layout)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.ColorLabel.setPalette(p)

    def getBGColory(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.ColorLabel.setAutoFillBackground(True)
        self.ColorLabel.setPalette(p)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())


