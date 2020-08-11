# -*- coding: UTF-8 -*-
# @file    :displayWindow.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-07
# @description:

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from figure import MyFigure

class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsStyle()
        self.setThisLayout()

    def initComponents(self):
        self.__figure = MyFigure()

        self.__layout = QGridLayout()

    def initSignalAndSlot(self):
        pass

    def setComponentsStyle(self):
        pass

    def setThisLayout(self):
        self.__layout.addWidget(self.__figure, 0, 0, 1, 1)
        self.setLayout(self.__layout)
