from PyQt5.QtWidgets import QSlider

from operationType import OperationType

class SliderGroup():
     def __init__(self, mainWindow):
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

         self.sliderCombo[mainWindow.additionAmountSlider] = mainWindow.additionCount
         self.sliderValues[mainWindow.additionAmountSlider] = (OperationType.Addition, 0)

         self.sliderCombo[mainWindow.multiplicationAmountSlider] = \
             mainWindow.multiplicationCount
         self.sliderValues[mainWindow.multiplicationAmountSlider] = (OperationType.Multiplication, 0)

         self.sliderCombo[mainWindow.substractionAmountSlider] = \
             mainWindow.substractionCount
         self.sliderValues[mainWindow.substractionAmountSlider] = (OperationType.Substraction, 0)

         self.sliderCombo[mainWindow.divisionAmountSlider] = \
             mainWindow.divisionCount
         self.sliderValues[mainWindow.divisionAmountSlider] = (OperationType.Division, 0)

         self.sliderCombo[mainWindow.timeTellingAmountSlider] = \
             mainWindow.timeTellingCount
         self.sliderValues[mainWindow.timeTellingAmountSlider] = (OperationType.Time, 0)

         self.sliderCombo[mainWindow.emojiAmountSlider] = \
             mainWindow.emojiCount
         self.sliderValues[mainWindow.emojiAmountSlider] = (OperationType.EmojiAddition, 0)

         self.sliderCombo[mainWindow.spiralAmountSlider] = \
             mainWindow.spiralCount
         self.sliderValues[mainWindow.spiralAmountSlider] = (OperationType.Spiral, 0)

         self.sliderCombo[mainWindow.gridAmountSlider] = \
             mainWindow.gridCount
         self.sliderValues[mainWindow.gridAmountSlider] = (OperationType.GridWrite, 0)

         self.sliderCombo[mainWindow.letterAmountSlider] = \
             mainWindow.letterCount
         self.sliderValues[mainWindow.letterAmountSlider] = (OperationType.DottedLetter, 0)

         for slider, label in self.sliderCombo.items():
              slider.setTickPosition(QSlider.TicksBelow)
              slider.valueChanged.connect(self.sliderValueChanged)
              label.setText(str(slider.value()))
              self.sliderValues[slider] = (self.sliderValues[slider][0], slider.value())
              self.totalCount += slider.value()
              self.maxCount += slider.maximum()
         self.totalCountLabel.setText(str(self.totalCount))
         self.totalSlider.setMaximum(self.maxCount)
         self.totalSlider.setTickPosition(QSlider.TicksBelow)


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
