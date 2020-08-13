# -*- coding: UTF-8 -*-
# @file    :settingsWindow.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-06
# @description:
# TODO 支持扫描通道

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox, QTextEdit, QGridLayout, QLabel, QComboBox, QPushButton, QMessageBox
from nidaqmx.stream_readers import AnalogSingleChannelReader
from nidaqmx.constants import Edge, AcquisitionType, Coupling, VoltageUnits, TerminalConfiguration
# import nidaqmx.system

from settings import Settings

coupling = {"AC": Coupling.AC, "DC": Coupling.DC, "GND": Coupling.GND}
edge = {"上升沿": Edge.RISING, "下降沿": Edge.FALLING}
acquisitiontype = {
    "有限采样": AcquisitionType.FINITE,
    "持续采样": AcquisitionType.CONTINUOUS}

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initSignalAndSlot()
        self.setComponentsStyle()
        self.setThisLayout()

        self.__settings = Settings()
        self.readSettings()
        # self.scanChannels()
        self.sampleModeChange()

    def initComponents(self):
        self.__channelsLab = QLabel("通道")
        self.__channelsTxt = QTextEdit()
        self.__readPXIDataControlBtn = QPushButton("开始读取")

        self.__sampleFreqLab = QLabel("采样频率")
        self.__sampleFreqTxt = QTextEdit()

        self.__sampleModeLab = QLabel("采样模式")
        self.__sampleModeCob = QComboBox()

        self.__samplesPerChanLab = QLabel()
        self.__samplesPerChanTxt = QTextEdit()

        self.__maxValLab = QLabel("采样最大值")
        self.__maxValTxt = QTextEdit()

        self.__minValLab = QLabel("采样最小值")
        self.__minValTxt = QTextEdit()

        self.__couplingLab = QLabel("耦合方式")
        self.__couplingCob = QComboBox()

        self.__activeEdgeLab = QLabel("边沿触发")
        self.__activeEdgeCob = QComboBox()

        self.__writeSettingsBtn = QPushButton("保存设置")


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
        # self.__channelsTxt.textChanged.connect(self.writeChannels)
        # self.__sampleFreqTxt.textChanged.connect(self.writeSampleFreq)
        # self.__sampleModeCob.activated.connect(self.writeSampleMode)
        # self.__samplesPerChanTxt.textChanged.connect(self.writeSamplesPerChan)
        # self.__maxValTxt.textChanged.connect(self.writeMaxVal)
        # self.__minValTxt.textChanged.connect(self.writeMinVal)
        # self.__couplingCob.activated.connect(self.writeCoupling)
        # self.__activeEdgeCob.activated.connect(self.writeActiveEdge)

        # self.__sampleModeCob.activated.connect(self.sampleModeChange)
        # self.__refreshChannelsBtn.clicked.connect(self.refreshChannels)
        self.__readPXIDataControlBtn.clicked.connect(self.readPXIData)
        self.__writeSettingsBtn.clicked.connect(self.writeSettings)

    def setComponentsStyle(self):
        self.__sampleFreqTxt.setFixedSize(60, 25)
        self.__sampleModeCob.setFixedSize(80, 25)
        self.__samplesPerChanTxt.setFixedSize(60, 25)

        self.__HCutoffFreqTxt.setFixedSize(60, 25)
        self.__HCutoffFreqCob.setFixedSize(45, 25)

        self.__LCutoffFreqTxt.setFixedSize(60, 25)
        self.__LCutoffFreqCob.setFixedSize(45, 25)

        self.__deletePeriodsTxt.setFixedSize(60, 25)
        self.__zoomInTimesTxt.setFixedSize(60, 25)

        self.__sampleModeCob.addItems(["有限采样", "持续采样"])
        self.__couplingCob.addItems(["AC", "DC", "GND"])
        self.__activeEdgeCob.addItems(["上升沿", "下降沿"])
        self.__HCutoffFreqCob.addItems(["Hz", "KHz", "MHz"])
        self.__LCutoffFreqCob.addItems(["Hz", "KHz", "MHz"])

    def setThisLayout(self):
        self.__layout.addWidget(self.__channelsLab, 0, 0, 1, 1)
        self.__layout.addWidget(self.__channelsTxt, 0, 1, 1, 1)
        self.__layout.addWidget(self.__readPXIDataControlBtn, 0, 2, 1, 1)

        self.__layout.addWidget(self.__sampleFreqLab, 1, 0, 1, 1)
        self.__layout.addWidget(self.__sampleFreqTxt, 1, 1, 1, 1)

        self.__layout.addWidget(self.__sampleModeLab, 2, 0, 1, 1)
        self.__layout.addWidget(self.__sampleModeCob, 2, 1, 1, 1)

        self.__layout.addWidget(self.__samplesPerChanLab, 3, 0, 1, 1)
        self.__layout.addWidget(self.__samplesPerChanTxt, 3, 1, 1, 1)

        self.__layout.addWidget(self.__maxValLab, 4, 0, 1, 1)
        self.__layout.addWidget(self.__maxValTxt, 4, 1, 1, 1)

        self.__layout.addWidget(self.__minValLab, 5, 0, 1, 1)
        self.__layout.addWidget(self.__minValTxt, 5, 1, 1, 1)

        self.__layout.addWidget(self.__couplingLab, 6, 0, 1, 1)
        self.__layout.addWidget(self.__couplingCob, 6, 1, 1, 1)

        self.__layout.addWidget(self.__activeEdgeLab, 7, 0, 1, 1)
        self.__layout.addWidget(self.__activeEdgeCob, 7, 1, 1, 1)

        self.__layout.addWidget(self.__writeSettingsBtn, 8, 1, 1, 1)

        self.__layout.addWidget(self.__LPFChk, 9, 0, 1, 1)
        self.__layout.addWidget(self.__tenTimesMeasureChk, 9, 1, 1, 1)

        self.__layout.addWidget(self.__HCutoffFreqLab, 10, 0, 1, 1)
        self.__layout.addWidget(self.__HCutoffFreqTxt, 10, 1, 1, 1)
        self.__layout.addWidget(self.__HCutoffFreqCob, 10, 2, 1, 1)

        self.__layout.addWidget(self.__LCutoffFreqLab, 11, 0, 1, 1)
        self.__layout.addWidget(self.__LCutoffFreqTxt, 11, 1, 1, 1)
        self.__layout.addWidget(self.__LCutoffFreqCob, 11, 2, 1, 1)

        self.__layout.addWidget(self.__deletePeriodsLab, 12, 0, 1, 1)
        self.__layout.addWidget(self.__deletePeriodsTxt, 12, 1, 1, 1)

        self.__layout.addWidget(self.__zoomInTimesLab, 13, 0, 1, 1)
        self.__layout.addWidget(self.__zoomInTimesTxt, 13, 1, 1, 1)
        
        self.setLayout(self.__layout)
        self.setMaximumSize(250, 450)

    def readSettings(self):
        self.__channelsTxt.setText(self.__settings.readChannels())
        self.__sampleFreqTxt.setText(self.__settings.readSampleFreq())
        for i in range(2):
            if self.__sampleModeCob.itemText(i) == self.__settings.readSampleMode():
                self.__sampleModeCob.setCurrentIndex(i)
        self.__samplesPerChanTxt.setText(self.__settings.readSamplesPerChan())
        self.__maxValTxt.setText(self.__settings.readMaxVal())
        self.__minValTxt.setText(self.__settings.readMinVal())
        for i in range(3):
            if self.__couplingCob.itemText(i) == self.__settings.readCoupling():
                self.__couplingCob.setCurrentIndex(i)
        for i in range(2):
            if self.__activeEdgeCob.itemText(i) == self.__settings.readActiveEdge():
                self.__activeEdgeCob.setCurrentIndex(i)

    def writeSettings(self):
        self.__settings.writeChannels(self.__channelsTxt.toPlainText())
        self.__settings.writeSampleFreq(self.__sampleFreqTxt.toPlainText())
        self.__settings.writeSampleMode(self.__sampleModeCob.currentText())
        self.__settings.writeSamplesPerChan(
            self.__samplesPerChanTxt.toPlainText())
        self.__settings.writeMaxVal(self.__maxValTxt.toPlainText())
        self.__settings.writeMinVal(self.__minValTxt.toPlainText())
        self.__settings.writeCoupling(self.__couplingCob.currentText())
        self.__settings.writeActiveEdge(self.__activeEdgeCob.currentText())
        self.__settings.writeSettings()
        QMessageBox.information(self, "提醒", "设置保存成功")

    # def writeChannels(self):
    #     self.__settings.writeChannels(self.__channelsTxt.currentText())

    # def writeSampleFreq(self):
    #     self.__settings.writeSampleFreq(self.__sampleFreqTxt.toPlainText())

    # def writeSampleMode(self):
    #     self.__settings.writeSampleMode(self.__sampleModeCob.currentText())

    # def writeSamplesPerChan(self):
    #     self.__settings.writeSamplesPerChan(
    #         self.__samplesPerChanTxt.toPlainText())

    # def writeMaxVal(self):
    #     self.__settings.writeMaxVal(self.__maxValTxt.toPlainText())

    # def writeMinVal(self):
    #     self.__settings.writeMinVal(self.__minValTxt.toPlainText())

    # def writeCoupling(self):
    #     self.__settings.writeCoupling(self.__couplingCob.currentText())

    # def writeActiveEdge(self):
    #     self.__settings.writeActiveEdge(self.__activeEdgeCob.currentText())

    def sampleModeChange(self):
        if self.__sampleModeCob.currentText() == "有限采样":
            self.__samplesPerChanLab.setText("采样样本数")
        else:
            self.__samplesPerChanLab.setText("缓冲区样本数")

    def readPXIData(self):
        if self.__readPXIDataControlBtn.text() == "开始读取":
            self.__readPXIDataControlBtn.setText("停止读取")
            self.readPXIDataTask()
        else:
            self.__readPXIDataControlBtn.setText("开始读取")

    def readPXIDataTask(self):
        with nidaqmx.Task() as task:
            chan0 = task.ai_channels.add_ai_voltage_chan(
                self.__settings.readChannels(),
                terminal_config = TerminalConfiguration.DIFFERENTIAL,
                min_val = float(self.__settings.readMinVal()),
                max_val = float(self.__settings.readMaxVal()),
                units = VoltageUnits.VOLTS)
            chan0.ai_coupling = coupling[self.__couplingCob.currentText()]
            task.timing.cfg_samp_clk_timing(
                self.__settings.readSampleFreq(),
                source = "",
                active_edge = edge[self.__settings.readActiveEdge()],
                sample_mode = acquisitiontype[self.__settings.readSampleMode()],
                samps_per_chan = self.__settings.readSamplesPerChan())
            # TODO 保存数据并显示
            data = np.ndarray((1, samps_per_file), dtype=np.float64)
            q = AnalogSingleChannelReader(task.in_stream).read_many_sample(
                data, samps_per_file, timeout=nidaqmx.constants.WAIT_INFINITELY)
