from PyQt6.QtWidgets import (QWidget,QLabel,QMessageBox)
from PyQt6.QtGui import QPixmap #para mostrar subir imagenes
#el q label tambien puede mostrar imagnes



class main(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUi() 

    def inicializarUi(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Main view")
        self.generarcontenido()

    def generarcontenido(self):
        imagePath = "setting.png" #ingresar una imagen
        try: #es suseptible a errores
            with open(imagePath): #la abro en un contage manage / verifica si la imagen existe
                imageLabel = QLabel(self)
                imageLabel.setPixmap(QPixmap(imagePath)) #agregar al label un objeto PixMap ( imagen)
            

        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error","Contenido del login no encontrado: {e}",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
            
        except Exception as e:
                        QMessageBox.warning(self,"Error","Error en el mainView: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close) 
        

