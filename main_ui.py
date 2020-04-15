from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSlider

from ui.mult_ui import *
from generator import *
#from multiconfig import Addition, MultiConfig, Multiplication, Substraction
#from multiprinter import MultiPrinter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Generate Button
        self.generateButton.clicked.connect(self.generateMult)

        # Operation Slider
        # TODO check if we can do this in the UI directly
        self.operationAmountSlider.setTickPosition(QSlider.TicksBelow)
        self.operationAmountSlider.valueChanged.connect(self.operationSliderValuechange)

    def operationSliderValuechange(self):
        print(self.operationAmountSlider.value())

    def generateMult(self):
        config = self.getConfig()
        generate(config)
        self.resultDisplay.setSource(QtCore.QUrl("res.html"))

    def getConfig(self):
        """ Loads a configuration based on the UI settings"""
        
        timetables = []
        if self.timeTable1.isChecked():
            timetables.append(1)
        if self.timeTable2.isChecked():
            timetables.append(2)
        if self.timeTable3.isChecked():
            timetables.append(3)
        if self.timeTable4.isChecked():
            timetables.append(4)
        if self.timeTable5.isChecked():
            timetables.append(5)
        if self.timeTable6.isChecked():
            timetables.append(6)
        if self.timeTable7.isChecked():
            timetables.append(7)
        if self.timeTable8.isChecked():
            timetables.append(8)
        if self.timeTable9.isChecked():
            timetables.append(9)

        config = MultiConfig()
        config.timetables = timetables

        # TODO add a number to the slide and update it via slider events
        config.maxCount = self.operationAmountSlider.value()

        config.includeAdditions = self.additionConfig.isChecked()
        config.includeSubstractions = self.substractionConfig.isChecked()
        config.includeMultiplications = self.multiplicationConfig.isChecked()
        config.includeTimeTables = self.timeTableConfig.isChecked()
        config.includeTimes = self.timeConfig.isChecked()
        
        return config



if __name__== "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
