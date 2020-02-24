import random
from multiconfig import MultiConfig, Multiplication
from multiprinter import MultiPrinter


def generateMultiplications(config):
    multiplications = set()
    for mult in range(0, config.maxcount):
        table = config.timetables[random.randint(0, len(config.timetables)-1)]
        multiplicant = random.randint(0, config.maxmult)
        order = random.randint(0,1)
        if order:
            multiplications.add(Multiplication(table, multiplicant))
        else:
            multiplications.add(Multiplication(multiplicant, table))
    return multiplications

def main():
    config = MultiConfig()
    config.timetables = [1, 2, 3, 4, 5, 10, 11]
    config.maxcount = 10

    mult =  generateMultiplications(config);
    printer = MultiPrinter(mult)
    result = printer.generate() 
    print(result)
    with open("res.html", "w") as f:
        f.write(result)

if __name__== "__main__":
  main()
