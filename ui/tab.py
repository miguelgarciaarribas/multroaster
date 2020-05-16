from operationType import Category
from ui.slider import SliderGroup


class TabGroup():
    def __init__(self, mainWindow, sliderGroup):
        self.mainWindow = mainWindow
        self.studentName = mainWindow.studentName
        self.tab = mainWindow.tabWidget
        self.tab.setCurrentIndex(0)
        self.tab.currentChanged.connect(self.tabChanged)
        self.sliderGroup = sliderGroup

    def tabChanged(self, current):
        if (current == 0):
            self.studentName.setText("Bruno Garcia")
            self.sliderGroup.resetSliders(Category.Primary)
        else:
            self.studentName.setText("Maya Garcia")
            self.sliderGroup.resetSliders(Category.EarlyYears)