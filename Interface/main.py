import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *

from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()


    sys.exit(app.exec_())