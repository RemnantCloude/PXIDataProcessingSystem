# -*- coding: UTF-8 -*-
# @file    :resultWindow.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-07
# @description:

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit, QGridLayout, QLabel


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsStyle()
        self.setThisLayout()

    def initComponents(self):
        self.__disLab = QLabel("位移(nm)")
        self.__disTxt = QTextEdit("0")
        self.__VelLab = QLabel("速度(m/s)")
        self.__VelTxt = QTextEdit("0")
        self.__accLab = QLabel("加速度(m/s2)")
        self.__accTxt = QTextEdit("0")
        self.__THDLab = QLabel("THD(%)") # TODO 这是啥玩意
        self.__THDTxt = QTextEdit("0")
        self.__ampLab = QLabel("幅值(mV)")
        self.__ampTxt = QTextEdit("0")
        self.__phaLab = QLabel("相位(deg)")
        self.__phaTxt = QTextEdit("0")
        self.__senLab = QLabel("灵敏度(mV/m/s2)")
        self.__senTxt = QTextEdit("0")
        # self.__ = QLabel("THD(%)") # TODO 同一个东西？？
        # self.__ = QTextEdit("0")

        self.__disTxt.setReadOnly(True)
        self.__VelTxt.setReadOnly(True)
        self.__accTxt.setReadOnly(True)
        self.__THDTxt.setReadOnly(True)
        self.__ampTxt.setReadOnly(True)
        self.__phaTxt.setReadOnly(True)
        self.__senTxt.setReadOnly(True)

        self.__layout = QGridLayout()

    def initSignalAndSlot(self):
        pass

    def setComponentsStyle(self):
        self.__disTxt.setFixedSize(60, 25)
        self.__VelTxt.setFixedSize(60, 25)
        self.__accTxt.setFixedSize(60, 25)
        self.__THDTxt.setFixedSize(60, 25)
        self.__ampTxt.setFixedSize(60, 25)
        self.__phaTxt.setFixedSize(60, 25)
        self.__senTxt.setFixedSize(60, 25)

    def setThisLayout(self):
        self.__layout.addWidget(self.__disLab, 0, 0, 1, 1)
        self.__layout.addWidget(self.__disTxt, 0, 1, 1, 1)
        self.__layout.addWidget(self.__VelLab, 1, 0, 1, 1)
        self.__layout.addWidget(self.__VelTxt, 1, 1, 1, 1)
        self.__layout.addWidget(self.__accLab, 2, 0, 1, 1)
        self.__layout.addWidget(self.__accTxt, 2, 1, 1, 1)
        self.__layout.addWidget(self.__ampLab, 3, 0, 1, 1)
        self.__layout.addWidget(self.__ampTxt, 3, 1, 1, 1)
        self.__layout.addWidget(self.__phaLab, 4, 0, 1, 1)
        self.__layout.addWidget(self.__phaTxt, 4, 1, 1, 1)
        self.__layout.addWidget(self.__senLab, 5, 0, 1, 1)
        self.__layout.addWidget(self.__senTxt, 5, 1, 1, 1)
        self.__layout.addWidget(self.__THDLab, 6, 0, 1, 1)
        self.__layout.addWidget(self.__THDTxt, 6, 1, 1, 1)

        self.setLayout(self.__layout)
        self.setMaximumSize(200, 200)
