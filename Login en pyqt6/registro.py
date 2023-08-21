
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QDialog,QLabel,  #iba qdialog
                             QPushButton, QLineEdit,
                             QMessageBox, QCheckBox)

from PyQt6.QtGui import QFont

class registroUsuarioView(QDialog):

    def __init__(self, close_callback=[]):
        super().__init__()
        self.setModal(True)#con este comando le digo que si ejecuta la aplicacion y el usuraio quiere interactuar con otra app que lo bloquee
        #literalmente la bloquea
        self.generarFormulario()
        self.close_callback = close_callback
        
    def close(self):
        for callback in self.close_callback:
            callback()
        super().close()

    def generarFormulario(self):
            self.setGeometry(100,100,350,250)
            self.setWindowTitle("registration window")

            #campo de label y de recibir info para el user
            user_label = QLabel(self)
            user_label.setText("usuario: ")
            user_label.move(20,44)
            user_label.setFont(QFont("arial",10))

            self.user_input = QLineEdit(self)
            self.user_input.resize(250,24)
            self.user_input.move(90,40)

            #campo de label y de recibir info para el password
            password1_label = QLabel(self)
            password1_label.setText("password: ")
            password1_label.move(20,74)
            password1_label.setFont(QFont("arial",10))

            self.password1_input = QLineEdit(self)
            self.password1_input.resize(250,24)
            self.password1_input.move(90,70)
            self.password1_input.setEchoMode(
                 QLineEdit.EchoMode.Password
            )

            #para crear un boton de view password
            self.password_view = QCheckBox(self)
            self.password_view.move(20,135)
            self.password_view.setText("view password")
            self.password_view.toggled.connect(self.mostrar)





            #campo de label y de recibir info para rectificar password
            password2_label = QLabel(self)
            password2_label.setText("password: ")
            password2_label.move(20,104)
            password2_label.setFont(QFont("arial",10))

            self.password2_input = QLineEdit(self)
            self.password2_input.resize(250,24)
            self.password2_input.move(90,100)
            self.password2_input.setEchoMode(
                 QLineEdit.EchoMode.Password
            )

            #Crear boton para registrar el user
            registrar_button = QPushButton(self)
            registrar_button.resize(150,32)
            registrar_button.move(20,170)
            registrar_button.setText("Crear")
            registrar_button.clicked.connect(self.crear_usuario)

            #crear boton de cancelar
            cancel_button = QPushButton(self)
            cancel_button.resize(150,32)
            cancel_button.move(170,170)
            cancel_button.setText("Cancelar")
            cancel_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
         self.close()
         
         

    def crear_usuario(self):
         user_path = "usuarios.txt"#creamos un archivo para almacenar
         usuario = self.user_input.text() #de esta froma, con el metodo text, podemos sacar la informacion que esta dentro de user_input()
         usuario = usuario.strip(" ") #para quitar espacion en el login
         password1=self.password1_input.text()
         password2=self.password2_input.text()
         users = list() # lista con usuarios 

         with open(user_path,"r") as f: #context manage - "r" porque solo queremos leer
                   for line in f: #para iterar linea por linea del archivo
                        users.append(line.strip("\n"))#quitamos el salto de linea al final de cada linea
         #Crear una listea de los usarios existentes 

         if password1 == "" or password2=="" or usuario == "":
              QMessageBox.warning(self,"Error","Por favor ingrese datos validos",
                                  QMessageBox.StandardButton.Close,
                                   QMessageBox.StandardButton.Close ) 

              #q message box permite mostrat una caja de texto, existen varios formatos
              # en este caso le damos el wraning (emergencia ) por lo tanto aparecera un icono de mergencia
              # en el segundo campo le damos el titulo al box
              # en el tercer campo le damos el mensaje que queremos que parezca
              # el cuarto campo es el (los) botones con los que podemos interactuar
              # y el ultimo campo son los botones que aparecen por defecto
              #en este caso aparece el boton standar por defecto de cerrar ventana

         elif password1 != password2:
              QMessageBox.warning(self,"Error","Las contraseñas no coinciden",
                                  QMessageBox.StandardButton.Close,
                                   QMessageBox.StandardButton.Close ) 
              
          
         elif f"{usuario},{password1}" in users:
              QMessageBox.warning(self,"error","usuario existenten.\nIntente iniciar sesion.",
                                  QMessageBox.StandardButton.Close,
                                  QMessageBox.StandardButton.Close)
              
         
         
         
         
         else:
              try:
                   with open(user_path,"a+") as f:
                        f.write(f"{usuario},{password1}\n")
                    
                   QMessageBox.information(self,"Creacion exitosa", "Usuario creado correctamente",
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok)
                   
                   self.close()
                   
              except FileNotFoundError as e:
                   QMessageBox.warning(self,f"Error","La base de datos de usuario no existe:{e}",
                                  QMessageBox.StandardButton.Close,
                                   QMessageBox.StandardButton.Close ) 
                   
    def mostrar(self,clicked):
          if clicked:
               self.password1_input.setEchoMode(QLineEdit.EchoMode.Normal)
               self.password2_input.setEchoMode(QLineEdit.EchoMode.Normal)

          else:
               self.password1_input.setEchoMode(QLineEdit.EchoMode.Password)
               self.password2_input.setEchoMode(QLineEdit.EchoMode.Password)


 









                                      
              
                   
                   
                   
                   
          
                   
                   
              
              
         
              

    
            






            
