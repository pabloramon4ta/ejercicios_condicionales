#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math


a=int(input("introduce el primer valor: "))
b=int(input("introduce el segundo valor: "))
c=int(input("introduce el tercer valor: "))
contenido=(b**2)-4*a*c
if contenido<0:
    print("la raiz no puede ser un valor negativo")
else:
    raiz=math.sqrt(contenido)

  
    eq_positiva=(-b+raiz)/2*a
    eq_negativa=(-b-raiz)/2*a
    print("el valor de x1 es:",eq_positiva)
    print("el valor de x2 es:",eq_negativa)