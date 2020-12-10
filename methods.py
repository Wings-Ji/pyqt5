# -*- coding: utf-8 -*-
"""
Project: QtTest2
Creator: tianx
Create time: 2020-12-07 10:24
IDE: PyCharm
Introduction:这里放所有逻辑代码
"""
import sys
from PyQt5.QtCore import QFile
from PyQt5.Qt import QDesktopServices, QUrl
from PyQt5.QtWidgets import QFileDialog, QWidget

def chooseFile(self):
    try:
        openfile_name = QFileDialog.getOpenFileName(self,"请选择Excel文件",'','Excel files(*.xlsx , *.xls)')
        self.fileName.setText(openfile_name[0])
    except Exception as e:
        print(e)

def openExcelfile(self):
    try:
        fileName = 'templete.xls'
        filePath = ''.join([sys.path[0],r'\resource\\',fileName])
        if not QFile(filePath).exists():
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(filePath)) #打开模板文件
    except Exception as e:
        print(e)