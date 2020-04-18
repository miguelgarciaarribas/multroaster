import random

from multiconfig import Addition, MultiConfig, Multiplication, Substraction, Times
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
        multiplications.add(Multiplication(table, multiplicant, config.resolve))
    if config.includeTimeTables:
        for mult in range(0, int(maxCount /2)):
            table = config.timetables[random.randint(0, len(config.timetables)-1)]
            multiplicant = random.randint(0,12)
            multiplications.add(Multiplication(table, multiplicant, config.resolve))
    return multiplications

def generateSubstractions(config):
    maxCount = getMaxCount(config)
    substractions = set()
    if not config.includeSubstractions:
        return substractions

    for i in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        substractions.add(Substraction(first,second, config.resolve))
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
        additions.add(Addition(first,second,  config.resolve))
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
        times.add(Times(first,second, config.resolve))
    return times

def generate(config):
    multiplications =  generateMultiplications(config)
    substractions = generateSubstractions(config)
    additions = generateAdditions(config)
    times = generateTimes(config)
    result = list(multiplications) + list( substractions) + list(additions) + list(times)
    random.shuffle(result)

    printer = MultiPrinter()
    result = printer.print(config, result)
    print(result)
    with open(config.fileName, "w") as f:
        f.write(result)
