# -*- encoding: utf-8 -*-
"""
@File    : Drawing.py
@Time    :  2020/1/30 0:42
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
项目实战:实现绘图应用
需要解决3个核心内容
1.如何绘图

在paintEvent方法中绘图，通过调用update方法触发painEvent的调用

2.在哪里绘图
在白色背景QPixmap对象中绘图

3.如何通过移动鼠标进行绘图
鼠标拥有3个事件
（1）鼠标按下:mousePressEvent
（2）鼠标移动:
（3）鼠标抬起
'''