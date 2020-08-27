# -*- coding: UTF-8 -*-
# @file    :system.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-06
# @description:

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout

from settingsWindow import SettingsWindow
from resultWindow import ResultWindow
from displayWindow import DisplayWindow
from reviseWindow import ReviseWindow

class MeasureSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsLayout()
        self.setComponentsStyle()
        self.initWindowStyle()
    
    def initComponents(self):
        self.__settingsWindow = SettingsWindow()
        self.__resultWindow = ResultWindow()
        self.__displayWindow = DisplayWindow()
        self.__reviseWindow = ReviseWindow()

        self.__layout = QGridLayout()

    def initSignalAndSlot(self):
        self.__settingsWindow.signalReadPXIData.connect(self.__displayWindow.figure.setAxes)

    def setComponentsLayout(self):
        self.__layout.addWidget(self.__settingsWindow, 0, 0, 1, 1)
        self.__layout.addWidget(self.__resultWindow, 1, 0, 1, 1)
        self.__layout.addWidget(self.__displayWindow, 0, 1, 2, 2)
        self.__layout.addWidget(self.__reviseWindow, 2, 0, 1, 2)
        self.setLayout(self.__layout)

    def setComponentsStyle(self):
        pass

    def initWindowStyle(self):
        self.setMinimumSize(1000, 800)
        self.resize(1000, 800)
