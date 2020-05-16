import random

from generator import *


def createOperations(args):
    config = MultiConfig()
    config.defaultConfig()
    if args.output:
        config.fileName = args.output
    else:
        config.fileName = "restest.html"
    generate(config)


def runApp(args):
    createOperations(args)
