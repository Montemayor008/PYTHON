print ("Ingrese número límite")
limite = int(input())
primero = 0
segundo = 1  
  
while primero <= limite:  
    print(primero)
    ultimo = segundo + primero
    primero = segundo
    segundo = ultimo
    
