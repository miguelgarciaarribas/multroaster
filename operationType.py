from enum import Enum, unique

@unique
class Category(Enum):
     EarlyYears = 0
     Primary = 1
     Undefined = 2

@unique
class OperationType(Enum):
     Addition = (0, Category.Primary)
     Substraction = (1, Category.Primary)
     Multiplication = (2, Category.Primary)
     Division = (3, Category.Primary)
     Fraction = (4, Category.Primary) # Not Supported
     Time = (5, Category.Primary)
     DigitalTime = (6, Category.Primary)
     Spiral = (7, Category.EarlyYears)
     DottedLetter = (8, Category.EarlyYears)
     GridWrite = (9, Category.EarlyYears)
     EmojiAddition = (10, Category.EarlyYears)
     Undefined = (11, Category.Undefined)

     def __init__(self, value, category):
          self.category = category
