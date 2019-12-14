# -*- encoding: utf-8 -*-
"""
@File    : runmainwingridlayout.py
@Time    :  2019/12/14 15:20
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
import mainwingridlayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = mainwingridlayout.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())