# -*- encoding: utf-8 -*-
"""
@File    : DateDialog.py
@Time    :  2020/1/15 22:17
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):
    def __init__(self):
        super(DateDialog, self).__init__()
        self.setWindowTitle("DateDialog")

        layout = QVBoxLayout(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return (date.date(), date.time(), result==QDialog.Accepted)