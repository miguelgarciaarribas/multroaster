# multroaster
Generates an operation roaster for kids to practice

I find myself constantly writting operations for my 7 year old to resolve, at some point I got tired of doing it by hand.

In order to run the command line version just do python3 main.py it will generate a html file (res.txt) ready to print. It's super basic right now but I will be improving it in the future.
It currently supports: Multiplications (one digit), Additions (up to 3 digits, two numbers), Substractions (up to 3 digits, two numbers)

There is an initial attempt of a pyqt version that allows you to configure the final operation roaster without modifying the config file manually. In order to run it:

++create a virtual environment: python3 -m venv venv
++activate it: source venv/bin/activate (on mac)
++install pyt: pip install PyQt5
++cd ui/
++pyuic5 -x multui.ui -o mult_ui.py # note that mult_ui.py is included in the source so only do this if you change the ui
++cd ..
++python3 main_ui.py
