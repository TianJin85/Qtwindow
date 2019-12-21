# -*- encoding: utf-8 -*-
"""
@File    : screengeometry.py
@Time    :  2019/12/20 21:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget

app = QApplication(sys.argv)


def onClick_Button():
    print("1")
    print("widget.x() = %d" % widget.x())
    print("widget.y() = %d" % widget.y())
    print("widget.width() = %d" % widget.width())
    print("widget.height() = %d" % widget.height())

    print("2")
    print("widget.frameGeometry().x() = %d" % widget.geometry().x())
    print("widget.geometry().y() = %d" % widget.geometry().width())
    print("widget.geometry().height() = %d" %widget.geometry().height())

    print("3")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("widget.frameGeometry.y() = %d" % widget.frameGeometry().width())
    print("widget.frameGeometry.height() = %d" % widget.frameGeometry().height())

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24, 52)

widget.resize(300, 240)
widget.setWindowTitle("屏幕坐标")
widget.show()
sys.exit(app.exec_())

