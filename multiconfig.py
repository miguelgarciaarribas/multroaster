import random

class MultiConfig:
    """
    Contains the configuraation to decide how the multiplication should be generated.
    """
    def __init__(self):
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

class Operation:
    """ Generic operation with two operands"""
    def __init__(self, first, second, sign, result = False):
        self.first = first
        self.second = second
        self.sign = sign
        self.result = result
    def __str__(self):
        return "%s %s %s = %s" % (self.first, self.sign, self.second, self.calculate())
    def operation(self):
        return "%s %s %s =" % (self.first, self.sign, self.second)

    def calculate(self):
        raise Exception('Operation not Supported')

    def display(self):
        return "<div class=box> <span> %s </span> <span class=result> %s </span> </div>\n" % (self.operation(), str(self.calculate()))


class Multiplication(Operation):
    """ Contains a multiplication itself """
    def __init__(self, first, second, result):
        order = random.randint(0,1)
        if order:
            Operation.__init__(self, first, second, 'x', result)
        else:
            Operation.__init__(self, second, first, 'x', result)
    def calculate(self):
        return self.first * self.second


class Substraction(Operation):
    """ Contains a substraction itself """
    def __init__(self, first, second, result):
        if (first > second):
            Operation.__init__(self, first, second, '-', result)
        else:
            Operation.__init__(self, second, first, '-', result)
    def calculate(self):
        return self.first - self.second

class Addition(Operation):
    """ Contains a substraction itself """
    def __init__(self, first, second, result):
        order = random.randint(0,1)
        if order:
            Operation.__init__(self, first, second, '+', result)
        else:
            Operation.__init__(self, second, first, '+', result)
    def calculate(self):
        return self.first + self.second


class Times(Operation):
    def __init__(self, first, second, result):
        Operation.__init__(self, first, second, ':', result)
    def calculate(self):
        return 0
    def operation(self):
       identifier='"canvas'+str(self.first)+str(self.second)+'"'
       return '<canvas id=' + identifier + ' width="300" height="300"</canvas>\n' +  \
           '<script>drawClock(' + identifier + ', 200, 300, 300, ' + str(self.first) + ', ' \
               + str(self.second) + ')</script>'
       # TODO: allow digital times
       #return str(self.first) + ' : ' + str(self.second) + '='
