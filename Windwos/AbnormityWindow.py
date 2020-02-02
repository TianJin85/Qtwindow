# -*- encoding: utf-8 -*-
"""
@File    : AbnormityWindow.py
@Time    :  2020/1/30 11:39
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    实现不规则窗口(异形窗口)
    通过mask实现异形窗口
    需要一张透明png图片，透明部分被扣出，形成一个非矩形的区域
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()
        self.setWindowTitle('异形窗口')
        self.pix = QBitmap('./images/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap('./images/screen1.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbnormityWindow()
    main.show()
    sys.exit(app.exec_())