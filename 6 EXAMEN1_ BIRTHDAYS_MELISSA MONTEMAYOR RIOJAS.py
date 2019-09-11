print ("Hola")

ano = int(input("Teclea tu año de nacimiento"))
mes = int(input("Teclea tu mes de cumpleaños"))
dia = int(input("Teclea tu día de cumpleaños"))


if (mes == (1 or 3 or 5 or 7 or 8 or 10 or 12) and (dia >0 and dia <=31)):
    print ("VALIDO")
elif (mes == (4 or 6 or 9 or 11)) and  (dia >0 and dia <31):
    print ("VALIDO")
elif (mes == 2 and (dia >0 and dia <28)):
    print ("VALIDO")
elif ((ano%4 == 0) and (mes == 2) and (dia >0 and dia <30)):
    print ("VALIDO")
    
    

else:
    print ("INVALIDO")

# if (ano%4 == 0 and (mes == (1 or 3 or 5 or 7 or 8 or 10 or 12) and (dia >0 and dia <=31)) 

##if (ano%4 == 0):
 ##       print ("Este es un año bisiesto")
##else:
  ##  print ("ano no biesto")
# print(ano%4)
#if (dia >0 and dia <31):    #para meses de 30 dias
 #   print ("valido")
#else:
 #   print ("invakido")

#if (dia >0 and dia <=31):    #para meses de 31 dias
 #   print ("valido")
#else:
 #   print ("invakido")



    


print("Gracias")


#print("Bienvenido")
#ano = input("Teclea tu año de nacimiento")

#mes = int(input("Teclea mes de cumpleaños (numerico)"))

#dia = input("Teclea tu dia de nacimiento"))

   

