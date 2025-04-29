Lista = [98,140,81,102,15] 
print (Lista)

num = int(input("Ingrese un numero:  "))
if num in Lista :
    posicion = Lista.index(num)
    print ("EL numero esta en la pocision" , posicion)
    print ("el numero esta en la lista")
    
else:
    print ("el numero no esta en la lista")
