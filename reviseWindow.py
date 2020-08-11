# -*- coding: UTF-8 -*-
# @file    :reviseWindow.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-10
# @description:

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QGridLayout

class ReviseWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsStyle()
        self.setThisLayout()

    def initComponents(self):
        self.__table = QTableWidget()
        self.__table.setColumnCount(1)
        self.__table.setRowCount(1)
        self.__table.setRowHeight(0, 50)
        self.__table.setColumnWidth(0, 50)

        self.__layout = QGridLayout()

    def initSignalAndSlot(self):
        pass

    def setComponentsStyle(self):
        pass

    def setThisLayout(self):
        self.__layout.addWidget(self.__table)
        self.setLayout(self.__layout)
