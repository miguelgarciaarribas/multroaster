import random

from multiconfig import MultiConfig
from operation import Addition, Letters, Spiral, Multiplication, Substraction, Times
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
        times.add(Times(first,second))
    return times

def generateLetters(config):
    maxCount = getMaxCount(config)
    letters = set()
    candidates = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    if not config.includeLetters:
        return letters
    for i in range(0, maxCount):
        combo1 = candidates[random.randint(0, len(candidates) -1)]
        combo2 = candidates[random.randint(0, len(candidates) -1)]
        letters.add(Letters(combo1, combo2))
    return letters

def generateSpirals(config):
    maxCount = 2 #getMaxCount(config)
    spirals  = set()
    if not config.includeSpirals:
        return spirals
    for i in range(0, maxCount):
        iterations = random.randint(140, 210)
        spirals.add(Spiral(iterations))
    return spirals

def generate(config):
    multiplications =  generateMultiplications(config)
    substractions = generateSubstractions(config)
    additions = generateAdditions(config)
    times = generateTimes(config)
    letters = generateLetters(config)
    spirals = generateSpirals(config)
    result = list(multiplications) + list( substractions) + list(additions) + \
             list(times) + list(letters) + list(spirals)
    random.shuffle(result)

    printer = MultiPrinter()
    result = printer.print(config, result)
    print(result)
    with open(config.fileName, "w") as f:
        f.write(result)
