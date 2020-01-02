# -*- encoding: utf-8 -*-
"""
@File    : ScrllBar.py
@Time    :  2020/1/2 22:25
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollBar(QWidget):
    def __int__(self):
        super(ScrollBar, self).__int__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条去改变颜色')

        hbox.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMover)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMover)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMover)

        hbox.addWidget(self.scrollbar1)
        hbox.addWidget(self.scrollbar2)
        hbox.addWidget(self.scrollbar3)

        self.setGeometry(300, 300, 300, 200)

        self.setLayout(hbox)

    def sliderMover(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        palette = QPalette()
        c = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ScrollBar()
    demo.initUI()
    demo.show()
    sys.exit(app.exec_())

