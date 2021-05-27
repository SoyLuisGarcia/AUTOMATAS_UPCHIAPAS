x = input ("ingrese la cadena inicial: ")
count = 0
tamano = len(x)
if x[count] == '0' and x [count + 1] =='0':
    for i in range(len(x)):
        x[i] = "0" 
        print ("hola")
        print("primero ceros pares")
elif x[count] == '1' and x[count + 1]== '1':
    print ("primeros unos pares")
else:

    print("se encontro espacio")