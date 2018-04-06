import numpy as np
from scipy.signal import zpk2ss, ss2zpk, tf2zpk, zpk2tf
from numpy import linspace, logspace
from numpy import asarray, tan, array, pi, arange, cos, log10, unwrap, angle
from matplotlib.pyplot import axvline, axhline
from scipy.signal import freqz
import matplotlib.pyplot as plt
from PyQt4.uic import loadUiType

import matplotlib.backends.backend_qt4agg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)
from PyQt4.QtGui import *
import wave
from scipy.fftpack import rfft, irfft, fftfreq ,fft ,ifft
#import pyglet
import scipy.io.wavfile as wav
import serial  # import Serial Library, ESP
import numpy as np
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph # FOR LIVE DISPLAY
import random
arduinoData = serial.Serial('com3', 115200)
Ui_MainWindow, QMainWindow = loadUiType('arduino_sound.ui')


class Main(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):
        #pyqtgraph.setConfigOption('background', 'w')  # before loading widget
        super(Main, self).__init__()
        self.setupUi(self)

        #self.plot = pg.PlotWidget()
        #self.verticalLayout_3.addWidget(self.plot)

        #self.setLayout(self.verticalLayout_3)


        #self.button.clicked.connect(self.plotter)
        self.pushButton_2.clicked.connect(self.plotter)

        #self.pushButton_3.clicked.connect(self.pause)

        #TO make the self.label text red
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
        self.label.setPalette(palette)

        self.grFFT.plotItem.showGrid(True, True, 0.7)

        self.grFFT_2.plotItem.showGrid(True, True, 0.7)

        #self.grFFT.plotItem.setRange(yRange=[0, 1])


    def plotter(self):

        self.data = [0]
        self.curve = self.grFFT.getPlotItem().plot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)





    def updater(self):

        arduinoString = arduinoData.readline()  # read the line of text from the serial port
        dataArray = arduinoString.split(',')
        a = float(dataArray[0])
        f = float(dataArray[1])
        if f == 1:
         self.label.setText('Sensor 1 is Now Selected')
        if f == 2:
         self.label.setText('Sensor 2 is Now Selected')



        print len (self.data)
        self.data.append(a)
        if (len(self.data )>= 15):
            self.data.pop(0)
        # self.data.append(self.data[-1] + 0.2 * (0.5 - random.random()))
        pen1 = pyqtgraph.mkPen(color='b')
        self.curve.setData(self.data,pen=pen1)

        #if (len(self.data)% 1024 == 0) and (f==1):
            #pen1 = pyqtgraph.mkPen(color='b')
            #pen2 = pyqtgraph.mkPen(color='r')

            #self.curve.setData(self.data, pen=pen1)

            #self.data = [0]
        #if (len(self.data) % 1024 == 0) and (f ==2 ):
         #   pen1 = pyqtgraph.mkPen(color='b')
          #  pen2 = pyqtgraph.mkPen(color='r')

            #self.grFFT_2.plot(self.data, fft, pen=pen1, clear=True)

           # self.data = [0]





        #self.login_widget_1 = LoginWidget(self)
        #self.verticalLayout_3.addWidget(self.login_widget_1)



        #self.pushButton_4.clicked.connect(self.browse_wav)
        #self.pushButton_4.setStyleSheet("background-color: red")












if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    import numpy as np

    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



