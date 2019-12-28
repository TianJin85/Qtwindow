# -*- encoding: utf-8 -*-
"""
@File    : Toolbar.py
@Time    :  2019/12/28 15:51
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    创建和使用工具栏
    工具栏默认按钮：只显示图标，将文本作为悬停提示展示
    工具栏按钮有3种显示状态
    1.只显示图标
    2.只显示文本
    3.同时显示文本和图标
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Toolbar(QMainWindow):
    def __int__(self):
        super(Toolbar, self).__int__()

    def initUI(self):
        self.setWindowTitle("工具栏列子")
        self.resize(300, 200)

        tbl = self.addToolBar("File")
        new = QAction(QIcon(r'./images/首页-选中 (2).png'), "new", self)
        tbl.addAction(new)

        open = QAction(QIcon(r'./images/开锁icon 打开.png'), "opne", self)
        tbl.addAction(open)

        save = QAction(QIcon(r'./images/下载 保存 存储 线性.png'), "save", self)
        tbl.addAction(save)

        # tbl.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)   # 文字和图标都显示
        tb2 = self.addToolBar("File1")
        new1 = QAction(QIcon(r'./images/首页-选中 (2).png'), "新建", self)
        tb2.addAction(new1)

        tb2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        tbl.actionTriggered.connect(self.toolbtnpressed)

        tb2.actionTriggered.connect(self.toolbtnpressed)


    def toolbtnpressed(self, a):
        print("按下的工具栏按钮", a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.initUI()
    main.show()
    sys.exit(app.exec_())