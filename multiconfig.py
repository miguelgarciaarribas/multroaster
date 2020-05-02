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

        # Main variants
        # TODO: This can be a set of OperationType now.
        self.includeMultiplications = True
        self.includeAdditions = True
        self.includeSubstractions = True
        self.includeTimes = True
        self.includeLetters = True
        self.includeSpirals = True
        self.includeEmojiAdditions = True
        self.includeGrids = True

        # Sub variants
        self.includeTimeTables =  True
        self.addFourDigits = True
        self.addToTimes = True

        # output file
        self.fileName = "res.html"
