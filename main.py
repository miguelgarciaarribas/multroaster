import random

from generator import *
from multiconfig import Addition, MultiConfig, Multiplication, Substraction
from multiprinter import MultiPrinter


def generate():
    config = MultiConfig()
    config.timetables = [1, 2, 3, 4, 5, 8]
    config.maxCount = 24

    multiplications =  generateMultiplications(config)
    substractions = generateSubstractions(config)
    additions = generateAdditions(config)
    times = generateTimes(config)
    result = list(multiplications) + list( substractions) + list(additions)
    random.shuffle(result)

    # Temporarly add all the clocks at the bottom to not break layout
    result += times

    printer = MultiPrinter()
    result = printer.print(result)
    print(result)
    with open("restest.html", "w") as f:
        f.write(result)


def main():
    generate()

if __name__== "__main__":
  main()
