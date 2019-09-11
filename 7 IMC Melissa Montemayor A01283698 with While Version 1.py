xSi = "Si"
xNo = "No"
answerWritten = "Si"
while answerWritten == xSi:

    print ("Hola soy tu calculadora de IMC")

    nombre = input("Cual es tu nombre: ")

    edad = int(input("Teclea tu edad en años porfavor: "))

    altura = float(input("Ingresa tu altura en metros por favor: "))

    masa = float (input("Ingrese su masa en kilogramos por favor :"))

    IMC = masa / altura**2

    print ("Tu IMC es de: " + str(IMC))

    if (IMC < 19):
        print ("Estás en bajo peso")
    elif (IMC < 25):
        print ("Estás en peso saludable")
    elif (IMC < 30 ):
        print ("Tienes un ligero sobrepeso")
    elif (IMC < 35 ):
        print ("Debes cuidar tu salud, es muy recomendado que solicite ayuda de un nutriólogo")
    else:
        print ("Tu salud está en alto riesgo, es muy recomendado que solicite ayuda de un nutriólogo")
        
    if (edad < 13):
        print ("Además, a niños pequeños se les recomienda que se ejerciten durante 1 hora para mantener su salúd.")
    elif (edad < 18):
        print ("Además, se recomienda que te ejercites durante 1 hora para mantener tu salúd. Una recomendación sería involucrarse en un deporte escolar.")
    elif (edad < 25):
        print ("Además, es el momento perfecto para comenzar a ejercitarte y hacer un hábito para que sea más facil tener buena salúd y mantenerla.")
    elif (edad < 35):
        print ("Además, es muy recomendado que incluya algún ejercicio o entrenamiento como parte de su rutina, de esa manera será más facil mantener masa muscular.")
    elif (edad < 45):
        print ("Gracias a la edad, su cuerpo naturalmente comienza a perder músculo, es importante que se ejercite y le ayude a su cuerpo a mantener la salúd.")
    else:
        print ("Este es un buen momento para enfocarse en el fortalecimiento óseo. Asegúrese de que realice actividades que soporten y ayuden a mantener la salúd y el bienestar.")
    
    print ("Deseas continuar calculando tu IMC?" + " Si deseas continuar escribe -1- , si deseas terminar escribe -2- ")
    
    answerWritten = input()
    
print("Gracias! Vuelve pronto")

#if (edad < 18):
# print("Consulta a un esecialista, eres menor de edad")
#else:
# print (" Bien por ti, cuidas tu salud, eres mayor de edad")