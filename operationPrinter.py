from abc import ABCMeta, abstractmethod
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
        self.operation = operation
        self.identifier = '"canvas'+ str(random.randint(0,1000000)) + '"'

    def cssClass(self):
        return 'canvasbox'

    def runOperation(self, identifier):
        if self.operation.type() is operation.OperationType.Time:
             return '<script>drawClock(' + identifier + ', 200, ' + str(self.operation.first) + ', ' \
               + str(self.operation.second) + ')</script>'
        elif self.operation.type() is operation.OperationType.Spiral:
            return '<script>drawSpiral(' + self.identifier + ', '+ str(self.operation.first) + ' )</script>'

        else : raise "runOperation not supported"


    def canvas(self):
       return '<canvas id=' + self.identifier + ' width="' + str(self.width) + \
             '" height="' + str(self.height) +'"> </canvas>\n'


    def display(self, order):
        return super().display(order) % (self.canvas(), self.runOperation(self.identifier))


class DivPrinter(OperationPrinter):
    def __init_(self, operation):
        super().__init__(operation)
    def cssClass(self):
        return 'letterbox'
    def display(self, order):
        text = '<div class=kidstext> %s </div>\n' % \
            (str(self.operation.first) + ' ' + str(self.operation.second))
        return super().display(order) % (text, '')

class EmojiPrinter(OperationPrinter):
    def __init__(self, operation):
        # assert issubclass(operation, operation.ArithmeticOperation)
        super().__init__(operation)
        self.EMOJIS= ['&#x1F3E0;', # house
                  '&#x1F434;', # horse
                  '&#x1F42E;', # cow
                  '&#x1F410;'  # goat
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
