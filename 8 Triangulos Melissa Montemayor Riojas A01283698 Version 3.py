from math import sqrt
xP1X1 = float(input("Escriba el valor para X1: "))
xP1Y1 = float(input("Escriba el valor para Y1: "))

xP2X2 = float(input("Escriba el valor para X2: "))
xP2Y2 = float(input("Escriba el valor para Y2: "))

xP3X3 = float(input("Escriba el valor para X3: "))
xP3Y3 = float(input("Escriba el valor para Y3: "))


xDAB = sqrt(  ((xP2X2 - xP1X1)**2) + ((xP2Y2 - xP1Y1)**2)  ) #Distancia entre puntos AB
print(xDAB)

xDBC = sqrt(  ((xP2X2 - xP3X3)**2) + ((xP2Y2 - xP3Y3)**2)  ) #Distancia entre puntos BC
print(xDBC)

xDAC = sqrt(  ((xP1X1 - xP3X3)**2) + ((xP1Y1 - xP3Y3)**2)  ) #Distancia entre puntos AC
print(xDAC)

xDAB = (round(xDAB, 1))
xDBC = (round(xDBC, 1))
xDAC = (round(xDAC, 1))

print(xDAB)
print(xDBC)
print(xDAC)


if (xDAB == xDBC and xDAB == xDAC):
    print("Equilatero")
elif (xDAB == xDBC or xDAB == xDAC or xDBC == xDAC):
    print("Isoceles")
else:
    print("Escaleno")
    

              