from PyQt5 import QtCore

from ui.mult_ui import *
from generator import *
from multiconfig import Addition, MultiConfig, Multiplication, Substraction
from multiprinter import MultiPrinter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.generateButton.clicked.connect(self.generateMult)
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
        config.maxCount = 24

        config.includeAdditions = self.additionConfig.isChecked()
        config.includeSubstractions = self.substractionConfig.isChecked()
        config.includeMultiplications = self.multiplicationConfig.isChecked()
        config.includeTimeTables = self.timeTableConfig.isChecked()
        
        return config

def generate(config):
    multiplications =  generateMultiplications(config)
    substractions = generateSubstractions(config)
    additions = generateAdditions(config)
    result = list(multiplications) + list( substractions) + list(additions)
    random.shuffle(result)
    
    printer = MultiPrinter()
    result = printer.print(result) 
    print(result)
    with open("res.html", "w") as f:
        f.write(result)


if __name__== "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
