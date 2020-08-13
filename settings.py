# -*- coding: UTF-8 -*-
# @file    :settings.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-10
# @description:
# TODO 数据类型检查

from PyQt5.QtCore import QSettings

class Settings():
    def __init__(self):
        self.__settings = QSettings("./settings.ini", QSettings.IniFormat)
        self.__settings.setIniCodec("UTF8")

        # 检查设置文件是否存在
        if self.__settings.value("isInitialized", False) == False:
            self.__settings.setValue("isInitialized", True)
            self.initSettings()
        else:
            self.readSettings()

    def initSettings(self):
        self.__channels = "6132/ai0"
        self.__sampleFreq = 0
        self.__sampleMode = "持续采样"
        self.__samplesPerChan = 0
        self.__maxVal = 5.0
        self.__minVal = -5.0
        self.__coupling = "DC"
        self.__activeEdge = "上升沿"

        self.writeSettings()

    def readSettings(self):
        self.__settings.beginGroup("Settings")

        self.__channels = self.__settings.value("channels")
        self.__sampleFreq = self.__settings.value("sampleFreq")
        self.__sampleMode = self.__settings.value("sampleMode")
        self.__samplesPerChan = self.__settings.value("samplesPerChan")
        self.__maxVal = self.__settings.value("maxVal")
        self.__minVal = self.__settings.value("minVal")
        self.__coupling = self.__settings.value("coupling")
        self.__activeEdge = self.__settings.value("activeEdge")

        self.__settings.endGroup()

    def writeSettings(self):
        self.__settings.beginGroup("Settings")

        self.__settings.setValue("channels", self.__channels)
        self.__settings.setValue("sampleFreq", self.__sampleFreq)
        self.__settings.setValue("sampleMode", self.__sampleMode)
        self.__settings.setValue("samplesPerChan", self.__samplesPerChan)
        self.__settings.setValue("maxVal", self.__maxVal)
        self.__settings.setValue("minVal", self.__minVal)
        self.__settings.setValue("coupling", self.__coupling)
        self.__settings.setValue("activeEdge", self.__activeEdge)

        self.__settings.endGroup()
        self.__settings.sync()

    def readChannels(self):
        return self.__channels

    def readSampleFreq(self):
        return self.__sampleFreq

    def readSampleMode(self):
        return self.__sampleMode

    def readSamplesPerChan(self):
        return self.__samplesPerChan

    def readMaxVal(self):
        return self.__maxVal

    def readMinVal(self):
        return self.__minVal

    def readCoupling(self):
        return self.__coupling

    def readActiveEdge(self):
        return self.__activeEdge

    def writeChannels(self, channels):
        self.__channels = channels

    def writeSampleFreq(self, sampleFreq):
        self.__sampleFreq = sampleFreq

    def writeSampleMode(self, sampleMode):
        self.__sampleMode = sampleMode

    def writeSamplesPerChan(self, samplesPerChan):
        self.__samplesPerChan = samplesPerChan

    def writeMaxVal(self, maxVal):
        self.__maxVal = maxVal

    def writeMinVal(self, minVal):
        self.__minVal = minVal

    def writeCoupling(self, coupling):
        self.__coupling = coupling

    def writeActiveEdge(self, activeEdge):
        self.__activeEdge = activeEdge
