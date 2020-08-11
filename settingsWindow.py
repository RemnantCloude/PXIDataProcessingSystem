# -*- coding: UTF-8 -*-
# @file    :settingsWindow.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-06
# @description:

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox, QTextEdit, QGridLayout, QLabel, QComboBox, QPushButton

# import nidaqmx.system

from settings import Settings

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsStyle()
        self.setThisLayout()
        self.scanChannels()
        self.sampleModeChange()

    def initComponents(self):
        self.__channelsLab = QLabel("通道选择")
        self.__channelsCob = QComboBox()
        # self.__refreshChannelsBtn = QPushButton("刷新") # TODO
        self.__readPXIDataControlBtn = QPushButton("开始读取")

        self.__sampleFreqLab = QLabel("采样频率")
        self.__sampleFreqTxt = QTextEdit()

        self.__sampleModeLab = QLabel("采样模式")
        self.__sampleModeCob = QComboBox()

        self.__samplesPerChanLab = QLabel()
        self.__samplesPerChanTxt = QTextEdit()
        self.__samplesPerChanCob = QComboBox()

        self.__maxValLab = QLabel("最大电压值")
        self.__maxValTxt = QTextEdit()

        self.__minValLab = QLabel("最小电压值")
        self.__minValTxt = QTextEdit()

        self.__couplingLab = QLabel("耦合方式")
        self.__couplingCob = QComboBox()

        self.__activeEdgeLab = QLabel("边沿触发")
        self.__activeEdgeCob = QComboBox()


        self.__LPFChk = QCheckBox("低通滤波")
        self.__tenTimesMeasureChk = QCheckBox("十次测量")

        self.__HCutoffFreqLab = QLabel("高截止频率")
        self.__HCutoffFreqTxt = QTextEdit()
        self.__HCutoffFreqCob = QComboBox()

        self.__LCutoffFreqLab = QLabel("低截止频率")
        self.__LCutoffFreqTxt = QTextEdit()
        self.__LCutoffFreqCob = QComboBox()

        self.__deletePeriodsLab = QLabel("删除周期数")
        self.__deletePeriodsTxt = QTextEdit()  # TODO 带下拉菜单？
        self.__zoomInTimesLab = QLabel("放大倍数")
        self.__zoomInTimesTxt = QTextEdit()  # TODO 带下拉菜单？

        self.__layout = QGridLayout()

    def initSignalAndSlot(self):
        self.__channelsCob.activated.connect(self.refreshData)
        self.__sampleModeCob.activated.connect(self.sampleModeChange)
        # self.__refreshChannelsBtn.clicked.connect(self.refreshChannels)
        self.__readPXIDataControlBtn.clicked.connect(self.readPXIData)

    def setComponentsStyle(self):
        self.__channelsCob.setFixedSize(80, 21)

        self.__sampleFreqTxt.setFixedSize(60, 25)
        self.__sampleModeCob.setFixedSize(80, 25)
        self.__samplesPerChanTxt.setFixedSize(60, 25)
        self.__samplesPerChanCob.setFixedSize(45, 25)

        self.__HCutoffFreqTxt.setFixedSize(60, 25)
        self.__HCutoffFreqCob.setFixedSize(45, 25)

        self.__LCutoffFreqTxt.setFixedSize(60, 25)
        self.__LCutoffFreqCob.setFixedSize(45, 25)

        self.__deletePeriodsTxt.setFixedSize(60, 25)
        self.__zoomInTimesTxt.setFixedSize(60, 25)

        self.__sampleModeCob.addItems(["有限采样", "持续采样"])
        self.__samplesPerChanCob.addItems(["", "K", "M"])
        self.__couplingCob.addItems(["AC", "DC", "GND"])
        self.__activeEdgeCob.addItems(["上升沿", "下降沿"])
        self.__HCutoffFreqCob.addItems(["Hz", "KHz", "MHz"])
        self.__LCutoffFreqCob.addItems(["Hz", "KHz", "MHz"])

    def setThisLayout(self):  # TODO
        self.__layout.addWidget(self.__channelsLab, 0, 0, 1, 1)
        self.__layout.addWidget(self.__channelsCob, 0, 1, 1, 1)
        self.__layout.addWidget(self.__readPXIDataControlBtn, 0, 2, 1, 1)

        self.__layout.addWidget(self.__sampleFreqLab, 1, 0, 1, 1)
        self.__layout.addWidget(self.__sampleFreqTxt, 1, 1, 1, 1)

        self.__layout.addWidget(self.__sampleModeLab, 2, 0, 1, 1)
        self.__layout.addWidget(self.__sampleModeCob, 2, 1, 1, 1)

        self.__layout.addWidget(self.__samplesPerChanLab, 3, 0, 1, 1)
        self.__layout.addWidget(self.__samplesPerChanTxt, 3, 1, 1, 1)
        self.__layout.addWidget(self.__samplesPerChanCob, 3, 2, 1, 1)

        self.__layout.addWidget(self.__maxValLab, 4, 0, 1, 1)
        self.__layout.addWidget(self.__maxValTxt, 4, 1, 1, 1)

        self.__layout.addWidget(self.__minValLab, 5, 0, 1, 1)
        self.__layout.addWidget(self.__minValTxt, 5, 1, 1, 1)

        self.__layout.addWidget(self.__couplingLab, 6, 0, 1, 1)
        self.__layout.addWidget(self.__couplingCob, 6, 1, 1, 1)

        self.__layout.addWidget(self.__activeEdgeLab, 7, 0, 1, 1)
        self.__layout.addWidget(self.__activeEdgeCob, 7, 1, 1, 1)

        self.__layout.addWidget(self.__LPFChk, 8, 0, 1, 1)
        self.__layout.addWidget(self.__tenTimesMeasureChk, 8, 1, 1, 1)

        self.__layout.addWidget(self.__HCutoffFreqLab, 9, 0, 1, 1)
        self.__layout.addWidget(self.__HCutoffFreqTxt, 9, 1, 1, 1)
        self.__layout.addWidget(self.__HCutoffFreqCob, 9, 2, 1, 1)

        self.__layout.addWidget(self.__LCutoffFreqLab, 10, 0, 1, 1)
        self.__layout.addWidget(self.__LCutoffFreqTxt, 10, 1, 1, 1)
        self.__layout.addWidget(self.__LCutoffFreqCob, 10, 2, 1, 1)

        self.__layout.addWidget(self.__deletePeriodsLab, 11, 0, 1, 1)
        self.__layout.addWidget(self.__deletePeriodsTxt, 11, 1, 1, 1)

        self.__layout.addWidget(self.__zoomInTimesLab, 12, 0, 1, 1)
        self.__layout.addWidget(self.__zoomInTimesTxt, 12, 1, 1, 1)
        
        self.setLayout(self.__layout)
        self.setMaximumSize(250, 400)

    def scanChannels(self):
        self.__channelsCob.addItem("Dev1/ai0")
        self.__channelsCob.addItem("Dev1/ai1")
        self.__channelsCob.addItem("Dev1/ai2")

        # Settings.writeChannels()
        # pass# TODO 等待测试

    def sampleModeChange(self):
        if self.__sampleModeCob.currentText() == "有限采样":
            self.__samplesPerChanLab.setText("采样样本数")
        else:
            self.__samplesPerChanLab.setText("缓冲区样本数")
        #TODO 改变模式

    def readPXIData(self):
        if self.__readPXIDataControlBtn.text() == "开始读取":
            self.__readPXIDataControlBtn.setText("停止读取")
            # TODO
        else:
            self.__readPXIDataControlBtn.setText("开始读取")

    # def refreshChannels(self):
    #     pass

    def refreshData(self):
        # self.__LCutoffFreqTxt.setText("fxxk")
        pass
