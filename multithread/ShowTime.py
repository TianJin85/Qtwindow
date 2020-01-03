# -*- encoding: utf-8 -*-
"""
@File    : ShowTime.py
@Time    :  2020/1/3 22:06
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    动态显示当前时间
    QTimer
    QThread
    多线程：用于同时完成多个任务
'''
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTime, QDateTime, QTimer


class ShowTime(QWidget):

    def __int__(self, parent=None):
        super(ShowTime, self).__int__()

    def initUI(self):
        self.setWindowTitle("动态显示当前时间")

        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')

        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ShowTime()
    form.initUI()
    form.show()
    sys.exit(app.exec_())
