from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
import sys

#palabra input

class ACTION(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Buscador.ui",self)
        self.Verificar.clicked.connect(self.palabra)

    def palabra(self):
        self.ENVIAR1.clear()
        palabra1 =  self.Sintaxis.text() #TRAER TEXTO
        x = palabra1.split()
        count =0
        if x[count]=='int' or x[count]=='byte' or x[count]=='short' :
            print(x[count])
            count =count+1
            cadena1 =x[count]
            if cadena1.isalnum():
                print(cadena1)
                count =count+1
                if x[count] =='[':
                    count =count+1
                    print("se encontro corchete")
                    number = x[count]
                    cadena = x[count]
                    if number.isdigit():
                        count = count+1
                        print("se encontro enteros")
                        if x[count]==']':
                            count = count+1
                            if x[count]==';':
                              self.ENVIAR1.addItem("completo")
                            else:
                                print("no se encontro ';' ")
                                    
                        else:
                            print("no se encontro corchete")                 
                    elif cadena.isalnum():
                        count = count+1
                        print("se encontro  cadena")
                        if x[count]==']':
                            count = count+1
                            if x[count]==';':
                                print("sintaxis Completa")
                        else:
                            print("no se encontro corchete")
                    elif x[count]==']':
                        count= count+1
                        if x[count]==';':
                            print("completa Si")
                        else:
                            print("no completa")        
        else:
            self.ENVIAR1.addItem("error")


if __name__ == '__main__':
    Datt = QApplication (sys.argv)
    GUI = ACTION()
    GUI.show()
    sys.exit(Datt.exec_())