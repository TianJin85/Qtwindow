# -*- encoding: utf-8 -*-
"""
@File    : ListWidget.py
@Time    :  2019/12/28 23:12
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    扩展的列表控件（QListWidget）
    QListView
'''
import sys
from PyQt5.QtWidgets import *


class ListWidgetDemo(QMainWindow):
    def __int__(self, parent=None):
        super(ListWidgetDemo, self).__int__(parent)

    def initUI(self):
        self.setWindowTitle("QListWidget例子")
        self.resize(300, 270)
        self.listwidget = QListWidget()
        self.listwidget.resize(300, 120)
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        self.listwidget.addItem("item4")
        self.listwidget.addItem("item5")
        self.listwidget.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidget)

    def clicked(self, Index):
        QMessageBox.information(self, "QListWidget", "您选择了：" + self.listwidget.item(self.listwidget.row(Index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ListWidgetDemo()
    win.initUI()
    win.show()
    sys.exit(app.exec_())

