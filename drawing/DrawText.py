# -*- encoding: utf-8 -*-
"""
@File    : DrawText.py
@Time    :  2019/12/26 23:22
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    绘图API:绘制文本
    1.文本
    2.各种图形（直线，点，椭圆，弧，扇形，多边形等）
    3.图像
    QPainter
    painter = QPainter()
    painter.begin()
    painter.drawText()
    painter.end()
    必须在paintEvent事件方法中绘制各种元素
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __int__(self):
        super(DrawText, self).__int__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 200)
        self.text = "Python从菜鸟到高手"

    def paintEngine(self, even):
        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSun', 25))

        painter.drawText(even.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())
