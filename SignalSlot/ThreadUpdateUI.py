# -*- encoding: utf-8 -*-
"""
@File    : ThreadUpdateUI.py
@Time    :  2020/1/12 12:45
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    多线程更新UI数据(二个线程之间传递数据)
'''
import time
import sys
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(str(currentTime))
            time.sleep(1)


class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)

        self.initUI()

    def initUI(self):

        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateUI()
    main.show()
    sys.exit(app.exec_())