from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSlider

from ui.mult_ui import *
from generator import *

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
        self.operationCount.setText(str(self.operationAmountSlider.value()))

        # Main Tab
        self.tabWidget.currentChanged.connect(self.tabChanged)

    def tabChanged(self, current):
        if (current == 0):
            self.studentName.setText("Bruno Garcia")
        else:
            self.studentName.setText("Maya Garcia")

    def operationSliderValuechange(self):
        self.operationCount.setText(str(self.operationAmountSlider.value()))

    def generateMult(self):
        config = self.generateConfig()
        generate(config)
        self.resultDisplay.setSource(QtCore.QUrl(config.fileName))

    def generateConfig(self):
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

        config.studentName = self.studentName.text()

        # TODO generate temporary html files based on date and student
        config.fileName = "res.html"

        config.maxCount = self.operationAmountSlider.value()

        config.includeAdditions = self.additionConfig.isChecked()
        config.addFourDigits = self.addFourDigits.isChecked()
        config.includeSubstractions = self.substractionConfig.isChecked()
        config.includeMultiplications = self.multiplicationConfig.isChecked()
        config.includeTimeTables = self.timeTableConfig.isChecked()
        config.includeTimes = self.timeConfig.isChecked()
        config.includeEmojiAdditions = self.emojiConfig.isChecked()
        config.includeGrids = self.gridConfig.isChecked()

        # TODO: Discriminate numbers and letters
        config.includeLetters = self.letterConfig.isChecked()
        config.includeSpirals = self.spiralConfig.isChecked()


        return config



if __name__== "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
