from PyQt5 import QtCore

from operationType import Category
from ui.slider import SliderGroup
from multiprinter import MultiPrinter


class TabGroup():
    def __init__(self, mainWindow, sliderGroup, args):
        self.mainWindow = mainWindow
        self.args = args
        self.studentName = mainWindow.studentName
        self.tab = mainWindow.tabWidget
        self.tab.setCurrentIndex(0)
        self.tab.currentChanged.connect(self.tabChanged)
        self.sliderGroup = sliderGroup

        if not args.experimental:
            self.mainWindow.tabWidget.removeTab(2)
        self.tabChanged(0)

    def tabChanged(self, current):
        category = Category.Undefined
        if (current == Category.Primary.enumValue):
            category = Category.Primary
            self.studentName.setText('Bruno Garcia')
            self.sliderGroup.resetSliders(category)
            self.mainWindow.previewLayout.removeWidget(self.mainWindow.resultDisplay)
            self.mainWindow.previewLayout.addWidget(self.mainWindow.resultDisplay)
        elif (current == Category.EarlyYears.enumValue):
            category = Category.EarlyYears
            self.studentName.setText('Maya Garcia')
            self.sliderGroup.resetSliders(category)
            self.mainWindow.previewLayoutEY.addWidget(self.mainWindow.resultDisplay)
        else:
            self.studentName.setText('')

        self.displayIntro(category)

    def displayIntro(self, category):
        if category == Category.Undefined:
            return
        intro = MultiPrinter().printIntro(category)
        self.mainWindow.resultDisplay.setHtml(intro, QtCore.QUrl('/'))
        self.mainWindow.resultDisplay.show()
