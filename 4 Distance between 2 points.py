from math import sqrt
def distanciaEntrePuntos(x1,y1,x2,y2):
    d = sqrt(( (x2-x1) ** 2) + ((y2-y1) ** 2))
    return (d)

Px1 = float(input("Escribe el valor de X1: "))
Py1 = float(input("Escribe el valor de Y1: "))


Px2 = float(input("Escribe el valor de X2: "))
Py2 = float(input("Escribe el valor de Y2: "))


a = distanciaEntrePuntos(Px1,Py1,Px2,Py2)
print("La distancia entre P1 y P2 es: " + str(a))
print(" ")

#pedirle al usuario 3 puntos diferentes y determinar si se forma un triangulo equilatero, isoceles o escaleno
#if iguales las distancias, es equilatero
#if 2 distancias iguales = isoceles
#if las 3 diferentes = escaleno
#tarea entrega miercoles a la media noche
