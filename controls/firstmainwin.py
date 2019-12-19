# -*- encoding: utf-8 -*-
"""
@File    : firstmainwin.py.py
@Time    :  2019/12/19 21:07
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle("这是我的第一个主窗口")

        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage("消息只存在5秒", 18)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Bart_Simpson_Bartman_128px_1134096_easyicon.net.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())

