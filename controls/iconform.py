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

"""
    窗口的setWindowIcon的方法用于设置窗口的图标，只在Windows中可用
    QAplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标，但调用了窗口的setWindowIcon方法
"""


class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")
        # 设置窗口图标
        self.setWindowIcon(QIcon('./images/Bart_Simpson_Bartman_128px_1134096_easyicon.net.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/Bart_Simpson_Bartman_128px_1134096_easyicon.net.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())

