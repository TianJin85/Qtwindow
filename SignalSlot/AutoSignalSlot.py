# -*- encoding: utf-8 -*-
"""
@File    : AutoSignalSlot.py
@Time    :  2020/1/14 22:13
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    信号与槽自动连接
    on_objectname_signalname
    on_okButton_clicked
'''
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton('OK', self)
        self.okButton.setObjectName("okButton")

        self.okButton = QPushButton('cancel', self)
        self.okButton.setObjectName("cancelButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        # self.okButton.clicked.connect(self.on_okButton_clicked)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setLayout(layout)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cance按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()
    sys.exit(app.exec_())

