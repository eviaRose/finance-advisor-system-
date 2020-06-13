
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogError import Ui_DialogError
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import pandas_datareader as pdr
import numpy as np
import chart_studio.plotly as py
from datetime import datetime
from datetime import date
import pyfolio as pf
from pyfolio import plotting as pa
import icons


class Ui_TabWidgetPortfolio(object):

    def openError(self):
        self.dialog=QtWidgets.QDialog()
        self.uiError=Ui_DialogError()
        self.uiError.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, TabWidgetPortfolio):
        TabWidgetPortfolio.setObjectName("TabWidgetPortfolio")
        TabWidgetPortfolio.resize(1124, 854)
        TabWidgetPortfolio.setMinimumSize(QtCore.QSize(1124, 854))
        TabWidgetPortfolio.setMaximumSize(QtCore.QSize(1124, 854))
        font = QtGui.QFont()
        font.setPointSize(18)
        TabWidgetPortfolio.setFont(font)
        TabWidgetPortfolio.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidgetPortfolio.setIconSize(QtCore.QSize(26, 26))
        TabWidgetPortfolio.setElideMode(QtCore.Qt.ElideNone)
        self.tab_portfolio = QtWidgets.QWidget()
        self.tab_portfolio.setObjectName("tab_portfolio")
        self.listWidget = QtWidgets.QListWidget(self.tab_portfolio)
        self.listWidget.setGeometry(QtCore.QRect(80, 210, 241, 341))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setObjectName("listWidget")
        self.comboBoxSymbol = QtWidgets.QComboBox(self.tab_portfolio)
        self.comboBoxSymbol.setGeometry(QtCore.QRect(80, 130, 241, 51))
        self.comboBoxSymbol.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBoxSymbol.setEditable(True)
        self.comboBoxSymbol.setObjectName("comboBoxSymbol")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.comboBoxSymbol.addItem("")
        self.labelPeriod = QtWidgets.QLabel(self.tab_portfolio)
        self.labelPeriod.setGeometry(QtCore.QRect(610, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelPeriod.setFont(font)
        self.labelPeriod.setStyleSheet("")
        self.labelPeriod.setObjectName("labelPeriod")
        self.labelDateRange = QtWidgets.QLabel(self.tab_portfolio)
        self.labelDateRange.setGeometry(QtCore.QRect(640, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelDateRange.setFont(font)
        self.labelDateRange.setStyleSheet("")
        self.labelDateRange.setObjectName("labelDateRange")
        self.label_3 = QtWidgets.QLabel(self.tab_portfolio)
        self.label_3.setGeometry(QtCore.QRect(640, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateStart = QtWidgets.QDateEdit(self.tab_portfolio)
        self.dateStart.setGeometry(QtCore.QRect(640, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateStart.setFont(font)
        self.dateStart.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.dateStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateStart.setDate(QtCore.QDate(2019, 1, 1))
        self.dateStart.setObjectName("dateStart")
        self.labelParameter = QtWidgets.QLabel(self.tab_portfolio)
        self.labelParameter.setGeometry(QtCore.QRect(930, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelParameter.setFont(font)
        self.labelParameter.setStyleSheet("")
        self.labelParameter.setObjectName("labelParameter")
        self.comboBoxPeriod = QtWidgets.QComboBox(self.tab_portfolio)
        self.comboBoxPeriod.setGeometry(QtCore.QRect(930, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxPeriod.setFont(font)
        self.comboBoxPeriod.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.comboBoxPeriod.setObjectName("comboBoxPeriod")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.labelInterval = QtWidgets.QLabel(self.tab_portfolio)
        self.labelInterval.setGeometry(QtCore.QRect(620, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelInterval.setFont(font)
        self.labelInterval.setStyleSheet("")
        self.labelInterval.setObjectName("labelInterval")
        self.comboBoxInterval = QtWidgets.QComboBox(self.tab_portfolio)
        self.comboBoxInterval.setGeometry(QtCore.QRect(640, 450, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxInterval.setFont(font)
        self.comboBoxInterval.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.comboBoxInterval.setObjectName("comboBoxInterval")
        self.comboBoxInterval.addItem("")
        self.comboBoxInterval.addItem("")
        self.comboBoxInterval.addItem("")
        self.comboBoxInterval.addItem("")
        self.comboBoxInterval.addItem("")
        self.radioButtonRange = QtWidgets.QRadioButton(self.tab_portfolio)
        self.radioButtonRange.setGeometry(QtCore.QRect(610, 180, 21, 20))
        self.radioButtonRange.setText("")
        self.radioButtonRange.setChecked(True)
        self.radioButtonRange.setObjectName("radioButtonRange")
        self.radioButtonPeriod = QtWidgets.QRadioButton(self.tab_portfolio)
        self.radioButtonPeriod.setGeometry(QtCore.QRect(900, 180, 16, 21))
        self.radioButtonPeriod.setText("")
        self.radioButtonPeriod.setObjectName("radioButtonPeriod")
        self.label_2 = QtWidgets.QLabel(self.tab_portfolio)
        self.label_2.setGeometry(QtCore.QRect(640, 300, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEnd = QtWidgets.QDateEdit(self.tab_portfolio)
        self.dateEnd.setGeometry(QtCore.QRect(640, 330, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEnd.setFont(font)
        self.dateEnd.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.dateEnd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEnd.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEnd.setObjectName("dateEnd")
        self.AddButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.AddButton.setGeometry(QtCore.QRect(350, 140, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("font: 87 15pt \"Arial Black\";\n"
"background-color: rgb(206, 206, 206);")
        self.AddButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/add/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon)
        self.AddButton.setIconSize(QtCore.QSize(34, 34))
        self.AddButton.setObjectName("AddButton")
        self.DeleteButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.DeleteButton.setGeometry(QtCore.QRect(350, 210, 91, 41))
        self.DeleteButton.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgba(206, 206, 206, 206);")
        self.DeleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/delete/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon1)
        self.DeleteButton.setIconSize(QtCore.QSize(34, 34))
        self.DeleteButton.setObjectName("DeleteButton")
        self.candlestickButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.candlestickButton.setGeometry(QtCore.QRect(200, 760, 151, 41))
        self.candlestickButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/candlestick/candlestick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.candlestickButton.setIcon(icon2)
        self.candlestickButton.setIconSize(QtCore.QSize(34, 34))
        self.candlestickButton.setObjectName("candlestickButton")
        self.OHLCButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.OHLCButton.setGeometry(QtCore.QRect(360, 760, 141, 41))
        self.OHLCButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ohlc/ohlc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OHLCButton.setIcon(icon3)
        self.OHLCButton.setIconSize(QtCore.QSize(24, 24))
        self.OHLCButton.setObjectName("OHLCButton")
        self.timeSeriesDataButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.timeSeriesDataButton.setGeometry(QtCore.QRect(10, 760, 181, 41))
        self.timeSeriesDataButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/timeseries/timeser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.timeSeriesDataButton.setIcon(icon4)
        self.timeSeriesDataButton.setIconSize(QtCore.QSize(34, 34))
        self.timeSeriesDataButton.setObjectName("timeSeriesDataButton")
        self.dailyPercentageChangeButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.dailyPercentageChangeButton.setGeometry(QtCore.QRect(660, 760, 191, 41))
        self.dailyPercentageChangeButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/histogram/chart-histogram-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dailyPercentageChangeButton.setIcon(icon5)
        self.dailyPercentageChangeButton.setIconSize(QtCore.QSize(34, 34))
        self.dailyPercentageChangeButton.setObjectName("dailyPercentageChangeButton")
        self.volatilityButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.volatilityButton.setGeometry(QtCore.QRect(510, 760, 141, 41))
        self.volatilityButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/volatility/volatility-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volatilityButton.setIcon(icon6)
        self.volatilityButton.setIconSize(QtCore.QSize(34, 34))
        self.volatilityButton.setObjectName("volatilityButton")
        self.volumeButton = QtWidgets.QPushButton(self.tab_portfolio)
        self.volumeButton.setGeometry(QtCore.QRect(860, 760, 141, 41))
        self.volumeButton.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/area/area.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumeButton.setIcon(icon7)
        self.volumeButton.setIconSize(QtCore.QSize(34, 34))
        self.volumeButton.setObjectName("volumeButton")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/portfolio/portfolio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidgetPortfolio.addTab(self.tab_portfolio, icon8, "")
        self.tab_advisor = QtWidgets.QWidget()
        self.tab_advisor.setObjectName("tab_advisor")
        self.toolBoxAdvisor = QtWidgets.QToolBox(self.tab_advisor)
        self.toolBoxAdvisor.setGeometry(QtCore.QRect(0, 220, 1121, 581))
        self.toolBoxAdvisor.setObjectName("toolBoxAdvisor")
        self.pageNaive = QtWidgets.QWidget()
        self.pageNaive.setGeometry(QtCore.QRect(0, 0, 1121, 428))
        self.pageNaive.setObjectName("pageNaive")
        self.comboBoxThreshold = QtWidgets.QComboBox(self.pageNaive)
        self.comboBoxThreshold.setGeometry(QtCore.QRect(160, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxThreshold.setFont(font)
        self.comboBoxThreshold.setStyleSheet("")
        self.comboBoxThreshold.setObjectName("comboBoxThreshold")
        self.comboBoxThreshold.addItem("")
        self.comboBoxThreshold.addItem("")
        self.comboBoxThreshold.addItem("")
        self.comboBoxThreshold.addItem("")
        self.comboBoxThreshold.addItem("")
        self.labelThreshold = QtWidgets.QLabel(self.pageNaive)
        self.labelThreshold.setGeometry(QtCore.QRect(30, 20, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelThreshold.setFont(font)
        self.labelThreshold.setStyleSheet("")
        self.labelThreshold.setObjectName("labelThreshold")
        self.naiveButton = QtWidgets.QPushButton(self.pageNaive)
        self.naiveButton.setGeometry(QtCore.QRect(500, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.naiveButton.setFont(font)
        self.naiveButton.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.naiveButton.setObjectName("naiveButton")
        self.toolBoxAdvisor.addItem(self.pageNaive, "")
        self.pageMAC = QtWidgets.QWidget()
        self.pageMAC.setGeometry(QtCore.QRect(0, 0, 1121, 428))
        self.pageMAC.setObjectName("pageMAC")
        self.labelShort = QtWidgets.QLabel(self.pageMAC)
        self.labelShort.setGeometry(QtCore.QRect(30, 40, 261, 31))
        self.labelShort.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.labelShort.setObjectName("labelShort")
        self.comboBoxShort = QtWidgets.QComboBox(self.pageMAC)
        self.comboBoxShort.setGeometry(QtCore.QRect(290, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxShort.setFont(font)
        self.comboBoxShort.setStyleSheet("")
        self.comboBoxShort.setObjectName("comboBoxShort")
        self.comboBoxShort.addItem("")
        self.comboBoxShort.addItem("")
        self.comboBoxShort.addItem("")
        self.labelLong = QtWidgets.QLabel(self.pageMAC)
        self.labelLong.setGeometry(QtCore.QRect(30, 100, 251, 31))
        self.labelLong.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.labelLong.setObjectName("labelLong")
        self.comboBoxLong = QtWidgets.QComboBox(self.pageMAC)
        self.comboBoxLong.setGeometry(QtCore.QRect(290, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxLong.setFont(font)
        self.comboBoxLong.setStyleSheet("")
        self.comboBoxLong.setObjectName("comboBoxLong")
        self.comboBoxLong.addItem("")
        self.comboBoxLong.addItem("")
        self.comboBoxLong.addItem("")
        self.MACButton = QtWidgets.QPushButton(self.pageMAC)
        self.MACButton.setGeometry(QtCore.QRect(500, 190, 131, 31))
        self.MACButton.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.MACButton.setObjectName("MACButton")
        self.toolBoxAdvisor.addItem(self.pageMAC, "")
        self.pageTurtle = QtWidgets.QWidget()
        self.pageTurtle.setGeometry(QtCore.QRect(0, 0, 1121, 428))
        self.pageTurtle.setObjectName("pageTurtle")
        self.labelBreakout = QtWidgets.QLabel(self.pageTurtle)
        self.labelBreakout.setGeometry(QtCore.QRect(30, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelBreakout.setFont(font)
        self.labelBreakout.setObjectName("labelBreakout")
        self.comboBoxBreakout = QtWidgets.QComboBox(self.pageTurtle)
        self.comboBoxBreakout.setGeometry(QtCore.QRect(170, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBoxBreakout.setFont(font)
        self.comboBoxBreakout.setObjectName("comboBoxBreakout")
        self.comboBoxBreakout.addItem("")
        self.comboBoxBreakout.addItem("")
        self.comboBoxBreakout.addItem("")
        self.comboBoxBreakout.addItem("")
        self.comboBoxBreakout.addItem("")
        self.turtleButton = QtWidgets.QPushButton(self.pageTurtle)
        self.turtleButton.setGeometry(QtCore.QRect(500, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.turtleButton.setFont(font)
        self.turtleButton.setStyleSheet("font: 87 15pt \"Arial Black\";")
        self.turtleButton.setObjectName("turtleButton")
        self.toolBoxAdvisor.addItem(self.pageTurtle, "")
        self.labelInitialCapital = QtWidgets.QLabel(self.tab_advisor)
        self.labelInitialCapital.setGeometry(QtCore.QRect(30, 70, 241, 51))
        self.labelInitialCapital.setStyleSheet("font: 87 18pt \"Arial Black\";")
        self.labelInitialCapital.setObjectName("labelInitialCapital")
        self.comboBoxInitialCapital = QtWidgets.QComboBox(self.tab_advisor)
        self.comboBoxInitialCapital.setGeometry(QtCore.QRect(270, 80, 131, 31))
        self.comboBoxInitialCapital.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBoxInitialCapital.setEditable(True)
        self.comboBoxInitialCapital.setObjectName("comboBoxInitialCapital")
        self.comboBoxInitialCapital.addItem("")
        self.comboBoxInitialCapital.addItem("")
        self.comboBoxInitialCapital.addItem("")
        self.comboBoxInitialCapital.addItem("")
        self.labelCommission = QtWidgets.QLabel(self.tab_advisor)
        self.labelCommission.setGeometry(QtCore.QRect(540, 70, 221, 41))
        self.labelCommission.setStyleSheet("font: 87 18pt \"Arial Black\";")
        self.labelCommission.setObjectName("labelCommission")
        self.comboBoxCommission = QtWidgets.QComboBox(self.tab_advisor)
        self.comboBoxCommission.setGeometry(QtCore.QRect(760, 80, 101, 31))
        self.comboBoxCommission.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBoxCommission.setEditable(True)
        self.comboBoxCommission.setObjectName("comboBoxCommission")
        self.comboBoxCommission.addItem("")
        self.comboBoxCommission.addItem("")
        self.comboBoxCommission.addItem("")
        self.comboBoxCommission.addItem("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/advisor/advisor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidgetPortfolio.addTab(self.tab_advisor, icon9, "")

        self.retranslateUi(TabWidgetPortfolio)
        TabWidgetPortfolio.setCurrentIndex(0)
        self.toolBoxAdvisor.setCurrentIndex(0)
        self.toolBoxAdvisor.layout().setSpacing(7)
        QtCore.QMetaObject.connectSlotsByName(TabWidgetPortfolio)

        self.AddButton.clicked.connect(self.addToList)
        self.DeleteButton.clicked.connect(self.removeItems) 
        self.comboBoxPeriod.setDisabled(True)
        self.timeSeriesDataButton.clicked.connect(self.plotTimeSeries)
        self.candlestickButton.clicked.connect(self.plotCandlestick)
        self.OHLCButton.clicked.connect(self.plotOHLC)
        self.volatilityButton.clicked.connect(self.plotVolatility)
        self.dailyPercentageChangeButton.clicked.connect(self.calculatePctChange)
        self.volumeButton.clicked.connect(self.plotVolume)
        self.naiveButton.clicked.connect(self.buildTableNaive)
        self.MACButton.clicked.connect(self.buildTableMAC)
        self.turtleButton.clicked.connect(self.turtleStrategy)
        self.radioButtonRange.clicked.connect(self.disablePeriod)
        self.radioButtonPeriod.clicked.connect(self.disableRange)
        self.comboBoxPeriod.currentIndexChanged.connect(self.changeIntervalOptionsForPeriod)
        self.radioButtonRange.clicked.connect(self.changeIntervalOptionsForRange)
        self.radioButtonPeriod.clicked.connect(self.changeIntervalOptionsForPeriod)
        self.dateEnd.dateChanged.connect(self.startDateLowerThenEnd)

    def retranslateUi(self, TabWidgetPortfolio):
        _translate = QtCore.QCoreApplication.translate
        TabWidgetPortfolio.setWindowTitle(_translate("TabWidgetPortfolio", "TabWidget"))
        self.comboBoxSymbol.setToolTip(_translate("TabWidgetPortfolio", "<html><head/><body><p><span style=\" font-size:12pt;\">Type/ Select Symbol</span></p></body></html>"))
        self.comboBoxSymbol.setCurrentText(_translate("TabWidgetPortfolio", "Enter Symbol"))
        self.comboBoxSymbol.setItemText(0, _translate("TabWidgetPortfolio", "Enter Symbol"))
        self.comboBoxSymbol.setItemText(1, _translate("TabWidgetPortfolio", "Microsoft"))
        self.comboBoxSymbol.setItemText(2, _translate("TabWidgetPortfolio", "Apple"))
        self.comboBoxSymbol.setItemText(3, _translate("TabWidgetPortfolio", "Amazon"))
        self.comboBoxSymbol.setItemText(4, _translate("TabWidgetPortfolio", "Alphabet"))
        self.comboBoxSymbol.setItemText(5, _translate("TabWidgetPortfolio", "Alibaba"))
        self.comboBoxSymbol.setItemText(6, _translate("TabWidgetPortfolio", "Facebook"))
        self.comboBoxSymbol.setItemText(7, _translate("TabWidgetPortfolio", "Visa"))
        self.comboBoxSymbol.setItemText(8, _translate("TabWidgetPortfolio", "Walmart"))
        self.labelPeriod.setText(_translate("TabWidgetPortfolio", "Period:"))
        self.labelDateRange.setText(_translate("TabWidgetPortfolio", "By Date Range"))
        self.label_3.setText(_translate("TabWidgetPortfolio", "Start:"))
        self.dateStart.setDisplayFormat(_translate("TabWidgetPortfolio", "yyyy-MM-dd"))
        self.labelParameter.setText(_translate("TabWidgetPortfolio", "By Parameter"))
        self.comboBoxPeriod.setItemText(0, _translate("TabWidgetPortfolio", "1d"))
        self.comboBoxPeriod.setItemText(1, _translate("TabWidgetPortfolio", "5d"))
        self.comboBoxPeriod.setItemText(2, _translate("TabWidgetPortfolio", "7d"))
        self.comboBoxPeriod.setItemText(3, _translate("TabWidgetPortfolio", "1mo"))
        self.comboBoxPeriod.setItemText(4, _translate("TabWidgetPortfolio", "3mo"))
        self.comboBoxPeriod.setItemText(5, _translate("TabWidgetPortfolio", "6mo"))
        self.comboBoxPeriod.setItemText(6, _translate("TabWidgetPortfolio", "1y"))
        self.comboBoxPeriod.setItemText(7, _translate("TabWidgetPortfolio", "2y"))
        self.comboBoxPeriod.setItemText(8, _translate("TabWidgetPortfolio", "5y"))
        self.comboBoxPeriod.setItemText(9, _translate("TabWidgetPortfolio", "10y"))
        self.labelInterval.setText(_translate("TabWidgetPortfolio", "Interval:"))
        self.comboBoxInterval.setItemText(0, _translate("TabWidgetPortfolio", "1d"))
        self.comboBoxInterval.setItemText(1, _translate("TabWidgetPortfolio", "5d"))
        self.comboBoxInterval.setItemText(2, _translate("TabWidgetPortfolio", "1wk"))
        self.comboBoxInterval.setItemText(3, _translate("TabWidgetPortfolio", "1mo"))
        self.comboBoxInterval.setItemText(4, _translate("TabWidgetPortfolio", "3mo"))
        self.label_2.setText(_translate("TabWidgetPortfolio", "End:"))
        self.dateEnd.setDisplayFormat(_translate("TabWidgetPortfolio", "yyyy-MM-dd"))
        self.AddButton.setToolTip(_translate("TabWidgetPortfolio", "<html><head/><body><p><span style=\" font-size:12pt;\">Add Symbol</span></p></body></html>"))
        self.DeleteButton.setToolTip(_translate("TabWidgetPortfolio", "<html><head/><body><p>Delete Symbol</p></body></html>"))
        self.candlestickButton.setText(_translate("TabWidgetPortfolio", "Candlestick"))
        self.OHLCButton.setText(_translate("TabWidgetPortfolio", "OHLC"))
        self.timeSeriesDataButton.setToolTip(_translate("TabWidgetPortfolio", "<html><head/><body><p><br/></p></body></html>"))
        self.timeSeriesDataButton.setText(_translate("TabWidgetPortfolio", "Time Series Data"))
        self.dailyPercentageChangeButton.setText(_translate("TabWidgetPortfolio", "Percentage Change "))
        self.volatilityButton.setText(_translate("TabWidgetPortfolio", "Volatility"))
        self.volumeButton.setText(_translate("TabWidgetPortfolio", "Volume"))
        TabWidgetPortfolio.setTabText(TabWidgetPortfolio.indexOf(self.tab_portfolio), _translate("TabWidgetPortfolio", "Portfolio"))
        self.comboBoxThreshold.setItemText(0, _translate("TabWidgetPortfolio", "5"))
        self.comboBoxThreshold.setItemText(1, _translate("TabWidgetPortfolio", "7"))
        self.comboBoxThreshold.setItemText(2, _translate("TabWidgetPortfolio", "10"))
        self.comboBoxThreshold.setItemText(3, _translate("TabWidgetPortfolio", "15"))
        self.comboBoxThreshold.setItemText(4, _translate("TabWidgetPortfolio", "20"))
        self.labelThreshold.setText(_translate("TabWidgetPortfolio", "Threshold:"))
        self.naiveButton.setText(_translate("TabWidgetPortfolio", "Advise"))
        self.toolBoxAdvisor.setItemText(self.toolBoxAdvisor.indexOf(self.pageNaive), _translate("TabWidgetPortfolio", "Naive Trading Strategy"))
        self.labelShort.setText(_translate("TabWidgetPortfolio", "Short Moving Average:"))
        self.comboBoxShort.setItemText(0, _translate("TabWidgetPortfolio", "5"))
        self.comboBoxShort.setItemText(1, _translate("TabWidgetPortfolio", "10"))
        self.comboBoxShort.setItemText(2, _translate("TabWidgetPortfolio", "25"))
        self.labelLong.setText(_translate("TabWidgetPortfolio", "Long Moving Average:"))
        self.comboBoxLong.setItemText(0, _translate("TabWidgetPortfolio", "50"))
        self.comboBoxLong.setItemText(1, _translate("TabWidgetPortfolio", "100"))
        self.comboBoxLong.setItemText(2, _translate("TabWidgetPortfolio", "200"))
        self.MACButton.setText(_translate("TabWidgetPortfolio", "Advise"))
        self.toolBoxAdvisor.setItemText(self.toolBoxAdvisor.indexOf(self.pageMAC), _translate("TabWidgetPortfolio", "Two Moving Average Crossover Strategy"))
        self.labelBreakout.setText(_translate("TabWidgetPortfolio", "Breakout:"))
        self.comboBoxBreakout.setCurrentText(_translate("TabWidgetPortfolio", "35"))
        self.comboBoxBreakout.setItemText(0, _translate("TabWidgetPortfolio", "35"))
        self.comboBoxBreakout.setItemText(1, _translate("TabWidgetPortfolio", "40"))
        self.comboBoxBreakout.setItemText(2, _translate("TabWidgetPortfolio", "45"))
        self.comboBoxBreakout.setItemText(3, _translate("TabWidgetPortfolio", "50"))
        self.comboBoxBreakout.setItemText(4, _translate("TabWidgetPortfolio", "55"))
        self.turtleButton.setText(_translate("TabWidgetPortfolio", "Advise"))
        self.toolBoxAdvisor.setItemText(self.toolBoxAdvisor.indexOf(self.pageTurtle), _translate("TabWidgetPortfolio", "Turtle Strategy"))
        self.labelInitialCapital.setText(_translate("TabWidgetPortfolio", "Initial Capital:"))
        self.comboBoxInitialCapital.setCurrentText(_translate("TabWidgetPortfolio", "100000"))
        self.comboBoxInitialCapital.setItemText(0, _translate("TabWidgetPortfolio", "100000"))
        self.comboBoxInitialCapital.setItemText(1, _translate("TabWidgetPortfolio", "150000"))
        self.comboBoxInitialCapital.setItemText(2, _translate("TabWidgetPortfolio", "200000"))
        self.comboBoxInitialCapital.setItemText(3, _translate("TabWidgetPortfolio", "250000"))
        self.labelCommission.setText(_translate("TabWidgetPortfolio", "Commission:"))
        self.comboBoxCommission.setItemText(0, _translate("TabWidgetPortfolio", "0.00"))
        self.comboBoxCommission.setItemText(1, _translate("TabWidgetPortfolio", "0.02"))
        self.comboBoxCommission.setItemText(2, _translate("TabWidgetPortfolio", "0.03"))
        self.comboBoxCommission.setItemText(3, _translate("TabWidgetPortfolio", "0.04"))
        TabWidgetPortfolio.setTabText(TabWidgetPortfolio.indexOf(self.tab_advisor), _translate("TabWidgetPortfolio", "Trade Advisor"))

#############################SET#####################################################################################################
        self.dateEnd.setMaximumDate(date.today())
        self.dateStart.setMaximumDate(self.dateEnd.date())

    def startDateLowerThenEnd(self):
        self.dateStart.setMaximumDate(self.dateEnd.date())

    def disablePeriod(self):
        self.comboBoxPeriod.setDisabled(True)
        self.dateEnd.setEnabled(True)
        self.dateStart.setEnabled(True)
    
    def disableRange(self):
        self.dateEnd.setDisabled(True)
        self.dateStart.setDisabled(True)
        self.comboBoxPeriod.setEnabled(True)
        
    def changeIntervalOptionsForPeriod(self):  
        if ((self.comboBoxPeriod.currentText()=="1mo")|(self.comboBoxPeriod.currentText()=="60d")):
            self.comboBoxInterval.clear()
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.setItemText(0,"2m")
            self.comboBoxInterval.setItemText(1,"5m")
            self.comboBoxInterval.setItemText(2,"15m")
            self.comboBoxInterval.setItemText(3,"30m")
            self.comboBoxInterval.setItemText(4,"60m")
            self.comboBoxInterval.setItemText(5,"90m")
            self.comboBoxInterval.setItemText(6,"1d")
            self.comboBoxInterval.setItemText(7,"5d")
            self.comboBoxInterval.setItemText(8,"1wk")
            self.comboBoxInterval.setItemText(9,"1mo")
            self.comboBoxInterval.setItemText(10,"3mo")
        if((self.comboBoxPeriod.currentText()=="1d")|(self.comboBoxPeriod.currentText()=="5d")|(self.comboBoxPeriod.currentText()=="7d")):
            self.comboBoxInterval.clear()
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.setItemText(0,"1m")
            self.comboBoxInterval.setItemText(1,"2m")
            self.comboBoxInterval.setItemText(2,"5m")
            self.comboBoxInterval.setItemText(3,"15m")
            self.comboBoxInterval.setItemText(4,"30m")
            self.comboBoxInterval.setItemText(5,"60m")
            self.comboBoxInterval.setItemText(6,"90m")
            self.comboBoxInterval.setItemText(7,"1d")
            self.comboBoxInterval.setItemText(8,"5d")
            self.comboBoxInterval.setItemText(9,"1wk")
            self.comboBoxInterval.setItemText(10,"1mo")
            self.comboBoxInterval.setItemText(11,"3mo")
        if((self.comboBoxPeriod.currentText()=="3mo")|(self.comboBoxPeriod.currentText()=="1y")|(self.comboBoxPeriod.currentText()=="2y")|(self.comboBoxPeriod.currentText()=="5y")|(self.comboBoxPeriod.currentText()=="10y")):
            self.comboBoxInterval.clear()
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.setItemText(0,"1d")
            self.comboBoxInterval.setItemText(1,"5d")
            self.comboBoxInterval.setItemText(2,"1wk")
            self.comboBoxInterval.setItemText(3,"1mo")
            self.comboBoxInterval.setItemText(4,"3mo")

    def changeIntervalOptionsForRange(self):
            self.comboBoxInterval.clear()
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.addItem("")
            self.comboBoxInterval.setItemText(0,"1d")
            self.comboBoxInterval.setItemText(1,"5d")
            self.comboBoxInterval.setItemText(2,"1wk")
            self.comboBoxInterval.setItemText(3,"1mo")
            self.comboBoxInterval.setItemText(4,"3mo")      

###################################DATA############################################################################################
    def addToList(self):
        item=str(self.comboBoxSymbol.currentText())
        item=self.showSymbol(item)
        checkIfExist=yf.download(item,period="5d",interval="1m")
        x=checkIfExist.empty
        if x!=True:
            self.listWidget.insertItem(0,item)
            self.comboBoxSymbol.setCurrentIndex(0)
        else: 
            self.openError()
     
    def showSymbol(self,item):
        if item=='Microsoft':return 'MSFT'
        if item=='Apple': return 'AAPL'
        if item=='Amazon': return 'AMZN'
        if item=='Alphabet': return 'GOOG'
        if item=='Alibaba': return 'BABA'
        if item=='Facebook': return 'FB'
        if item=='Visa': return 'V'
        if item=='Walmart': return 'WMT'
        else: return item
    
    def removeItems(self): 
        for item in self.listWidget.selectedItems():
          self.listWidget.takeItem(self.listWidget.row(item))           

    def getList(self):
        lw = self.listWidget
        listSymbols=[]
        for x in range(lw.count()):
          listItem=str(lw.item(x).text())
          listSymbols.append(listItem)
        i=0
        while i< len(listSymbols):
            listSymbols[i]=listSymbols[i].upper()
            i=i+1
        return (listSymbols)

    def getForRange(self,tickers, startdate, enddate):
        def data(ticker):
          return(yf.download(ticker, start=startdate, end=enddate,interval=self.comboBoxInterval.currentText()))
        datas = map (data, tickers)
        return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

    def getForPeriod(self,tickers,period):
        def data(ticker):
          return(yf.download(ticker,period=self.comboBoxPeriod.currentText(),interval=self.comboBoxInterval.currentText()))
        datas = map (data, tickers)
        return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))  

####################################CHARTS############################################################################### 
    def plotCandlestick(self):    
        listSymbols=self.getList()
        if(self.radioButtonRange.isChecked()):
            df=yf.download(listSymbols,start=self.dateStart.text(),end=self.dateEnd.text(),interval=self.comboBoxInterval.currentText())
        if(self.radioButtonPeriod.isChecked()):
            df=yf.download(listSymbols,period=self.comboBoxPeriod.currentText(),interval=self.comboBoxInterval.currentText())  
        i=0
        if len(listSymbols)>1:
            while i< len(listSymbols):
              figu = go.Figure(data=[go.Candlestick(x=df.index,open=df['Open'][listSymbols[i]], high=df['High'][listSymbols[i]],low=df['Low'][listSymbols[i]],
               close=df['Close'][listSymbols[i]])],layout_title_text=listSymbols[i])
              figu.update_layout(xaxis_rangeslider_visible=False)
              figu.show()
              i=i+1
        if len(listSymbols)==1:
              figu = go.Figure(data=[go.Candlestick(x=df.index,open=df['Open'], high=df['High'],low=df['Low'],
               close=df['Close'])],layout_title_text=listSymbols[i])
              figu.update_layout(xaxis_rangeslider_visible=False)
              figu.show()

    def plotOHLC(self):  
        listSymbols=self.getList()
        if(self.radioButtonRange.isChecked()):
            df=yf.download(listSymbols,start=self.dateStart.text(),end=self.dateEnd.text(),interval=self.comboBoxInterval.currentText())
        if(self.radioButtonPeriod.isChecked()):
            df=yf.download(listSymbols,period=self.comboBoxPeriod.currentText(),interval=self.comboBoxInterval.currentText()) 
        i=0
        if len(listSymbols)>1:
            while i< len(listSymbols):
              figu = go.Figure(data=[go.Ohlc(x=df.index,open=df['Open'][listSymbols[i]], high=df['High'][listSymbols[i]],low=df['Low'][listSymbols[i]], 
              close=df['Close'][listSymbols[i]])],layout_title_text=listSymbols[i])
              figu.update_layout(xaxis_rangeslider_visible=False)
              figu.show()
              i=i+1
        if len(listSymbols)==1:
              figu = go.Figure(data=[go.Ohlc(x=df.index,open=df['Open'], high=df['High'],low=df['Low'], close=df['Close'])],layout_title_text=listSymbols[i])
              figu.update_layout(xaxis_rangeslider_visible=False)
              figu.show()
        
    def calculatePctChange(self):    
        listSymbols=self.getList()    
        if (self.radioButtonRange.isChecked()):
            all_data = self.getForRange(listSymbols,self.dateStart.text(),self.dateEnd.text())
        if(self.radioButtonPeriod.isChecked()):
            all_data=self.getForPeriod(listSymbols,self.comboBoxPeriod.currentText())    
        daily_close_px= all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')
        daily_pct_change = daily_close_px.pct_change()
        daily_pct_change.hist(bins=50, sharex=False, figsize=(12,8))
        plt.show()
    
    def plotTimeSeries(self):    
        listSymbols=self.getList()    
        if (self.radioButtonRange.isChecked()):
            all_data = self.getForRange(listSymbols,self.dateStart.text(),self.dateEnd.text())
        if(self.radioButtonPeriod.isChecked()):
            all_data=self.getForPeriod(listSymbols,self.comboBoxPeriod.currentText())    
        time_series= all_data[['Close']].reset_index().pivot('Date', 'Ticker', 'Close')
        time_series.plot(subplots=True,sharex=False)
        plt.show()        
     
    def plotVolume(self):  
        listSymbols=self.getList()    
        if (self.radioButtonRange.isChecked()):
            all_data = self.getForRange(listSymbols,self.dateStart.text(),self.dateEnd.text())
        if(self.radioButtonPeriod.isChecked()):
            all_data=self.getForPeriod(listSymbols,self.comboBoxPeriod.currentText())    
        vol=all_data[['Volume']].reset_index().pivot('Date', 'Ticker', 'Volume')
        vol.plot.area(subplots=True,sharex=False,lw=3,grid=True) 
        plt.show()
            
    def plotVolatility(self):    
        listSymbols=self.getList()
        if (self.radioButtonRange.isChecked()):
            all_data = self.getForRange(listSymbols,self.dateStart.text(),self.dateEnd.text())
        if(self.radioButtonPeriod.isChecked()):
            all_data=self.getForPeriod(listSymbols,self.comboBoxPeriod.currentText())   
        daily_close_px= all_data[['Adj Close']].reset_index().pivot('Date', 'Ticker', 'Adj Close')
        daily_pct_change = daily_close_px.pct_change()
        if len(daily_pct_change)>500:
            min_periods = 252
        else: min_periods = 21 
        vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods) 
        vol.plot(figsize=(10, 8))
        plt.show()

#################################################advisor####################################################################
    def buildDFAdvisor(self,listSymbols):
        if(self.radioButtonRange.isChecked()):
           df=yf.download(listSymbols,start=self.dateStart.text(),end=self.dateEnd.text(),interval=self.comboBoxInterval.currentText())
        if(self.radioButtonPeriod.isChecked()):
           df=yf.download(listSymbols,period=self.comboBoxPeriod.currentText(),interval=self.comboBoxInterval.currentText())
        return (df) 
      
    def buildTableMAC(self):
        listSymbols=self.getList()
        df=self.buildDFAdvisor(listSymbols)
        short_window = int(self.comboBoxShort.currentText())
        long_window = int(self.comboBoxLong.currentText())
        i=0
        if len(df)>short_window:
            while i< len(listSymbols):
                symbol=listSymbols[i]
                signals = pd.DataFrame(index=df.index)
                signals['symbol']=symbol
                signals['signal'] = 0.0
                if len(listSymbols)>1:
                    listLength=2
                    signals['short_mavg'] = df['Close'][symbol].rolling(window=short_window, min_periods=1, center=False).mean()
                    signals['long_mavg'] = df['Close'][symbol].rolling(window=long_window, min_periods=1, center=False).mean()
                    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:]  > signals['long_mavg'][short_window:], 1.0, 0.0)   
                    signals['positions'] = signals['signal'].diff()
                    signals['price']=df['Close'][symbol]
                if len(listSymbols)==1:
                    listLength=1
                    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
                    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
                    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:]  > signals['long_mavg'][short_window:], 1.0, 0.0)   
                    signals['positions'] = signals['signal'].diff()
                    signals['price']=df['Close']                        
                signals=self.addSharesColumn(signals)
                self.plotMAcrossover(df,symbol,signals,listLength)
                self.backtestTable(signals,symbol)
                i=i+1
           
    def plotMAcrossover(self,df,symbol,signals,listLength):
          fig = plt.figure()
          ax1 = fig.add_subplot(111,  ylabel='Price')
          if listLength==2:
              df['Close'][symbol].plot(ax=ax1, color='r', lw=2.)
          if listLength==1:
              df['Close'].plot(ax=ax1, color='r', lw=2.) 
          signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
          ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0],'^', markersize=10, color='k')
          ax1.plot(signals.loc[signals.positions == -1.0].index,signals.short_mavg[signals.positions == -1.0],'v', markersize=10, color='k')
          plt.legend(["Price",'short_mavg', 'long_mavg',"Buy","Sell"])
          plt.title("Two Moving Average Crossover For "+symbol)
          plt.show()

    def buildTableNaive(self):
        listSymbols=self.getList()
        df=self.buildDFAdvisor(listSymbols)
        nb_conseq_days=int(self.comboBoxThreshold.currentText())  
        i=0
        while (i< len(listSymbols)):        
          symbol=listSymbols[i]
          signals = pd.DataFrame(index=df.index)
          signals['symbol']=symbol
          if len(listSymbols)>1: 
            listLength=2
            signals['price']=df['Adj Close'][symbol]
          if len(listSymbols)==1:
            listLength=1
            signals['price']=df['Adj Close']
          signals['positions'] = 0
          cons_day=0
          prior_price=0
          init=True
          for k in range(len(signals['price'])):
              price=signals['price'][k]
              if init:
                  init=False
              elif price>prior_price:
                  if cons_day<0:
                      cons_day=0
                  cons_day+=1
              elif price<prior_price:
                  if cons_day>0:
                      cons_day=0
                  cons_day-=1
              if cons_day==nb_conseq_days:
                 signals['positions'][k]=1
              elif cons_day == -nb_conseq_days:
                 signals['positions'][k]=-1
              prior_price=price         
          signals=self.addSharesColumn(signals)
          signals=self.addArrowsColumnNaive(signals)
          self.plotNaive(df,symbol,signals,listLength)
          self.backtestTable(signals,symbol)
          i=i+1             
                
    def plotNaive(self,df,symbol,signals,listLength):
        fig = plt.figure()
        ax1 = fig.add_subplot(111, ylabel='price')
        if listLength==1:
          df["Adj Close"].plot(ax=ax1, color='g', lw=.5)
          ax1.plot(signals.loc[signals.arrows== 1.0].index,df["Adj Close"][signals.arrows == 1],'^', markersize=7, color='k')
          ax1.plot(signals.loc[signals.arrows== -1.0].index,df["Adj Close"][signals.arrows == -1],'v', markersize=7, color='k')
        if listLength==2:
          df["Adj Close"][symbol].plot(ax=ax1, color='g', lw=.5)
          ax1.plot(signals.loc[signals.arrows== 1.0].index,df["Adj Close"][symbol][signals.arrows == 1],'^', markersize=7, color='k')
          ax1.plot(signals.loc[signals.arrows== -1.0].index,df["Adj Close"][symbol][signals.arrows == -1],'v', markersize=7, color='k')            
        plt.legend(["Price","Buy","Sell"])
        plt.title("Naive Trading Strategy for "+symbol)
        plt.show()

    def turtleStrategy(self):
        listSymbols=self.getList()
        df=self.buildDFAdvisor(listSymbols)
        i=0
        while (i< len(listSymbols)):
          symbol=listSymbols[i]
          signals = pd.DataFrame(index=df.index)
          signals['symbol']=symbol
          if len(listSymbols)>1:
              listLength=2
              signals['price']=df['Close'][symbol]
              signals['high'] = df['Close'][symbol].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).max()
              signals['low'] = df['Close'][symbol].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).min()
              signals['avg'] = df['Close'][symbol].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).mean()
              signals['long_entry'] = df['Close'][symbol] > signals.high
              signals['short_entry'] = df['Close'][symbol] < signals.low
              signals['long_exit'] =df['Close'][symbol] < signals.avg
              signals['short_exit'] =df['Close'][symbol] > signals.avg
          if len(listSymbols)==1:
              listLength=1
              signals['price']=df['Close']
              signals['high'] = df['Close'].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).max()
              signals['low'] = df['Close'].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).min()
              signals['avg'] = df['Close'].shift(1).rolling(window=int(self.comboBoxBreakout.currentText())).mean()
              signals['long_entry'] = df['Close'] > signals.high
              signals['short_entry'] = df['Close'] < signals.low
              signals['long_exit'] =df['Close'] < signals.avg
              signals['short_exit'] =df['Close'] > signals.avg
          signals['positions_long'] = 0 
          signals.loc[signals.long_entry,'positions_long']= 1 
          signals.loc[signals.long_exit,'positions_long']= 0 
          signals['positions_short'] = 0 
          signals.loc[signals.short_entry,'positions_short']= -1 
          signals.loc[signals.short_exit,'positions_short']= 0 
          signals['positions'] = signals.positions_long + signals.positions_short
          signals['shares']=signals['positions']
          signals=self.addArrowsColumnTurtle(signals)
          self.plotTurtle(df,symbol,signals,listLength)
          self.backtestTable(signals,symbol)          
          i=i+1
    
    def plotTurtle(self,df,symbol,signals,listLength):
          fig = plt.figure()
          ax1 = fig.add_subplot(111, ylabel='price')
          if listLength==1:
              df["Close"].plot(ax=ax1, color='g', lw=.5)
              signals.low.plot(ax=ax1, color='r', lw=.5)
              signals.high.plot(ax=ax1, color='b', lw=.5)
              ax1.plot(signals.loc[signals['arrows']== 1].index, df["Close"][signals['arrows']== 1],'^', markersize=7, color='k')  
              ax1.plot(signals.loc[signals['arrows']==-1].index, df["Close"][signals['arrows']== -1],'v', markersize=7, color='k')
          if listLength==2:
              df["Close"][symbol].plot(ax=ax1, color='g', lw=.5)
              signals.low.plot(ax=ax1, color='r', lw=.5)
              signals.high.plot(ax=ax1, color='b', lw=.5)
              ax1.plot(signals.loc[signals['arrows']== 1].index, df["Close"][symbol][signals['arrows']== 1],'^', markersize=7, color='k')  
              ax1.plot(signals.loc[signals['arrows']==-1].index, df["Close"][symbol][signals['arrows']== -1],'v', markersize=7, color='k')
          plt.legend(["Price","low","high"])
          plt.title("Turtle Trading Strategy for "+symbol)
          plt.show()

    def addSharesColumn(self,signals):
        signals['shares']=0
        sign=0.0
        for k in range(len(signals)):
            if signals['positions'][k]==1.0: 
                sign=1.0
            elif signals['positions'][k]==-1.0:
                sign=0.0
            signals['shares'][k]=sign
        return(signals)
            
    def addArrowsColumnTurtle(self,signals):
        signals['arrows']=0
        prior_arrow=0.0
        for k in range(len(signals)):
            if signals['positions'][k]==1:
                if prior_arrow==1:
                    signals['arrows'][k]=0.0
                else: signals['arrows'][k]=1
                prior_arrow=1
            elif signals['positions'][k]==-1:
                if prior_arrow==-1:
                    signals['arrows'][k]=0.0
                else: signals['arrows'][k]=-1
                prior_arrow=-1
            elif signals['positions'][k]==0.0:
                if prior_arrow==1:
                    signals['arrows'][k]=-1
                if prior_arrow==-1:
                    signals['arrows'][k]=1
                prior_arrow=0
        return(signals)               

    def addArrowsColumnNaive(self,signals):
        signals['arrows']=0
        prior_arrow=0.0
        for k in range(len(signals)):
            if signals['positions'][k]==1:
                if prior_arrow==1:
                    signals['arrows'][k]=0.0
                else: signals['arrows'][k]=1
                prior_arrow=1
            elif signals['positions'][k]==-1:
                if prior_arrow==-1:
                    signals['arrows'][k]=0.0
                else: signals['arrows'][k]=-1
                prior_arrow=-1
        return(signals) 

    def backtestTable(self,signals,symbol):
        initial_capital= float(self.comboBoxInitialCapital.currentText())
        portfolio = pd.DataFrame(index=signals.index).fillna(0.0)
        portfolio['positions']=signals['positions']
        portfolio['shares']=100*signals['shares']
        portfolio['price']= signals['price']
        portfolio['holdings']=0
        portfolio['cash']=0
        pos_diff = portfolio['shares'].diff()
        commissionPayment=(portfolio['positions']*portfolio['shares']*portfolio['price']*float(self.comboBoxCommission.currentText())).cumsum()
        portfolio['holdings'] = portfolio['shares']*portfolio['price']
        portfolio['cash'] = initial_capital - (pos_diff*portfolio['price']).cumsum()-commissionPayment   
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()
        self.portfolioTable(portfolio,symbol)
        self.graphsForBacktesting(portfolio['returns'],portfolio['total'],symbol)
        
    def graphsForBacktesting(self,returns,total,symbol):    
        total.plot()
        plt.ylim(total.min(),total.max())
        plt.ylabel("Portfolio value")
        plt.title("Portfolio"+" ("+symbol+")")
        plt.show()
        pa.show_perf_stats(returns)
        pa.plot_returns(returns)
        plt.title("Returns"+" ("+symbol+")")
        plt.show()
        pa.plot_rolling_returns(returns)
        plt.title("Cumulative Returns"+" ("+symbol+")")
        plt.show()
        pa.plot_rolling_volatility(returns)
        plt.title("Rolling Volatility (6-month)"+" -"+symbol)
        plt.show()
        pa.plot_rolling_sharpe(returns)
        plt.title("Rolling Sharpe Ratio (6-month)"+" -"+symbol)
        plt.show()
        pa.plot_return_quantiles(returns)
        plt.title("Return Quantiles"+" ("+symbol+")")
        plt.show()
        pa.plot_monthly_returns_dist(returns)
        plt.title("Distribution of Monthly Returns"+" ("+symbol+")")
        plt.show()
        pa.plot_monthly_returns_timeseries(returns)
        plt.title("Monthly Returns"+" -"+symbol)
        plt.show()
        pa.plot_monthly_returns_heatmap(returns)
        plt.title("Monthly Returns (%)"+" -"+symbol)
        plt.show()
        pa.plot_annual_returns(returns)
        plt.title("Annual Returns (%)"+" -"+symbol)
        plt.show()
        pa.show_worst_drawdown_periods(returns)
        pa.plot_drawdown_periods(returns)
        plt.title("Top 10 Drawdown Periods"+" ("+symbol+")")
        plt.show()
        pa.plot_drawdown_underwater(returns)
        plt.title("Underwater Plot"+" ("+symbol+")")
        plt.show()   
             
    def portfolioTable(self,df,symbol):
        fig = go.Figure(data=[go.Table(header=dict(values=['Date','Positions','Shares','Price','Holdings','Cash','Total','Return'],
        fill_color='pink',align='left'),cells=dict(values=[df.index,
        df['positions'],df['shares'],df['price'],df['holdings'],df['cash'],df['total'],
        df['returns']],fill_color='lavender',align='left'))],layout_title_text="Portfolio("+symbol+")")
        fig.show()
  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidgetPortfolio = QtWidgets.QTabWidget()
    ui = Ui_TabWidgetPortfolio()
    ui.setupUi(TabWidgetPortfolio)
    TabWidgetPortfolio.show()
    sys.exit(app.exec_())
