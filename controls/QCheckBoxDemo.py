# -*- encoding: utf-8 -*-
"""
@File    : QCheckBoxDemo.py
@Time    :  2019/12/24 20:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    复选框控件
    
    3种转态
    
    未选中
    
    选中    
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class QCheckBoxDemo(QWidget):
    def __int__(self):
        super(QCheckBoxDemo, self).__init__()
        self.iniUI()

    def initUI(self):
        self.setWindowTitle("复选框控件演示")

        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("复选框1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("复选框2")
        self.checkBox2.stateChanged.connect(lambda: self.checkBoxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("半选中")
        self.checkBox3.stateChanged.connect(lambda: self.checkBoxState(self.checkBox3))
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def checkBoxState(self, cd):
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + 'chechState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + 'chechState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + 'chechState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status, check2Status, check3Status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())












