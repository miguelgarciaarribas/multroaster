import argparse

from PyQt5 import QtCore, QtWidgets

from ui.mult_ui import *
from generator import *
from ui.slider import SliderGroup

import hojitas_cli
import hojitas_qt


def processArguments():
    parser = argparse.ArgumentParser(description=
        'Tool to produce an html file with operations for kids to resolve.\n'
        'Run as a commnad line or a GUI to better configure the operations.')
    parser.add_argument('-c', '--cli', help='Runs the Command line version of the tool.'
                        ' Otherwise the QT version is run',
                        action='store_true')
    parser.add_argument('-o', '--output', help='name of the output file to generate')
    parser.add_argument('-f', '--filter', choices=['primary', 'earlyYears'],
                        help='filter operations by primary or earlyYears')
    args = parser.parse_args()
    return args



if __name__== "__main__":
    args = processArguments()
    if args.cli:
        hojitas_cli.runApp(args)
    else:
        hojitas_qt.runApp(args)
