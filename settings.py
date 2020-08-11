# -*- coding: UTF-8 -*-
# @file    :settings.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-10
# @description:

from PyQt5.QtCore import QSettings

class Settings():
    def __init__(self):
        self.__settings = QSettings("./settings.ini", QSettings.IniFormat)
        self.__settings.setIniCodec("UTF8")
        
