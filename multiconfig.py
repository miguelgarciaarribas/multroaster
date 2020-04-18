import random

class MultiConfig:
    """
    Contains the configuraation to decide how the multiplication should be generated.
    """
    def __init__(self):
        self.studentName = "Bruno"

        # Tables allowed
        self.timetables = []

        # Max multiplicator
        self.maxmult = 12
        
        # Number of multiplications to generate
        self.maxCount = 0

        # Whether to calculate the result
        self.resolve = True

        # Main variants
        self.includeMultiplications = True
        self.includeAdditions = True
        self.includeSubstractions = True
        self.includeTimes = True

        # Sub variants
        self.includeTimeTables =  True

        # output file
        self.fileName = "res.html"

class Operation:
    """ Generic operation with two operands
        operands = [] ints
    """
    def __init__(self, operands, sign, result = False):
        assert len(operands) >=2
        self.first = operands[0]
        self.second = operands[1]
        self.sign = sign
        self.result = result
    def __str__(self):
        # check # of parameters
        return "%s %s %s = %s" % (self.first, self.sign, self.second, self.calculate())
    def operation(self):
        return "%s %s %s =" % (self.first, self.sign, self.second)

    def calculate(self):
        raise Exception('Operation not Supported')

    def display(self, order):
        return "<div class=box> <span><b>%d)</b>  %s </span> <span class=result> %s </span> </div>\n" % \
    (order, self.operation(), str(self.calculate()))


class Multiplication(Operation):
    """ Contains a multiplication itself """
    def __init__(self, first, second, result):
        order = random.randint(0,1)
        if order:
            Operation.__init__(self, [first, second], 'x', result)
        else:
            Operation.__init__(self, [second, first], 'x', result)
    def calculate(self):
        return self.first * self.second


class Substraction(Operation):
    """ Contains a substraction itself """
    def __init__(self, first, second, result):
        if (first > second):
            Operation.__init__(self, [first, second], '-', result)
        else:
            Operation.__init__(self, [second, first], '-', result)
    def calculate(self):
        return self.first - self.second

class Addition(Operation):
    """ Contains a substraction itself """
    def __init__(self, first, second, result):
        order = random.randint(0,1)
        if order:
            Operation.__init__(self, [first, second], '+', result)
        else:
            Operation.__init__(self, [second, first], '+', result)
    def calculate(self):
        return self.first + self.second


class Times(Operation):
    """ Contains the logic for displaying a time """
    def __init__(self, first, second, result):
        Operation.__init__(self, [first, second], ':', result)
    def calculate(self):
        return str(self.first).zfill(2) + ' : ' + str(self.second).zfill(2)
    def operation(self):
       identifier='"canvas'+str(self.first)+str(self.second)+'"'
       return '<canvas id=' + identifier + ' width="300" height="300"</canvas>\n' +  \
           '<script>drawClock(' + identifier + ', 200, 300, 300, ' + str(self.first) + ', ' \
               + str(self.second) + ')</script>'
       # TODO: allow digital times
    def display(self, order):
        return '<div class=clockbox> <span align="center"><b>%d)</b> %s </span> <span class=result> %s </span> </div>\n' % \
    (order, self.operation(), str(self.calculate()))
