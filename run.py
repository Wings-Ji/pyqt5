# -*- coding: utf-8 -*- 
"""
Project: QtTest2
Creator: tianx
Create time: 2020-12-03 16:06
IDE: PyCharm
Introduction:
"""
"""
主程序入口
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app.MyAppWin import Ui_MainWindow
from app import methods

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def chooseFile(self):
        methods.chooseFile(self)

    def openExcelfile(self):
        methods.openExcelfile(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
