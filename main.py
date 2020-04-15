import random

from generator import *


def createOperations():
    config = MultiConfig()
    config.timetables = [1, 2, 3, 4, 5, 8]
    config.maxCount = 24
    config.fileName = "restest.html"
    generate(config)


def main():
    createOperations()

if __name__== "__main__":
  main()
