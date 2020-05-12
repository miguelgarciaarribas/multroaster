from PyQt5.QtWidgets import QSlider

class SliderGroup():
     def __init__(self, mainWindow):
         self.mainWindow = mainWindow

         # Associates a slider with a counter label
         self.sliderCombo = {}

         # Associates a slider with their current value. We could read
         # from the label text but seems hacky
         self.sliderValues = {}

         self.totalSlider = mainWindow.operationAmountSlider
         self.totalCountLabel = mainWindow.operationCount
         self.totalCount = 0
         self.maxCount = 0

         self.sliderCombo[mainWindow.additionAmountSlider] = mainWindow.additionCount
         self.sliderCombo[mainWindow.multiplicationAmountSlider] = \
             mainWindow.multiplicationCount
         self.sliderCombo[mainWindow.substractionAmountSlider] = \
             mainWindow.substractionCount
         self.sliderCombo[mainWindow.timeTellingAmountSlider] = \
             mainWindow.timeTellingCount
         self.sliderCombo[mainWindow.emojiAmountSlider] = \
             mainWindow.emojiCount
         self.sliderCombo[mainWindow.spiralAmountSlider] = \
             mainWindow.spiralCount
         self.sliderCombo[mainWindow.gridAmountSlider] = \
             mainWindow.gridCount
         self.sliderCombo[mainWindow.letterAmountSlider] = \
             mainWindow.letterCount

         for slider, label in self.sliderCombo.items():
              slider.setTickPosition(QSlider.TicksBelow)
              slider.valueChanged.connect(self.sliderValueChanged)
              label.setText(str(slider.value()))
              self.sliderValues[slider] = slider.value()
              self.totalCount += slider.value()
              self.maxCount += slider.maximum()
         self.totalCountLabel.setText(str(self.totalCount))
         self.totalSlider.setMaximum(self.maxCount)
         self.totalSlider.setTickPosition(QSlider.TicksBelow)


     def sliderValueChanged(self):
         slider =self.mainWindow.sender()
         label = self.sliderCombo[slider]
         label.setText(str(slider.value()))

         # refresh total count
         self.totalCount -= self.sliderValues[slider]
         self.totalCount += slider.value()
         self.sliderValues[slider] = slider.value()
         self.totalCountLabel.setText(str(self.totalCount))
         self.totalSlider.setValue(self.totalCount)
