from Ui_MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def onBtn1Clicked(self):
        print("onBtn1Clicked")