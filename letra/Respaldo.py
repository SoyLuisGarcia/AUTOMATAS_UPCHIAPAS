rint("Acepta tipo dato int chart byte    ejemplo int 3;")  #/int char byte
x= input("palabra: ")

#Validacion de palabra 
if x[0]=='i':
    if x[1] == 'n':
        if x[2] == 't':
             print(f"ingreso una palabra reservada: ",x)
             for i in range(len(x)):
                print(x[i])
        else :
            print("ingreso mal la palabra reservada")
    else : 
        print("ingreso mal palbra reservada")
elif x[0] == 's':
    if x[1]== 'h':
        if x[2]=='o':
            if x[3]=='r':
                if x[4]=='t':
                    
                    print(f"ingreso una palabra reservada: ",x)
                    
                else:
                     print("ingreso mal la palabra reservada")
            else:
                print("ingreso mal la palabra reservada")
        else:
            print("ingreso mal la palabra reservada")
    else:
        print("ingreso mal la palabra reservada")
elif x[0]=='b':
    if x[1]== 'y':
        if x[2]=='t':
            if x[3]=='e':
                print(f"ingreso una palabra reservada: ",x)
            else:
                print("ingreso mal la palabra reservada")
        else:
            print("ingreso mal la palabra reservada")
    else:
        print("ingreso mal la palabra reservada")
else:
    print("ingrese porfavor una pabara Reservada")*/
    
    
    
    palabra= input("palabra: ")
x = palabra.split()
count =0
if x[count]=='int' or x[count]=='byte' or x[count]=='short' :
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
                        print("sintaxis Completa")
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
                if x[count]==';':-
                    print("completa Si")
                else:
                    print("no completa")        
else:
    print("sintaxis Incorrecta")
    