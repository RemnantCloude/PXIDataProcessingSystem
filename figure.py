# -*- coding: UTF-8 -*-
# @file    :figure.py
# @brief   :
# @author  :Cloude Remnant
# @date    :2020-08-10
# @description:

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import numpy as np

class MyFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(5, 10), dpi=100)
        super().__init__(self.fig)
        matplotlib.use("Qt5Agg")  # 声明使用QT5

        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)