import random

class MultiConfig:
    """
    Contains the configuraation to decide how the multiplication should be generated.
    """
    def __init__(self):
        # tables allowed
        self.timetables = []

        # max multiplicator
        self.maxmult = 12
        
        # number of multiplications to generate
        self.maxCount = 0

        # whether to calculate the result
        self.resolve = True

        self.includeMultiplications = True
        self.includeAdditions = True
        self.includeSubstractions = True


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
