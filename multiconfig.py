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
        self.includeMultiplications = True
        self.includeAdditions = True
        self.includeSubstractions = True
        self.includeTimes = True
        self.includeLetters = True
        self.includeSpirals = True

        # Sub variants
        self.includeTimeTables =  True
        self.addFourDigits = True

        # output file
        self.fileName = "res.html"
