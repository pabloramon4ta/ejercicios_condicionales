#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
valor1=int(input("introduce el peimer valor: "))
valor2=int(input("introduce el segundo valor: "))
if(valor1<valor2):
    print("el número",valor2,"es mayor que el número",valor1)
if(valor1>valor2):
    print("el número",valor1,"es mayor que el número",valor2)
if(valor1==valor2):
    print("el número",valor1,"es igual al número",valor2)
    