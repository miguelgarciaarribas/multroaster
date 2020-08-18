from enum import Enum, unique

@unique
class Category(Enum):
     Primary = (0, 'Primary')
     EarlyYears = (1, 'Early Years')
     Undefined = (2, 'Undefined')

     def __init__(self, value, representation):
          self.representation = representation
          self.enumValue = value


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
     Maze = (11, Category.EarlyYears)
     Undefined = (11, Category.Undefined)

     def __init__(self, value, category):
          self.category = category
     def __str__(self):
          return str(self.value)
