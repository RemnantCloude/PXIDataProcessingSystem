# -*- coding: UTF-8 -*-
# @file    :main.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-06
# @description:

import sys
from PyQt5.QtWidgets import QApplication

from system import MeasureSystem

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MeasureSystem()
    w.setWindowTitle("高频微振幅振动测量系统")
    w.show()

    sys.exit(app.exec_())
