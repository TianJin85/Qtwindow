# -*- encoding: utf-8 -*-
"""
@File    : centereform.py
@Time    :  2019/12/19 21:49
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterFrom(QMainWindow):
    def __init__(self,parent=None):
        super(CenterFrom, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("让窗口居中")

        self.resize(400, 300)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterFrom()
    main.show()
    sys.exit(app.exec_())

