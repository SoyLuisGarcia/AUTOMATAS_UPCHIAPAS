from PyQt5  import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
import sys

#Clses
class Encendido(QMainWindow):
    #funtions
    def __init__(self):
        super().__init__()
        uic.loadUi("Imagen.ui" , self)
        self.CONCA.hide() #ocultar picture
        self.ENCENDIDO.clicked.connect(self.fn_On)
        

    def fn_On(self):
        # self.CONCA.hide()     #HIDE OCULTAR/ SHOW() MOSTRAR
        #self.ENCENDIDO.setText("APAGAR")    #Cabiar nombre}
        #self.ENCENDIDO.text()               #Extraer nombre
        Acti = self.ENCENDIDO.text()
       
        #Encendido
        
        if Acti == "ENCENDIDO":
            self.CONCA2.hide()
            self.CONCA.show()
            self.ENCENDIDO.setText("APAGAR")
        elif Acti == "APAGAR":
            self.CONCA2.show()
            self.CONCA.hide()
            self.ENCENDIDO.setText("ENCENDER")
        #else: 
            
      

#main
if __name__ == '__main__':
    Datt = QApplication (sys.argv)
    GUI = Encendido()
    GUI.show()
    sys.exit(Datt.exec_())