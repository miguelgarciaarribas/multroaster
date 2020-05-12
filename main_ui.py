from PyQt5 import QtCore, QtWidgets

from ui.mult_ui import *
from generator import *
from ui.slider import SliderGroup


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Generate Button
        self.generateButton.clicked.connect(self.generateMult)

        # Main Tab
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tabChanged)

        # Sliders
        self.sliders = SliderGroup(self)

    def tabChanged(self, current):
        if (current == 0):
            self.studentName.setText("Bruno Garcia")
        else:
            self.studentName.setText("Maya Garcia")

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
        config.resetConfig()

        config.timetables = timetables

        config.studentName = self.studentName.text()

        # TODO generate temporary html files based on date and student
        config.fileName = "res.html"

        config.operations[OperationType.Addition] = self.additionAmountSlider.value()
        config.addFourDigits = self.addFourDigits.isChecked()

        config.operations[OperationType.Substraction] = \
            self.substractionAmountSlider.value()

        config.operations[OperationType.Multiplication] = \
            self.multiplicationAmountSlider.value()
        config.includeTimeTables = True

        config.operations[OperationType.Time] = self.timeTellingAmountSlider.value()
        config.digitalTime = self.addDigital.isChecked()
        config.deltaToTimes = self.timeDeltas.isChecked()

        config.operations[OperationType.EmojiAddition] = \
            self.emojiAmountSlider.value()
        config.operations[OperationType.Spiral] = \
            self.spiralAmountSlider.value()
        config.operations[OperationType.GridWrite] = \
            self.gridAmountSlider.value()
        config.operations[OperationType.DottedLetter] = \
            self.letterAmountSlider.value()

        config.includeDottedLetters = self.letterCheck.isChecked()
        config.includeDottedNumbers = self.numberCheck.isChecked()

        return config



if __name__== "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
