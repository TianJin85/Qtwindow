# -*- encoding: utf-8 -*-
"""
@File    : CustomSignal.py
@Time    :  2020/1/8 21:50
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
'''
    自定义信号
    pyqtSignal()
'''

from PyQt5.QtCore import *


class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    def run(self):
        self.sendmsg.emit('Hello PyQt5')


class MySlot(QObject):
    def get(self, msg):
        print("信息："+ msg)


if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()

    send.sendmsg.connect(slot.get)

    send.run()
    send.sendmsg.disconnect(slot.get)       # 断开连接
    send.run()



    send.run()