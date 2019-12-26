# -*- encoding: utf-8 -*-
"""
@File    : QFontDialog.py
@Time    :  2019/12/26 19:08
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QFontDialogDemo(QWidget):
    def __int__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Font Dialog列子')
        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLabel = QLabel("Hello 测试字体列子")
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())
