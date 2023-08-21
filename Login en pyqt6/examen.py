import sys
from PyQt6.QtWidgets import (QWidget, QApplication)

class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUi()

    def inicializarUi(self):
        self.setGeometry(200,200,200,200)
        self.setWindowTitle("ventana")
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanas=ventana()
    sys.exit(app.exec())

        