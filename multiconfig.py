from operation import OperationType

class MultiConfig:
    """
    Contains the configuraation to decide how the multiplication should be generated.
    """
    def __init__(self):
        self.studentName = "Bruno"

        # Tables allowed
        self.timetables = []

        # Main variants
        self.operations = {}

        self.resetConfig()

        # output file
        self.fileName = "res.html"

    def resetConfig(self):
        # Tables allowed
        self.timetables = []

        # Main variants
        self.operations = {}
        for operation in OperationType:
            self.operations[operation] = 0

        # Sub variants
        self.includeTimeTables = False
        self.addFourDigits = False
        self.deltaToTimes = False
        self.digitalTime = False
        self.includeDottedLetters = False
        self.includeDottedNumbers = False


    def defaultConfig(self):
        self.timetables = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        for operation in OperationType:
            self.operations[operation] = 5
        self.includeTimeTables =  True
        self.addFourDigits = True
        self.deltaToTimes = True
        self.digitalTime = True
        self.includeDottedLetters = True
        self.includeNumbers = True
