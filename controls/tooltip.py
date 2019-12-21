# -*- encoding: utf-8 -*-
"""
@File    : tooltip.py
@Time    :  2019/12/21 20:21
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期六</b>')
        self.setGeometry(300, 30, 200, 300)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮，Are you ok?')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())