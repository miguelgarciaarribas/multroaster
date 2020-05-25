from PyQt5 import QtCore

from operationType import Category
from ui.slider import SliderGroup
from multiprinter import MultiPrinter


class TabGroup():
    def __init__(self, mainWindow, sliderGroup):
        self.mainWindow = mainWindow
        self.studentName = mainWindow.studentName
        self.tab = mainWindow.tabWidget
        self.tab.setCurrentIndex(0)
        self.tab.currentChanged.connect(self.tabChanged)
        self.sliderGroup = sliderGroup
        self.tabChanged(0)

    def tabChanged(self, current):
        category = Category.Undefined
        if (current == 0):
            category = Category.Primary
            self.studentName.setText('Bruno Garcia')
            self.sliderGroup.resetSliders(category)
            self.mainWindow.previewLayout.removeWidget(self.mainWindow.resultDisplay)
            self.mainWindow.previewLayout.addWidget(self.mainWindow.resultDisplay)
        else:
            category = Category.EarlyYears
            self.studentName.setText('Maya Garcia')
            self.sliderGroup.resetSliders(category)
            self.mainWindow.previewLayoutEY.addWidget(self.mainWindow.resultDisplay)

        self.displayIntro(category)

    def displayIntro(self, category):
        # Intro
        intro = MultiPrinter().printIntro(category)
        self.mainWindow.resultDisplay.setHtml(intro, QtCore.QUrl('/'))
        self.mainWindow.resultDisplay.show()
