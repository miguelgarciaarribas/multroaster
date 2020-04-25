from abc import ABCMeta, abstractmethod
import random


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
    @abstractmethod
    def display(self, order):
        pass


class MathOperation(Operation):
    """ Abstract: Represents a Mathematical operation with common methods for display and calculations. """
    def __init__(self, operands, sign):
        super().__init__(operands)
        self.sign = sign

    def __str__(self):
        # TODO check # of parameters
        return "%s %s %s = %s" % (self.first, self.sign, self.second)

    @abstractmethod
    def _calculate(self):
        pass

    def _operation(self):
        return "%s %s %s =" % (self.first, self.sign, self.second)

    def display(self, order):
        return "<div class=box> <span><b>%d)</b>  %s </span> <span class=result> %s </span> </div>\n" % \
    (order, self._operation(), str(self._calculate()))

class Multiplication(MathOperation):
    """ Represents a multiplication operation.

       For example 50 x 5 =
    """
    def __init__(self, first, second):
        order = random.randint(0,1)
        if order:
            super().__init__([first, second], 'x')
        else:
            super().__init__([second, first], 'x')
    def _calculate(self):
        return self.first * self.second

class Substraction(MathOperation):
    """ Represents a substraction operation.

       For example 40 - 5 =
    """
    def __init__(self, first, second):
        if (first > second):
            super().__init__([first, second], '-')
        else:
            super().__init__([second, first], '-')
    def _calculate(self):
        return self.first - self.second

class Addition(MathOperation):
    """ Contains an addition operation.

        For example 40 + 5 =
    """
    def __init__(self, first, second):
        order = random.randint(0,1)
        if order:
            super().__init__([first, second], '+')
        else:
            super().__init__([second, first], '+')
    def _calculate(self):
        return self.first + self.second

# TODO: create a GrapahicalOperation with common display logic for all the operations below

class Times(Operation):
    """ Contains the logic for displaying a time. Current representation is though an
        analog clock. The result is offerend in digital format in 12h format.

       For example 02:45
    """
    def __init__(self, first, second):
        super().__init__([first, second])

    def resolve(self):
        return str(self.first).zfill(2) + ' : ' + str(self.second).zfill(2)

    def canvas(self):
       identifier='"clock'+str(self.first)+str(self.second) + str(random.randint(0,10000)) + '"'
       return '<canvas id=' + identifier + ' width="300" height="300" </canvas>\n' +  \
           '<script>drawClock(' + identifier + ', 200, ' + str(self.first) + ', ' \
               + str(self.second) + ')</script>'
       # TODO: build support for  digital times

    def display(self, order):
        return '<div class=canvasbox> <b>%d)</b> <span align="center"> %s </span> <span class=result> %s </span> </div>\n' % \
    (order, self.canvas(), str(self.resolve()))

class Letters(Operation):
    """ Contains the logic for filling a pair of letters pair in dotted format. """
    def __init__(self, first,  second):
        super().__init__([first, second])
    def calculate(self):
        return str(self.first) + ' , ' + str(self.second)
    def display(self, order):
        return '<div class=letterbox> <b>%d)</b> <span class=kidstext align="center"> %s </span> <span class=result> %s </span> </div>' % \
            (order, str(self.first) + ' ' + str(self.second) , self.calculate())

class Spiral(Operation):
    """ Contains the logic for drawing a spiral """
    def __init__(self, iterations):
        super().__init__([iterations])
    def calculate(self):
        return self.first
    def operation(self):
       identifier='"spiral' + str(random.randint(0,10000)) + '"'
       return '<canvas id=' + identifier + ' width="310" height="310"</canvas>\n' +  \
           '<script>drawSpiral(' + identifier + ', '+ str(self.first) + ' )</script>'
    def display(self, order):
        return '<div class=canvasbox> <span> <b>%d) </b></span> <span> %s </span> <div class=result> %s </div> </div>\n' % \
    (order, self.operation(), str(self.calculate()))
