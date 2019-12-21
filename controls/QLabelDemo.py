# -*- encoding: utf-8 -*-
"""
@File    : QLabelDemo.py
@Time    :  2019/12/21 20:50
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
QLabel 控件
    
    setAlignment():设置文本的对齐方式
    
    setIndent():设置文本缩进
    
    test():获取文本内容
    
    setBuddy():设置伙伴关系
    
    setText():设置文本内容
    
    setWordWrap():设置是否允许换行
    
    QLable常用的信号（事件）
    1.当鼠标滑过QLable控件时触发：linkHovered
    2.当鼠标单击QLable控件时触发：linkActivated
    
'''

import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签。</>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")
        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')

        label3.setPixmap(QPixmap("./images/python.png"))
        # 如果设为True用浏览器打开
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignRight)

        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

    def linkHovered(self):
        print('当鼠标滑过label2标签是，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())




