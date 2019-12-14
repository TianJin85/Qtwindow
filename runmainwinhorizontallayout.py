# -*- encoding: utf-8 -*-
"""
@File    : runmainwinhorizontallayout.py
@Time    :  2019/12/14 15:10
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
import mainwinhorizontallayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainwinhorizontallayout.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
