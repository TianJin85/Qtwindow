# -*- encoding: utf-8 -*-
"""
@File    : ListView.py
@Time    :  2019/12/28 22:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QListView, QMessageBox
from PyQt5.QtCore import QStringListModel


class ListViewDemo(QWidget):

    def __int__(self, parent=None):
        super(ListViewDemo, self).__int__(parent)

    def initUI(self):
        self.setWindowTitle("QlistView例子")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listview = QListView()
        listModel = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.initUI()
    win.show()
    sys.exit(app.exec_())


