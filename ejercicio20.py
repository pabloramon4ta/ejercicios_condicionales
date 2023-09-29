#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
valor1=int(input("introduce el primer valor entre el 1 i el 10: "))
valor2=int(input("introduce el segundo valor entre el 1 i el 10: "))
if valor1>10 or valor2>10:
    print("uno de los números esta fuera de los límites establecidos")
else:
    if valor1>valor2:
        print("el número",valor1,"es mayor que el número",valor2)
    if valor1<valor2:
        print("el número",valor2,"es mayor que el número",valor1)
    if valor1==valor2:
        print("el número",valor1,"es igual al número",valor2)

