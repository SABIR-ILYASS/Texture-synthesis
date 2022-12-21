
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Synthèse de textures en imagerie ultrason")
        self.setGeometry(0, 0, 1500, 900)
        self.setWindowIcon(QIcon("images/icon.png"))

        self.centralWidget = QWidget(self)
        self.centralWidget.setGeometry(0, 0, 1500, 900)

        self.centralWidget.setStyleSheet("""background-image: url(images/background.jpg);
                            background-size: cover;
                            background-repeat: no-repeat;
                           """)

        self.setCentralWidget(self.centralWidget)


        # creating a label widget for TSE logo
        self.label1 = QLabel(self)
        pixmap = QPixmap('images/logoTSE.svg')
        self.label1.setPixmap(pixmap)
        self.label1.setGeometry(550, 10, 400, 100)

        # creating a label widget for app title
        self.label2 = QLabel(self)
        self.label2.setText('Synthèse de textures en imagerie ultrason')
        self.label2.setStyleSheet("""color: rgb(60, 84, 223);
                                    font: 14pt "MS Shell Dlg 2";
                                    font: bold;
                                    text-align:center;
                                    font-size: 50px;
                                    """)
        self.label2.setGeometry(170, 120, 1200, 100)

        self.labelImage = QLabel(self)



        self.buttonW = QWidget(self)
        self.labelText = QLabel(self)

        self.btn1 = QPushButton("&Méthode 1", self.buttonW)
        self.btn2 = QPushButton("&Méthode 2", self.buttonW)
        self.btn3 = QPushButton("&Méthode 3", self.buttonW)
        self.btn4 = QPushButton("&Méthode 4", self.buttonW)


        def importingImage(event):
            self.imagePath = QFileDialog.getOpenFileName(self, "Select Image File")[0]
            self.widgetInputImage.hide()
            self.imageWidget(self.imagePath)

            print(self.imagePath)

            self.buttonWidget(self.imagePath)


        # creating a widget for button input image
        self.widgetInputImage = QWidget(self)
        self.widgetInputImage.setGeometry(350, 450, 700, 150)

        self.btnInput = QPushButton("&Entrez l'image", self.widgetInputImage)
        self.btnInput.setStyleSheet("background-color : rgb(60, 84, 223); font-size: 40px; border-radius: 20px;")
        self.btnInput.setGeometry(0, 0, 700, 150)
        self.btnInput.mousePressEvent = importingImage

    def imageWidget(self, url):
        self.pixmap = QPixmap(url)
        self.labelImage.setPixmap(self.pixmap)
        self.labelImage.setGeometry(25, 220, 640, 640)

    def buttonWidget(self, url):

        self.labelText.setGeometry(810, 350, 640, 50)
        self.labelText.setText('Choisissez la méthode de synthèse')
        self.labelText.setStyleSheet("color: rgb(55, 128, 152); font-size: 30px; ")

        def func1(event):
            print(1)

        def func2(event):
            print(2)

        def func3(event):
            print(3)

        def func4(event):
            print(4)

        self.buttonW.setGeometry(725, 290, 640, 400)


        self.btn1.setStyleSheet("background-color : rgb(60, 84, 223); color: white; font-size: 20px; border-radius: 20px;")
        self.btn1.setGeometry(270, 150, 100, 50)
        self.btn1.mousePressEvent = func1

        self.btn2.setStyleSheet("background-color : rgb(60, 84, 223); color: white; font-size: 20px; border-radius: 20px;")
        self.btn2.setGeometry(30, 250, 100, 50)
        self.btn2.mousePressEvent = func2

        self.btn3.setStyleSheet("background-color : rgb(60, 84, 223); color: white; font-size: 20px; border-radius: 20px;")
        self.btn3.setGeometry(510, 250, 100, 50)
        self.btn3.mousePressEvent = func3

        self.btn4.setStyleSheet("background-color : rgb(60, 84, 223); color: white; font-size: 20px; border-radius: 20px;")
        self.btn4.setGeometry(270, 350, 100, 50)
        self.btn4.mousePressEvent = func4
