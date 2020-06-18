from PyQt5.QtGui import QImage, QPixmap # review

class ExperimentalContent():
    def __init__(self, mainWindow):
        print("Loading Experimental content")
        self.mainWindow = mainWindow
        self.mainWindow.expLabel.setText("hello world")
