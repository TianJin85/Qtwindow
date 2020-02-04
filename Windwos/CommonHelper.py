# -*- encoding: utf-8 -*-
"""
@File    : CommonHelper.py
@Time    :  2020/2/4 23:13
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""


class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style, 'r') as f:
            return f.read()
