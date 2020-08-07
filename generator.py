import random

from multiconfig import MultiConfig
from operation import Addition,  DigitalTime, Division, EmojiAddition, Grid, Letters, Spiral, Multiplication, OperationType, Substraction, Time
from operationType import Category, OperationType
from multiprinter import MultiPrinter
from operation import Addition, DigitalTime, Division, EmojiAddition, Grid, Letters, Spiral, Multiplication, Substraction, Time

def operationCount(config, operationType):
    if operationType.category in config.filterBy:
        return config.operations[operationType]
    return 0


def generateDivisions(config):
    """ Generates divisions. """
    maxCount = operationCount(config, OperationType.Division)
    divisions = set()
    for mult in range(0, maxCount):
        numerator = random.randint(1, 99)
        denominator = config.timetables[random.randint(0, len(config.timetables)-1)]
        # prevent division by 0
        if denominator == 0:
            denominator = 1
        divisions.add(Division(numerator, denominator))
    return divisions

def generateMultiplications(config):
    """ Generates a third of raw time tables as well as general multiplications if configured"""
    maxCount = operationCount(config, OperationType.Multiplication)
    multiplications = set()
    if config.includeTimeTables:
        maxCount = int(maxCount * 2 / 3)
    for mult in range(0, maxCount):
        table = config.timetables[random.randint(0, len(config.timetables)-1)]
        multiplicant = random.randint(10, 99)
        multiplications.add(Multiplication(table, multiplicant))
    if config.includeTimeTables:
        for mult in range(0, int(maxCount /2)):
            table = config.timetables[random.randint(0, len(config.timetables)-1)]
            multiplicant = random.randint(0,12)
            multiplications.add(Multiplication(table, multiplicant))
    return multiplications

def generateSubstractions(config):
    maxCount = operationCount(config, OperationType.Substraction)
    substractions = set()

    for i in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        substractions.add(Substraction(first,second))
    return substractions

def generateAdditions(config):
    maxCount = operationCount(config, OperationType.Addition)
    additions = set()

    minNumber = 11
    maxNumber = 999
    if config.addFourDigits:
        maxNumber = 9999
        minNumber = 100

    for i in range(0, maxCount):
        first = random.randint(minNumber, maxNumber)
        second = random.randint(minNumber, maxNumber)
        additions.add(Addition(first,second))
    return additions

def generateTimes(config):
    maxCount = operationCount(config, OperationType.Time)
    times = set()

    minutes = range(0, 60, 5)
    for i in range(0, maxCount):
        first = random.randint(1, 12) # TODO add 24h support
        second = random.choice(minutes)
        deltas = range(0, 55, 5)
        delta = 0
        if config.deltaToTimes:
            delta = random.choice(deltas)
        direction = random.choice(('+', '-', None))
        format = random.choice(['digital', 'analog'])
        if config.digitalTime and format == 'digital':
            times.add(DigitalTime(first, second, delta, direction))
        else:
            times.add(Time(first, second, delta, direction))

    return times

def generateLetters(config):
    maxCount = operationCount(config, OperationType.DottedLetter)
    letters = set()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    cases = ['small', 'capital']
    if config.includeDottedNumbers:
        cases.append('number')
    if not config.includeDottedLetters and config.includeDottedNumbers:
        cases = ['number']

    for i in range(0, maxCount):
        case = random.choice(cases)
        choice = ''
        for i in range(0,4):
          combo1 = '-'
          combo2 = '-'
          if case == 'small' or case == 'capital':
              combo1 = random.choice(consonants)
              combo2 = random.choice(vowels)
              if case == 'capital':
                  combo1 = combo1.capitalize()
                  combo2 = combo2.capitalize()
              choice = choice + combo1 + combo2

          elif case == 'number':
              choice += random.choice(digits)
        letters.add(Letters(choice))

    return letters

def generateSpirals(config):
    maxCount = operationCount(config, OperationType.Spiral)
    spirals  = set()

    for i in range(0, maxCount):
        iterations = random.randint(140, 210)
        spirals.add(Spiral(iterations))
    return spirals

def generateEmojiAdditions(config):
    maxCount = operationCount(config, OperationType.EmojiAddition)
    emojis = set()

    maxNumber = 5
    minNumber = 1

    for i in range(0, maxCount):
        first = random.randint(minNumber, maxNumber)
        second = random.randint(minNumber, maxNumber)
        emojis.add(EmojiAddition(first,second))
    return emojis

def generateGridWrites(config):
    maxCount = operationCount(config, OperationType.GridWrite)
    candidates = ['triangle', 'square']
    current = candidates.copy()
    grids = set()

    for i in range(0, maxCount):
        pattern = random.randint(0, len(current) -1)
        grids.add(Grid(current[pattern]))
        del current[pattern]
        if not current:
            current = candidates.copy()

    return grids


def generate(config):
    result = []
    operations = [generateMultiplications,
                  generateDivisions,
                  generateSubstractions,
                  generateAdditions,
                  generateTimes,
                  generateLetters,
                  generateSpirals,
                  generateEmojiAdditions,
                  generateGridWrites]

    for operation in operations:
        result += list(operation(config))

    random.shuffle(result)

    printer = MultiPrinter()
    result = printer.print(config, result)
    with open(config.fileName, "w") as f:
        f.write(result)
