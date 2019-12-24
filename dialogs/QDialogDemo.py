# -*- encoding: utf-8 -*-
"""
@File    : QDialogDemo.py
@Time    :  2019/12/24 22:43
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    对话框：QDialog
    
    QMessageBoxs
    QColorDialog
    QFileDialog
    QFontDialog
    QFontDialog
    QInputDialog
    
    QMainWindow
    QWidget
    QDialog
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QDialogDemo(QMainWindow):
    def __int__(self):
        super(QDialogDemo, self).__int__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QDialog")
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):

        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.initUI()
    main.show()
    sys.exit(app.exec_())