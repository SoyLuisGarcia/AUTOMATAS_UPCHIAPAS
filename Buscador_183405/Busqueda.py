from PyQt5  import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
import sys

Persona = {'abstract': 
"Un método sin definición debe declararse como \n abstracto y la clase que lo \n contiene debe declararse como abstracto.\n Las clases abstractas no pueden ser instanciadas."
,
'assert':
"Assert describe un predicado (una declaración de \n verdadero / falso) colocado en un programa Java para \n indicar que el desarrollador piensa que el predicado \n siempre es verdadero en ese lugar."
,
'boolean':
"Define una variable booleana para los valores true \n o false solamente. Por defecto, el valor del tipo \n primitivo booleano es falso."
}

#print(Persona)
#print(Persona['Nombre'])


#Clases
class ACTION(QMainWindow):
    #funtions
    def __init__(self):
        super().__init__()
        uic.loadUi("Buscador.ui" , self)
        self.BUSCAR.clicked.connect(self.palabra)
        
    
    def palabra(self):
        self.ENVIAR1.clear()
        buscar =  self.AGREGAR.text() #TRAER TEXTO
        Agregar = Persona.get (buscar,"No se encontro resultados")
        self.ENVIAR1.addItem(Agregar)
        
        

            

#main
if __name__ == '__main__':
    Datt = QApplication (sys.argv)
    GUI = ACTION()
    GUI.show()
    sys.exit(Datt.exec_())