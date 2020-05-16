from PyQt5.QtWidgets import QSlider

from operationType import OperationType

class SliderGroup():
     def __init__(self, mainWindow, category):
         self.mainWindow = mainWindow

         # Associates a slider with a counter label
         self.sliderCombo = {}

         # Associates a slider with their current value and op type.
         # slider -> (operationType, numberOfOperations)
         self.sliderValues = {}

         self.totalSlider = mainWindow.operationAmountSlider
         self.totalCountLabel = mainWindow.operationCount
         self.totalCount = 0
         self.maxCount = 0
         self.totalSlider.setTickPosition(QSlider.TicksBelow)

         self.sliderCombo[self.mainWindow.additionAmountSlider] = self.mainWindow.additionCount
         self.sliderValues[self.mainWindow.additionAmountSlider] = (OperationType.Addition, 0)

         self.sliderCombo[self.mainWindow.multiplicationAmountSlider] = \
             self.mainWindow.multiplicationCount
         self.sliderValues[self.mainWindow.multiplicationAmountSlider] = \
            (OperationType.Multiplication, 0)
         self.sliderCombo[self.mainWindow.substractionAmountSlider] = \
             self.mainWindow.substractionCount
         self.sliderValues[self.mainWindow.substractionAmountSlider] = \
            (OperationType.Substraction, 0)

         self.sliderCombo[self.mainWindow.divisionAmountSlider] = self.mainWindow.divisionCount
         self.sliderValues[self.mainWindow.divisionAmountSlider] = (OperationType.Division, 0)

         self.sliderCombo[self.mainWindow.timeTellingAmountSlider] = \
             self.mainWindow.timeTellingCount
         self.sliderValues[self.mainWindow.timeTellingAmountSlider] = (OperationType.Time, 0)

         self.sliderCombo[self.mainWindow.emojiAmountSlider] = self.mainWindow.emojiCount
         self.sliderValues[self.mainWindow.emojiAmountSlider] =  \
            (OperationType.EmojiAddition, 0)

         self.sliderCombo[self.mainWindow.spiralAmountSlider] =  self.mainWindow.spiralCount
         self.sliderValues[self.mainWindow.spiralAmountSlider] = (OperationType.Spiral, 0)

         self.sliderCombo[self.mainWindow.gridAmountSlider] = self.mainWindow.gridCount
         self.sliderValues[self.mainWindow.gridAmountSlider] = (OperationType.GridWrite, 0)

         self.sliderCombo[self.mainWindow.letterAmountSlider] = self.mainWindow.letterCount
         self.sliderValues[self.mainWindow.letterAmountSlider] = \
             (OperationType.DottedLetter, 0)

         for slider, label in self.sliderCombo.items():
              slider.setTickPosition(QSlider.TicksBelow)
              slider.valueChanged.connect(self.sliderValueChanged)

         self.resetSliders(category)


     def resetSliders(self, category):
         self.maxCount = 0
         self.totalCount = 0
         for slider, label in self.sliderCombo.items():
              label.setText(str(slider.value()))
              if self.sliderValues[slider][0].category == category:
                   self.sliderValues[slider] = (self.sliderValues[slider][0], slider.value())
                   self.totalCount += slider.value()
                   self.maxCount += slider.maximum()
         self.totalCountLabel.setText(str(self.totalCount))
         self.totalSlider.setMaximum(self.maxCount)


     def sliderValueChanged(self):
         slider = self.mainWindow.sender()
         label = self.sliderCombo[slider]
         label.setText(str(slider.value()))

         # refresh total count
         operation = self.sliderValues[slider][0]
         oldValue = self.sliderValues[slider][1]
         self.totalCount -= oldValue
         self.totalCount += slider.value()
         self.sliderValues[slider] = (operation, slider.value())
         self.totalCountLabel.setText(str(self.totalCount))
         self.totalSlider.setValue(self.totalCount)
