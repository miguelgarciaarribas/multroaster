import random

from generator import *


def createOperations(args):
    config = MultiConfig()
    config.defaultConfig()
    if args.output:
        config.fileName = args.output
    else:
        config.fileName = 'restest.html'

    if args.filter == 'primary':
        config.filterBy = [Category.Primary]
    elif args.filter == 'earlyYears':
        config.filterBy = [Category.EarlyYears]


    generate(config)


def runApp(args):
    createOperations(args)
