import random

from multiconfig import Addition, MultiConfig, Multiplication, Substraction

def getMaxCount(config):
    if config.includeMultiplications and config.includeAdditions and config.includeSubstractions:
        return int(config.maxCount / 3)
    if config.includeMultiplications and config.includeAdditions:
        return int(config.maxCount / 2)
    else:
        return int(config.maxCount)


def generateMultiplications(config):
    maxCount = getMaxCount(config)
    multiplications = set()
    if not config.includeMultiplications:
        return multiplications
    for mult in range(0, maxCount):
        table = config.timetables[random.randint(0, len(config.timetables)-1)]
        multiplicant = random.randint(0, 99)
        multiplications.add(Multiplication(table, multiplicant, config.resolve))

    return multiplications

def generateSubstractions(config):
    maxCount = getMaxCount(config)
    substractions = set()
    if not config.includeSubstractions:
        return substractions
    
    for subs in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        substractions.add(Substraction(first,second, config.resolve))
    return substractions

def generateAdditions(config):
    maxCount = getMaxCount(config)
    additions = set()
    if not config.includeAdditions:
        return additions
    for subs in range(0, maxCount):
        first = random.randint(0, 999)
        second = random.randint(0, 999)
        additions.add(Addition(first,second, config.resolve))
    return additions
            

