# -*- encoding: utf-8 -*-
"""
@File    : runmainwinhorizontallayout.py
@Time    :  2019/12/13 22:44
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

import sys
import mainwinverticallayout

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = mainwinverticallayout.Ui_MainWindow()
    # 向窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
