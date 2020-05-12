import random

from multiconfig import MultiConfig
from operation import Addition, DigitalTime, EmojiAddition, Grid, Letters, Spiral, Multiplication, OperationType, Substraction, Time
from multiprinter import MultiPrinter


def generateMultiplications(config):
    """ Generates a third raw time tables as well as general multiplications if configured"""
    maxCount = config.operations[OperationType.Multiplication]
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
    maxCount = config.operations[OperationType.Substraction]
    substractions = set()

    for i in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        substractions.add(Substraction(first,second))
    return substractions

def generateAdditions(config):
    maxCount = config.operations[OperationType.Addition]
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
    #TODO add unittest for this similar to generateLetters
    maxCount = config.operations[OperationType.Time]
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
        times.add(Time(first, second, delta, direction))

    return times

def generateLetters(config):
    maxCount = config.operations[OperationType.DottedLetter]
    letters = set()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnopqrstvwxyz'
    digits = '0123456789'
    cases = ['smallpair', 'capitalpair']
    if config.includeDottedNumbers:
        cases.append('numberpair')
    if not config.includeDottedLetters and config.includeDottedNumbers:
        cases = ['numberpair']

    for i in range(0, maxCount):
        case = random.choice(cases)
        combo1 = '-'
        combo2 = '-'
        if case == 'smallpair' or case == 'capitalpair':
            combo1 = consonants[random.randint(0, len(vowels) -1)]
            combo2 = vowels[random.randint(0, len(vowels) -1)]
            if case == 'capitalpair':
                combo1 = combo1.capitalize()
                combo2 = combo2.capitalize()
        elif case == 'numberpair':
            combo1 = digits[random.randint(0, len(digits) -1)]
            combo2 = digits[random.randint(0, len(digits) -1)]

        letters.add(Letters(combo1, combo2))

    return letters

def generateSpirals(config):
    maxCount = config.operations[OperationType.Spiral]
    spirals  = set()

    for i in range(0, maxCount):
        iterations = random.randint(140, 210)
        spirals.add(Spiral(iterations))
    return spirals

def generateEmojiAdditions(config):
    maxCount = config.operations[OperationType.EmojiAddition]
    emojis = set()

    maxNumber = 9
    minNumber = 1

    for i in range(0, maxCount):
        first = random.randint(minNumber, maxNumber)
        second = random.randint(minNumber, maxNumber)
        emojis.add(EmojiAddition(first,second))
    return emojis

def generateGridWrites(config):
    maxCount = config.operations[OperationType.GridWrite]
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
    multiplications =  generateMultiplications(config)
    substractions = generateSubstractions(config)
    additions = generateAdditions(config)
    times = generateTimes(config)
    letters = generateLetters(config)
    spirals = generateSpirals(config)
    emojis = generateEmojiAdditions(config)
    grids = generateGridWrites(config)
    result = list(multiplications) + list( substractions) + list(additions) + \
             list(times) + list(letters) + list(spirals) + list(emojis) + list(grids)
    random.shuffle(result)

    printer = MultiPrinter()
    result = printer.print(config, result)
    with open(config.fileName, "w") as f:
        f.write(result)
