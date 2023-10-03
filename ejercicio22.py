#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("introduce la nota de tu examen: "))
if nota<0 or nota>10:
    print("la nota que has introducido no esta entre el 1 y el 10")
else:
    if nota<5:
        print("has sacado un",nota,"y has suspendido")
    if nota>=5:
        print(" has sacado un",nota,"y has aprobado")
