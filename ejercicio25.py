#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("introduce tu nota: "))
if nota<0 or nota>10:
    print("la nota que has introducido no esta entre el 1 i el 10 ")
if nota<5 and nota>=0:
    print("tu nota es un:",nota,"has sacado un insuficiente")
if nota<6.5 and nota>=5:
    print("tu nota es de un:",nota,"has sacado un suficiente")
if nota<8.5 and nota>=6.5: 
    print("tu nota es de un:",nota,"has sacado un notable")
if nota<=10 and nota>=8.5:
    print("tu nota es de un:",nota,"has sacado un excelente")
