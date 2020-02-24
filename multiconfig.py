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
        self.maxcount = 0


class Multiplication:
    """ Contains a multiplication itself """
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __str__(self):
        return "%s x %s = " % (self.first,  self.second)
