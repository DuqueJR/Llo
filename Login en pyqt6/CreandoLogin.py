import time
from registro import registroUsuarioView
from MainWindow import main
import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication,
                             QLabel,
                             QWidget,
                             QLineEdit,
                             QPushButton,
                             QMessageBox,
                             QCheckBox,)

from PyQt6.QtGui import (QFont,QPixmap) #el q font permite introducir fuentes
#el qPix Map permite introducir imagenes en nuestra interfaz  
 

class Login(QWidget):
    def __init__(self):
          super().__init__()
          self.inicializar_ui()
    
    def inicializar_ui(self):
         self.setGeometry(100,100,350,250)
         self.setWindowTitle("mi login")
         self.generarformulario()
         self.show()
     
    def generarformulario(self):
         self.is_logged = False #si esta en el login el usuario no esta logeado por eso es false

         user_label = QLabel(self) # crear un objeto de la libreria label
         user_label.setText("usuario: ")#crear el texto que va a tener el label
         user_label.setFont(QFont("arial",10))#generar la fuente que va a tener el label
         user_label.move(20,54)#poner las cordenadas en las que aparecera el label (posicion x, posicion y)
         
         self.user_input = QLineEdit(self) # crear el objeto user input para la entrada de informacion
         #se le pone el self en qline para relacionarlo con la clase y el metodo en cuestion
         self.user_input.resize(250,24)#darle un tamaño a nuesto campo (tamaño en x, tamaño en y)
         self.user_input.move(90,50)
         #al poner self al principio de el user lo declaramos como una variabvle de instacia de modo que podremos acceder a el desde afuera del metodo

         password_label = QLabel(self) # crear un objeto de la libreria label para e pasword (una etiqueta) un texto
         password_label.setText("pasword: ")#crear el texto que va a tener el label (aparece en pantalla)
         password_label.setFont(QFont("arial",10))#generar la fuente que va a tener el label
         password_label .move(20,86)#poner las cordenadas en las que aparecera el label (posicion x, posicion y)

         
         self.password_input = QLineEdit(self) # crear el objeto user input para la entrada de informacion del pasword
         #se le pone el self en qline para relacionarlo con la clase y el metodo en cuestion
         self.password_input.resize(250,24)#darle un tamaño a nuesto campo (tamaño en x, tamaño en y)
         self.password_input.move(90,82) #darke unas cordenadas al pasword    
         self.password_input.setEchoMode(
              QLineEdit.EchoMode.Password #una variable estatica que ofrece el programa para establecer los campo que puede aceptar 
         )  #cambia el texto plano por oculto ( en puntos), es una variable estatica

         self.check_view_password = QCheckBox(self)
         self.check_view_password.setText("ver contraseña")
         self.check_view_password.move(90,110)
         #pongo el self si me interesa el valor que pueda tener la variable de instancia
         self.check_view_password.toggled.connect (self.mostrar_contrasena)


         login_button = QPushButton(self)
         login_button.setText("login") #para establecer texto interno del boton
         login_button.resize(320,34)
         login_button.move(20,140)
         login_button.clicked.connect(self.login) #este es un sygnal
         #al poner clicked definimos la señal con la que queremos interactuar, es un click (cliked)
         #al poner connect lo conectamos con un sloot(un metodo que responde a la funcion)
         #en los parentesis ponemos el metodo (sloot) que va a responder

         register_button = QPushButton(self)
         register_button.setText("registrarse") #para establecer texto interno del boton
         register_button.resize(320,34)
         register_button.move(20,180)
         register_button.clicked.connect(self.registrar_usuario)

    
    def mostrar_contrasena(self,clicked): #clicked para enviar  como argumento si esta chuleado o no
         if clicked:
              self.password_input.setEchoMode(
                   QLineEdit.EchoMode.Normal  #al axeder al echo mode como normal, normalizamos la contraseñña a texto plano
              )
          
         else:
               self.password_input.setEchoMode(
                   QLineEdit.EchoMode.Password  #al axeder al echo mode como password, ponemos la contraseñña en puntos
              )
                             
    def registrar_usuario(self): #si no ponemos el self no es posible para el programa abir otra ventana
         self.hide()
         self.new_user_form = registroUsuarioView(close_callback=[self.mostrarlogin])
         self.new_user_form.show()
    
    def mostrarlogin(self):
          self.show() 
         

               
         
         

         

    

    def login(self):
         users = list() #creo una lista para almacenar los usuarios
         user_path = "usuarios.txt"
         try:
              with open(user_path,"r") as f: #context manage - "r" porque solo queremos leer
                   for line in f: #para iterar linea por linea del archivo
                        users.append(line.strip("\n"))#quitamos el salto de linea al final de cada linea
                    
                   loginInfo = f"{self.user_input.text()},{self.password_input.text()}"#asignamos a la variable la informacion que el usuario puso en el ligin con el formato usuario,password


                   if loginInfo in users:
                        QMessageBox.information(self,"Inicio sesion","Inicio de sesion exitoso",
                                                QMessageBox.StandardButton.Ok,
                                                QMessageBox.StandardButton.Ok) #boton informativo que indique sesiion iniciada exitosamente
                        
                        self.is_logged = True #cambiar el is loged de false a true para indicar el logeo
                        self.close()
                        self.open_main_window()

                   else: #si no se encuentra el usuario en la base de datos
                        QMessageBox.warning(self,"Error","Usario no encontrado",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)


         except FileNotFoundError as e: #si la base de datos no se encuetra
                        QMessageBox.warning(self,"Error",f"Error al cargar la base de datos: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)       

         except Exception as e:
                        QMessageBox.warning(self,"Error","Error en servidor: {e}",
                                        QMessageBox.StandardButton.Close,
                                        QMessageBox.StandardButton.Close)          

    def open_main_window(self): #para abrir la ventana principal despues de haberse logeado   
          self.main_window = main()
          self.main_window.show()
          





                   
                   
              

    

    

          
if __name__=="__main__":
     App = QApplication(sys.argv)# todas las operaciones de nuestra app
     login= Login()
     sys.exit(App.exec())




