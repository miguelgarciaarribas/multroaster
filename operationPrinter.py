from abc import ABCMeta, abstractmethod
from string import Template
import operation
import random


class OperationPrinter(metaclass=ABCMeta):
    """
      Abstract Class to print a specific operation.
      'operation' will be a class of type Operation found in operation.py
    """
    def __init__(self, operation):
        super().__init__()
        self.operation = operation

    @abstractmethod
    def cssClass(self):
        pass

    @abstractmethod
    def display(self, order):
        """ Produces a template with the skeleton to be printed.
          Needs to be filled in by:
             The number of the concrete operation
             The representation of the operation in question
             The result string to be displayed
        """
        return '<div class="%s flexbox"> <div class="order"> %d)' \
            ' </div>  %s <span class=result> %s </span> </div>\n %s\n' % \
            (self.cssClass(), order, '%s', str(self.operation.calculate()), '%s')

class CanvasPrinter(OperationPrinter):
    def __init__(self, operation):
        super().__init__(operation)
        self.height = 300
        self.width = 300
        self.identifier = '"canvas'+ str(random.randint(0,1000000)) + '"'
        self.clock_tmpl = '<script>drawClock($id, 200, $first, $second)</script>\n'
        self.digi_clock_tmpl = '<script>drawDigitalClock($id, "$first", "$second")</script>\n'
        self.text_tmpl = '<script>drawText($id, 72, 293, "$delta minutes $direction")</script>\n'
        self.spiral_tmpl = '<script>drawSpiral($id , $iterations)</script>\n'


    def cssClass(self):
        return 'canvasbox'

    def runOperation(self):
        script = ''

        if self.operation.type() == operation.OperationType.Time:
            script = Template(self.clock_tmpl).substitute(id=self.identifier, first=self.operation.first,
                                                          second=self.operation.second)
        elif self.operation.type() == operation.OperationType.DigitalTime:
            hour =  str(self.operation.first).zfill(2)
            minute = str(self.operation.second).zfill(2)
            script = Template(self.digi_clock_tmpl).substitute(
                id=self.identifier, first=hour, second=minute)

        if self.operation.type() == operation.OperationType.Time or \
           self.operation.type() == operation.OperationType.DigitalTime:
             if self.operation.delta != 0 and self.operation.sign is not None:
                 direction = 'earlier'
                 if self.operation.sign == '+':
                     direction = 'later'
                 script += Template(self.text_tmpl).substitute(
                     id=self.identifier, delta=self.operation.delta, direction=direction)
        elif self.operation.type() is operation.OperationType.Spiral:
            script = Template(self.spiral_tmpl).substitute(id=self.identifier, iterations=self.operation.first)

        else : raise "runOperation not supported"
        return script

    def canvas(self):
       return '<canvas id=' + self.identifier + ' width="' + str(self.width) + \
             '" height="' + str(self.height) + '"> </canvas>\n'


    def display(self, order):
        return super().display(order) % (self.canvas(), self.runOperation())

class GridPrinter(CanvasPrinter):
    def __init__(self, operation, pattern):
        super().__init__(operation)
        self.pattern = pattern
        self.width = 1100

    def cssClass(self):
        return 'gridbox'

    def runOperation(self):
        return '<script>drawFigureGrid(' + self.identifier + ', "' + self.pattern + '")</script>'

class LetterPrinter(OperationPrinter):
    def __init_(self, operation):
        super().__init__(operation)
    def cssClass(self):
        return 'letterbox'
    def display(self, order):

        text = '<div class=kidstext> %s </div>\n' % \
            str(self.operation.first.ljust(4, '_'))

        return super().display(order) % (text, '')

class EmojiPrinter(OperationPrinter):
    def __init__(self, operation):
        # assert issubclass(operation, operation.ArithmeticOperation)
        super().__init__(operation)
        self.EMOJIS= ['&#x1F3E0;', # house
                      '&#x1F434;', # horse
                      '&#x1F42E;', # cow
                      '&#x1F410;', # goat
                      '&#x1F992;', # giraffe
                      '&#x1F98D;', # elephant
                      '&#x1F418;', # gorilla
                      '&#x1F405',  # tiger
                      '&#x1F334'   # palm tree

        ]
        self.EMOJIS_PER_ROW = 4


    def cssClass(self):
        return 'letterbox'

    def generateEmoji(self, argument):
        # Emoji of the operation
        emoji = self.EMOJIS[random.randint(0, len(self.EMOJIS) -1)]

        # Divide the argument in groups of 4
        rows = argument // self.EMOJIS_PER_ROW
        lastrow = argument % self.EMOJIS_PER_ROW
        result = ' <div class="emojigroup">'
        for i in range(0, rows):
            result += '<div class="emojistep">'
            result += emoji + emoji + emoji + emoji + '</div>'
        if lastrow >0:
            result+= '<div class="emojistep">'
            for i in range(0, lastrow):
                result += emoji
            result += '</div>'
        result += '</div>'
        return result

    def generateString(self, st):
        result = ' <div class="emojigroup">'
        result +=  '<div class="emojistep">' + st + '</div>'
        result += '</div>'
        return result


    def display(self, order):
        text = '<div> %s </div>' % \
            self.generateEmoji(self.operation.first) + \
            self.generateString(self.operation.sign) + \
            self.generateString(str(self.operation.second)) + \
            self.generateString(' = ')
        return super().display(order) % (text, '')
