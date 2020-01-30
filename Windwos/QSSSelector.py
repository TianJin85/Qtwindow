# -*- encoding: utf-8 -*-
"""
@File    : QSSSelector.py
@Time    :  2020/1/30 10:22
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    使用QSS选择器设置控件样式
'''
import sys
from PyQt5.QtWidgets import *


class QSSSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS样式")
        btn1 = QPushButton(self)
        btn1.setText("按钮1")
        btn2 = QPushButton(self)
        btn2.setProperty('name', 'btn2')
        btn2.setText("按钮2")

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QSSSelector()
    # 选择器
    qssStyle = '''
        QPushButton[name="btn2"] {
            background-color:red;
            color:yellow;
            height:120;
            font-size:60px;
        }
    '''
    form.setStyleSheet(qssStyle)
    form.show()
    sys.exit(app.exec_())
