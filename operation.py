from abc import ABCMeta, abstractmethod
import random

from operationType import OperationType
from operationPrinter import CanvasPrinter, EmojiPrinter, GridPrinter, LetterPrinter


class Operation(metaclass=ABCMeta):
    """Abstract class to represent an operation with multiple operands
        operands = [] list of parameters for the operation. Can be ints for mathematical ones or just parameters
          for graphical operations like filling in a spiral. Subclasses determine this.

       Offers a generic display method valid for mathemathical operations. Graphical operation implement
       their own for now.
    """
    def __init__(self, operands):
        super().__init__()
        self.first = operands[0]
        if len(operands) > 1:
            self.second = operands[1]
        else:
            self.second = 0

    def __str__(self):
        return "<%s %s>" %  (self.first, self.second)

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def category(self):
        """
        Whether the operation belongs to early years or primary.
        """
        pass

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def display(self, order):
        pass


class ArithmeticOperation(Operation):
    """ Abstract: Represents a Mathematical operation with common methods for display and calculations. """
    def __init__(self, operands, sign):
        super().__init__(operands)
        self.sign = sign

    def __str__(self):
        # TODO check # of parameters
        return "%s %s %s = %s" % (self.first, self.sign, self.second)

    def _operation(self):
        return "%s %s %s =" % (self.first, self.sign, self.second)

    def category(self):
        return Category.Primary

    def display(self, order):
        return '<div class="box flexbox"> <div class="order"> %d) </div>' \
             ' <span class="control"> %s </span> <span class=result> %s </span>' \
             ' </div>\n' % \
    (order, self._operation(), str(self.calculate()))

class Division(ArithmeticOperation):
    """ Represents a division operation.

       For example 50 ÷ 5 =
    """
    def __init__(self, first, second):
        if first > second:
            super().__init__([first, second], '÷')
        else:
            super().__init__([second, first], '÷')

    def type(self):
        return OperationType.Division

    def calculate(self):
         if (self.first % self.second) == 0:
             return str(self.first // self.second)
         return str(self.first // self.second) + 'r' + str(self.first % self.second)

class Multiplication(ArithmeticOperation):
    """ Represents a multiplication operation.

       For example 50 x 5 =
    """
    def __init__(self, first, second):
        order = random.randint(0,1)
        if order:
            super().__init__([first, second], 'x')
        else:
            super().__init__([second, first], 'x')

    def type(self):
        return OperationType.Multiplication

    def calculate(self):
        return self.first * self.second

class Substraction(ArithmeticOperation):
    """ Represents a substraction operation.

       For example 40 - 5 =
    """
    def __init__(self, first, second):
        if (first > second):
            super().__init__([first, second], '-')
        else:
            super().__init__([second, first], '-')

    def type(self):
        return OperationType.Substraction

    def calculate(self):
        return self.first - self.second

class Addition(ArithmeticOperation):
    """ Contains an addition operation.

        For example 40 + 5 =
    """
    def __init__(self, first, second):
        order = random.randint(0,1)
        if order:
            super().__init__([first, second], '+')
        else:
            super().__init__([second, first], '+')

    def type(self):
        return OperationType.Addition

    def calculate(self):
        return self.first + self.second

class EmojiAddition(Addition):
    """ Variant of addition that shows emojis for one of the operands.
    """
    def __init__(self, first, second):
         super().__init__(first, second)
         self.printer = EmojiPrinter(self)

    def type(self):
         return OperationType.EmojiAddition

    def category(self):
         return Category.EarlyYears

    def display(self, order):
         return  self.printer.display(order)


class Time(Operation):
    """ Contains the logic for displaying a time. Current representation is though an
        analog clock. The result is offered in digital format in 12h format.

       For example 02:45
    """
    def __init__(self, first, second, delta=0, sign=None):
        super().__init__([first, second])
        self.delta = delta
        self.sign = sign
        self.printer = CanvasPrinter(self)

    def type(self):
        return OperationType.Time

    def category(self):
        return Category.Primary

    def calculate(self):
         minute = self.second
         hour = self.first
         if self.sign == "-":
              minute -= self.delta
              if minute < 0:
                   minute +=60
                   hour -=1
                   if hour < 0:
                        hour = 11
         elif self.sign == "+":
              minute += self.delta
              if minute >=60:
                   minute = minute % 60;
                   hour += 1
                   if hour > 12:
                        hour = 12

         return str(hour).zfill(2) + ' : ' + str(minute).zfill(2)

    def display(self, order):
        return self.printer.display(order)

class DigitalTime(Time):
     def __init__(self, first, second, delta=0, sign=None):
          super().__init__(first, second, delta, sign)
     def type(self):
          return OperationType.DigitalTime

class Spiral(Operation):
    """ Contains the logic for drawing a spiral """
    def __init__(self, iterations):
        super().__init__([iterations])
        self.printer = CanvasPrinter(self)

    def type(self):
        return OperationType.Spiral

    def calculate(self):
        return self.first

    def category(self):
        return Category.EarlyYears

    def display(self, order):
        return self.printer.display(order)

class Grid(Operation):
    """ Contains the logic for drawing a spiral """
    def __init__(self, pattern):
        super().__init__([pattern])
        self.pattern = pattern
        self.printer = GridPrinter(self, pattern)

    def type(self):
        return OperationType.GridWrite

    def category(self):
        return Category.EarlyYears

    def calculate(self):
        return self.first

    def display(self, order):
        return self.printer.display(order)




class Letters(Operation):
    """ Contains the logic for filling a pair of letters pair in dotted format. """
    def __init__(self, first):
        super().__init__([first])
        self.printer = LetterPrinter(self)

    def type(self):
        return OperationType.Letters

    def calculate(self):
        return self.first

    def category(self):
         return Category.EarlyYears

    def display(self, order):
        return self.printer.display(order)
