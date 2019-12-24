# -*- encoding: utf-8 -*-
"""
@File    : QSpinBoxDemo.py
@Time    :  2019/12/24 22:14
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
# 计数控件（QSpinBox）
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSpinBoxDemo(QWidget):
    def __int__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QSpinBox演示")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(18)
        self.sb.setRange(10, 38)
        self.sb.setSingleStep(3)
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.vlaueChange)
        self.setLayout(layout)

    def vlaueChange(self):
        self.label.setText('当前值：' + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())