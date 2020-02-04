# -*- encoding: utf-8 -*-
"""
@File    : OpacityWindow.py
@Time    :  2020/2/4 23:03
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    创建透明窗口
'''
import sys
from PyQt5.Qt import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle('窗口的透明读设置')
    win.setWindowOpacity(0.5)
    but = QPushButton("我的按钮", win)
    win.show()
    sys.exit(app.exec_())
