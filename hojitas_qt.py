from PyQt5 import QtCore, QtWidgets

import os


from ui.mult_ui import *
from generator import *
from ui.slider import SliderGroup
from ui.tab import TabGroup

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
     Main UI for the hojitas application.
    """
    def __init__(self, args):
        QtWidgets.QMainWindow.__init__(self, *[], **{})
        self.setupUi(self)

        # Generate Button
        self.generateButton.clicked.connect(lambda: self.generateRoaster(args))

        # Sliders
        self.sliders = SliderGroup(self, self.category())

        # Main Tab
        self.tabs = TabGroup(self, self.sliders)


    def generateRoaster(self, args):
        config = self.generateConfig()
        if args.output:
            config.fileName = args.output
        generate(config)
        path = os.getcwd() + '/' + config.fileName
        url = QtCore.QUrl.fromLocalFile(path)
        self.resultDisplay.load(QtCore.QUrl.fromLocalFile(path))
        self.resultDisplay.show()

    def generateConfig(self):
        """ Loads a configuration based on the UI settings """

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
        config.resetConfig()

        config.timetables = timetables

        config.studentName = self.studentName.text()

        # TODO consider generating temporary html files based on date and student
        config.fileName = "res.html"


        for operation, value in self.sliders.sliderValues.values():
            config.operations[operation] = value

        config.filterBy = [self.category()]

        config.addFourDigits = self.addFourDigits.isChecked()
        config.includeTimeTables = True
        config.digitalTime = self.addDigital.isChecked()
        config.deltaToTimes = self.timeDeltas.isChecked()
        config.includeDottedLetters = self.letterCheck.isChecked()
        config.includeDottedNumbers = self.numberCheck.isChecked()

        return config

    def category(self):
        if self.tabWidget.currentIndex() == 0:
            return Category.Primary
        return Category.EarlyYears

def runApp(args):
    app = QtWidgets.QApplication([])
    window = MainWindow(args)
    window.show()
    app.exec_()
