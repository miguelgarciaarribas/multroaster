## multroaster app: Generates an operation roaster for kids to practice

I find myself constantly writing operations for my 7 year old to resolve, at some point I got tired of doing it by hand. This is a toy project meant to learn some basic pyqt and web technologies while at the same time saving myself some time to write operations by hand.

In order to run the command line version just do "python3 main.py" from the source directory it will generate an html file (res.txt) ready to print. It's super basic right now but I will be improving it in the future.
It currently supports the following operations:


* Early years (3-4 years)
  * Fill in Spirals
  * Fill in dotted letters

* Primary level (6-8 years)
  *  Multiplications (one digit)
  *  Additions (up to 3 digits, two numbers)
  *  Subtractions (up to 3 digits, two numbers)
  *  Times (in analog format clock).

The command line version will generate all operations. There is also a  pyqt based UI that allows you to configure the final operation roaster without modifying the config file manually. In order to run it:

> * create a virtual environment: python3 -m venv venv
>* activate it: source venv/bin/activate (on mac)
>* install pyt: pip install PyQt5
>* cd ui/
>* pyuic5 -x multui.ui -o mult_ui.py # note that mult_ui.py is included in the source so only do this >if you change the ui
>* cd ..
>* python3 main_ui.py
