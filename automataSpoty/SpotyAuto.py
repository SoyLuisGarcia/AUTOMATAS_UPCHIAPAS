from PyQt5  import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
import sys

#Clses
class ACTION(QMainWindow):
    #funtions
    def __init__(self):
        super().__init__()
        uic.loadUi("VistaSpoty.ui" , self)
        self.PAUSE.hide() #ocultar picture
        self.ACTION.clicked.connect(self.fn_On)
        self.LF.clicked.connect(self.fn_LF)
        #self.RG.clicked.connect(self.fn_RG)
        
    def fn_LF(self):
        Acti1 = self.LF.text()

        if Acti1 == "LF":
            self.LANA.hide()
            self.SQ.show()
            #self.RG.setText("ENCENDER")
        #Acti2 = self.RG.text()
        elif Acti1 == "RG":
            self.LANA.show()
            self.SQ.hide()
            #self.LF.setText("ENCENDER")

    def fn_On(self):
        # self.CONCA.hide()     #HIDE OCULTAR/ SHOW() MOSTRAR
        #self.ENCENDIDO.setText("APAGAR")    #Cabiar nombre}
        #self.ENCENDIDO.text()               #Extraer nombre
        Acti = self.ACTION.text()
        #Encendido
        if Acti == "ACTION":
            self.PLAY2.hide()
            self.PAUSE.show()

            self.ACTION.setText("APAGAR")

        elif Acti == "APAGAR":
            self.PAUSE.hide()
            self.PLAY2.show()
            
            self.ACTION.setText("ENCENDER")
        

     
    

        
      

#main
if __name__ == '__main__':
    Datt = QApplication (sys.argv)
    GUI = ACTION()
    GUI.show()
    sys.exit(Datt.exec_())