import random

from generator import *


def createOperations():
    config = MultiConfig()
    config.defaultConfig()
    config.fileName = "restest.html"
    generate(config)


def main():
    createOperations()

if __name__== "__main__":
  main()
