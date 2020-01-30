# -*- encoding: utf-8 -*-
"""
@File    : QSSSubControl.py
@Time    :  2020/1/30 10:34
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    QSS子控件选择器
    
    QComboBox
'''
import sys
from PyQt5.QtWidgets import *

class QSSSubControl(QWidget):
    def __init__(self):
        super(QSSSubControl, self).__init__()
        self.setWindowTitle("QSS子控件选择器")
        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItem("Window")
        combo.addItem("Linux")
        combo.addItem("Mac OS")

        combo.move(50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSSSubControl()
    qssStyle = """
        QComboBox#myComboBox::drop-down{
            image:url(./images/dropdown.png)
        }
    """
    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec_())