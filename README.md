## multroaster app: Generates an operation roaster for kids to practice

I find myself constantly writing operations for my 7 year old to resolve, at some point I got tired of doing it by hand. This is a toy project meant to learn some basic pyqt and web technologies while at the same time saving myself some time to write operations by hand.

It currently supports the following operations:


* Early years (3-4 years)
  * Fill in Spirals
  * Fill in dotted letters
  * Simple additions with animals and numbers
  * Pre-Writting exercises in a grid
  * Solve Mazes


* Primary level (6-8 years)
  *  Multiplications (one digit)
  *  Divisions (one digit)
  *  Additions (up to 4 digits, two numbers)
  *  Subtractions (up to 3 digits, two numbers)
  *  Times (in analog and digital format clock).

Running the program with no arguments will spawn a pyqt based UI that allows you to configure the final operation roaster without modifying the config file manually. In order to run it:

> * create a virtual environment: python3 -m venv venv
>* activate it: source venv/bin/activate (on mac)
>* install pyt: pip install PyQt5
>* install PyQtWebEngine: pip install PyQtWebEngine
>* cd ui/
>* pyuic5 -x multui.ui -o mult_ui.py # note that mult_ui.py is included in the source so only do this >if you change the ui
>* cd ..
>* python3 hojitas.py

Use "python3 hojitas.py -h" for more options, including running a cli version that spawns all possible operations.

There are also some unittest for non trivial operations, to run them do:
> python3 -m unittest discover ./ '*_unittest.py'
