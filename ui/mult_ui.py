# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 901, 471))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 60, 16))
        self.label.setObjectName("label")
        self.resultDisplay = QtWidgets.QTextBrowser(self.tab)
        self.resultDisplay.setGeometry(QtCore.QRect(20, 30, 541, 371))
        self.resultDisplay.setObjectName("resultDisplay")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(810, 30, 41, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.timetableGroup = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.timetableGroup.setContentsMargins(0, 0, 0, 0)
        self.timetableGroup.setObjectName("timetableGroup")
        self.timeTable1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable1.setChecked(False)
        self.timeTable1.setObjectName("timeTable1")
        self.timetableGroup.addWidget(self.timeTable1)
        self.timeTable2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable2.setChecked(True)
        self.timeTable2.setObjectName("timeTable2")
        self.timetableGroup.addWidget(self.timeTable2)
        self.timeTable3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable3.setChecked(True)
        self.timeTable3.setObjectName("timeTable3")
        self.timetableGroup.addWidget(self.timeTable3)
        self.timeTable4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable4.setChecked(True)
        self.timeTable4.setObjectName("timeTable4")
        self.timetableGroup.addWidget(self.timeTable4)
        self.timeTable5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable5.setChecked(True)
        self.timeTable5.setObjectName("timeTable5")
        self.timetableGroup.addWidget(self.timeTable5)
        self.timeTable6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable6.setObjectName("timeTable6")
        self.timetableGroup.addWidget(self.timeTable6)
        self.timeTable7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable7.setObjectName("timeTable7")
        self.timetableGroup.addWidget(self.timeTable7)
        self.timeTable8 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable8.setChecked(True)
        self.timeTable8.setObjectName("timeTable8")
        self.timetableGroup.addWidget(self.timeTable8)
        self.timeTable9 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.timeTable9.setObjectName("timeTable9")
        self.timetableGroup.addWidget(self.timeTable9)
        self.configPanel = QtWidgets.QGroupBox(self.tab)
        self.configPanel.setGeometry(QtCore.QRect(610, 0, 169, 441))
        self.configPanel.setObjectName("configPanel")
        self.additionConfig = QtWidgets.QCheckBox(self.configPanel)
        self.additionConfig.setGeometry(QtCore.QRect(10, 20, 87, 20))
        self.additionConfig.setChecked(True)
        self.additionConfig.setObjectName("additionConfig")
        self.multiplicationConfig = QtWidgets.QCheckBox(self.configPanel)
        self.multiplicationConfig.setGeometry(QtCore.QRect(10, 90, 141, 20))
        self.multiplicationConfig.setChecked(True)
        self.multiplicationConfig.setObjectName("multiplicationConfig")
        self.timeTableConfig = QtWidgets.QRadioButton(self.configPanel)
        self.timeTableConfig.setEnabled(True)
        self.timeTableConfig.setGeometry(QtCore.QRect(30, 120, 100, 20))
        self.timeTableConfig.setChecked(False)
        self.timeTableConfig.setAutoExclusive(False)
        self.timeTableConfig.setObjectName("timeTableConfig")
        self.radioButton_2 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 150, 100, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 180, 100, 20))
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 40, 100, 20))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.substractionConfig = QtWidgets.QCheckBox(self.configPanel)
        self.substractionConfig.setGeometry(QtCore.QRect(10, 210, 141, 20))
        self.substractionConfig.setChecked(True)
        self.substractionConfig.setObjectName("substractionConfig")
        self.radioButton_5 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 240, 100, 20))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.checkBox = QtWidgets.QCheckBox(self.configPanel)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(10, 300, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.radioButton_6 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_6.setEnabled(False)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 270, 100, 20))
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setAutoExclusive(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.addFourDigits = QtWidgets.QRadioButton(self.configPanel)
        self.addFourDigits.setEnabled(True)
        self.addFourDigits.setGeometry(QtCore.QRect(30, 60, 100, 20))
        self.addFourDigits.setChecked(False)
        self.addFourDigits.setAutoExclusive(False)
        self.addFourDigits.setObjectName("addFourDigits")
        self.timeConfig = QtWidgets.QCheckBox(self.configPanel)
        self.timeConfig.setGeometry(QtCore.QRect(10, 330, 121, 20))
        self.timeConfig.setChecked(True)
        self.timeConfig.setObjectName("timeConfig")
        self.radioButton = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton.setGeometry(QtCore.QRect(30, 360, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_8 = QtWidgets.QRadioButton(self.configPanel)
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 390, 100, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(780, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.resultDisplay_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.resultDisplay_2.setGeometry(QtCore.QRect(10, 30, 541, 371))
        self.resultDisplay_2.setObjectName("resultDisplay_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.label_5.setObjectName("label_5")
        self.configPanel_2 = QtWidgets.QGroupBox(self.tab_2)
        self.configPanel_2.setGeometry(QtCore.QRect(600, 0, 169, 521))
        self.configPanel_2.setObjectName("configPanel_2")
        self.letterConfig = QtWidgets.QCheckBox(self.configPanel_2)
        self.letterConfig.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.letterConfig.setChecked(True)
        self.letterConfig.setObjectName("letterConfig")
        self.emojiConfig = QtWidgets.QCheckBox(self.configPanel_2)
        self.emojiConfig.setEnabled(True)
        self.emojiConfig.setGeometry(QtCore.QRect(10, 120, 141, 20))
        self.emojiConfig.setChecked(True)
        self.emojiConfig.setObjectName("emojiConfig")
        self.letterCheck = QtWidgets.QRadioButton(self.configPanel_2)
        self.letterCheck.setGeometry(QtCore.QRect(30, 40, 100, 20))
        self.letterCheck.setChecked(True)
        self.letterCheck.setAutoExclusive(False)
        self.letterCheck.setObjectName("letterCheck")
        self.spiralConfig = QtWidgets.QCheckBox(self.configPanel_2)
        self.spiralConfig.setEnabled(True)
        self.spiralConfig.setGeometry(QtCore.QRect(10, 90, 141, 20))
        self.spiralConfig.setChecked(True)
        self.spiralConfig.setObjectName("spiralConfig")
        self.numberCheck = QtWidgets.QRadioButton(self.configPanel_2)
        self.numberCheck.setEnabled(True)
        self.numberCheck.setGeometry(QtCore.QRect(30, 60, 100, 20))
        self.numberCheck.setChecked(True)
        self.numberCheck.setAutoExclusive(False)
        self.numberCheck.setObjectName("numberCheck")
        self.generateButton_2 = QtWidgets.QPushButton(self.configPanel_2)
        self.generateButton_2.setGeometry(QtCore.QRect(0, 490, 171, 32))
        self.generateButton_2.setObjectName("generateButton_2")
        self.gridConfig = QtWidgets.QCheckBox(self.configPanel_2)
        self.gridConfig.setEnabled(True)
        self.gridConfig.setGeometry(QtCore.QRect(10, 150, 141, 20))
        self.gridConfig.setChecked(True)
        self.gridConfig.setObjectName("gridConfig")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_4.setObjectName("label_4")
        self.studentName = QtWidgets.QLineEdit(self.centralwidget)
        self.studentName.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.studentName.setObjectName("studentName")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(620, 580, 171, 32))
        self.generateButton.setObjectName("generateButton")
        self.operationCount = QtWidgets.QLabel(self.centralwidget)
        self.operationCount.setGeometry(QtCore.QRect(760, 530, 21, 16))
        self.operationCount.setObjectName("operationCount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 530, 141, 16))
        self.label_2.setObjectName("label_2")
        self.operationAmountSlider = QtWidgets.QSlider(self.centralwidget)
        self.operationAmountSlider.setGeometry(QtCore.QRect(620, 550, 160, 22))
        self.operationAmountSlider.setMinimum(5)
        self.operationAmountSlider.setMaximum(35)
        self.operationAmountSlider.setPageStep(5)
        self.operationAmountSlider.setProperty("value", 20)
        self.operationAmountSlider.setSliderPosition(20)
        self.operationAmountSlider.setOrientation(QtCore.Qt.Horizontal)
        self.operationAmountSlider.setObjectName("operationAmountSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Preview"))
        self.timeTable1.setText(_translate("MainWindow", "1"))
        self.timeTable2.setText(_translate("MainWindow", "2"))
        self.timeTable3.setText(_translate("MainWindow", "3"))
        self.timeTable4.setText(_translate("MainWindow", "4"))
        self.timeTable5.setText(_translate("MainWindow", "5"))
        self.timeTable6.setText(_translate("MainWindow", "6"))
        self.timeTable7.setText(_translate("MainWindow", "7"))
        self.timeTable8.setText(_translate("MainWindow", "8"))
        self.timeTable9.setText(_translate("MainWindow", "9"))
        self.configPanel.setTitle(_translate("MainWindow", "Configuration"))
        self.additionConfig.setText(_translate("MainWindow", "Addition"))
        self.multiplicationConfig.setText(_translate("MainWindow", "Multiplication"))
        self.timeTableConfig.setText(_translate("MainWindow", "Time Tables"))
        self.radioButton_2.setText(_translate("MainWindow", "Single Digit"))
        self.radioButton_3.setText(_translate("MainWindow", "Double Digit"))
        self.radioButton_4.setText(_translate("MainWindow", "Three Digits"))
        self.substractionConfig.setText(_translate("MainWindow", "Substraction"))
        self.radioButton_5.setText(_translate("MainWindow", "Three Digits"))
        self.checkBox.setText(_translate("MainWindow", "Division"))
        self.radioButton_6.setText(_translate("MainWindow", "Four Digits"))
        self.addFourDigits.setText(_translate("MainWindow", "Four Digits"))
        self.timeConfig.setText(_translate("MainWindow", "Time Telling"))
        self.radioButton.setText(_translate("MainWindow", "Analog"))
        self.radioButton_8.setText(_translate("MainWindow", "Digital"))
        self.label_3.setText(_translate("MainWindow", "Time Tables:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Primary"))
        self.label_5.setText(_translate("MainWindow", "Preview"))
        self.configPanel_2.setTitle(_translate("MainWindow", "Configuration"))
        self.letterConfig.setText(_translate("MainWindow", "Letter Filling"))
        self.emojiConfig.setText(_translate("MainWindow", "Count Objects"))
        self.letterCheck.setText(_translate("MainWindow", "Letters"))
        self.spiralConfig.setText(_translate("MainWindow", "Spirals"))
        self.numberCheck.setText(_translate("MainWindow", "Numbers"))
        self.generateButton_2.setText(_translate("MainWindow", "Generate"))
        self.gridConfig.setText(_translate("MainWindow", "Grid"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Early Years"))
        self.label_4.setText(_translate("MainWindow", "Student Name:"))
        self.studentName.setText(_translate("MainWindow", " Bruno Garcia"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.operationCount.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Number of operations:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
