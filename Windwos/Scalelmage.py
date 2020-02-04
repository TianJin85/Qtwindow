# -*- encoding: utf-8 -*-
"""
@File    : Scalelmage.py
@Time    :  2020/2/4 22:09
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

'''
    缩放图片
    QImage.scaled
'''


class ScaleImage(QWidget):
    def __init__(self):
        super(ScaleImage, self).__init__()
        self.setWindowTitle("图片放大缩小的例子")
        filename = './images/Cloudy_72px.png'
        img = QImage(filename)
        label1 = QLabel(self)
        label1.setFixedHeight(200)
        label1.setFixedWidth(200)

        result = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label1)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScaleImage()
    main.show()
    sys.exit(app.exec_())
