import random

from multiconfig import MultiConfig
from operation import Addition, EmojiAddition, Grid, Letters, Spiral, Multiplication, Substraction, Time
from multiprinter import MultiPrinter

def getMaxCount(config):
    operations = 0
    if config.includeMultiplications:
        operations +=1
    if config.includeAdditions:
        operations +=1
    if config.includeSubstractions:
        operations +=1
    if config.includeTimes:
        operations +=1
    if config.includeLetters:
        operations +=1
    if config.includeSpirals:
        operations +=1
    if config.includeEmojiAdditions:
        operations +=1
    if config.includeGrids:
        operations +=2 # Grids use two spaces

    if operations > 0:
        return int(config.maxCount / operations)
    raise "Operations cannot be 0"

def generateMultiplications(config):
    """ Generates a third raw time tables as well as general multiplications if configured"""
    maxCount = getMaxCount(config)
    multiplications = set()
    if not config.includeMultiplications:
        return multiplications
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
    maxCount = getMaxCount(config)
    substractions = set()
    if not config.includeSubstractions:
        return substractions

    for i in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        substractions.add(Substraction(first,second))
    return substractions

def generateAdditions(config):
    maxCount = getMaxCount(config)
    additions = set()
    if not config.includeAdditions:
        return additions

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
    maxCount = getMaxCount(config)
    times = set()
    if not config.includeTimes:
        return times
    minutes = range(0, 60, 5)
    for i in range(0, maxCount):
        first = random.randint(1, 12) # TODO add 24h support
        second = random.choice(minutes)
        deltas = range(0, 55, 5)
        delta = random.choice(deltas)
        direction = random.choice(('+', '-', None))
        times.add(Time(first, second, delta, direction))

    return times

def generateLetters(config):
    maxCount = getMaxCount(config)
    letters = set()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnopqrstvwxyz'
    digits = '0123456789'
    cases = ['smallpair', 'capitalpair', 'numberpair']

    if not config.includeLetters:
        return letters
    for i in range(0, maxCount):
        case = random.choice(cases)
        if case == 'smallpair' or case == 'capitalpair':
            combo1 = vowels[random.randint(0, len(vowels) -1)]
            combo2 = consonants[random.randint(0, len(vowels) -1)]
            if case == 'capitalpair':
                combo1.capitalize()
                combo2.capitalize()
        elif case == 'numberpair':
            combo1 = digits[random.randint(0, len(digits) -1)]
            combo2 = digits[random.randint(0, len(digits) -1)]

        order = random.choice((True, False))
        if order:
            letters.add(Letters(combo1, combo2))
        else:
            letters.add(Letters(combo2, combo1))
    return letters

def generateSpirals(config):
    maxCount = getMaxCount(config)
    spirals  = set()
    if not config.includeSpirals:
        return spirals
    for i in range(0, maxCount):
        iterations = random.randint(140, 210)
        spirals.add(Spiral(iterations))
    return spirals

def generateEmojiAdditions(config):
    maxCount = getMaxCount(config)
    emojis = set()
    if not config.includeEmojiAdditions:
        return emojis
    maxNumber = 9
    minNumber = 1

    for i in range(0, maxCount):
        first = random.randint(minNumber, maxNumber)
        second = random.randint(minNumber, maxNumber)
        emojis.add(EmojiAddition(first,second))
    return emojis

def generateGridWrites(config):
    maxCount = getMaxCount(config)
    candidates = ['triangle', 'square']
    current = candidates.copy()
    grids = set()
    if not config.includeGrids:
        return grids
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
