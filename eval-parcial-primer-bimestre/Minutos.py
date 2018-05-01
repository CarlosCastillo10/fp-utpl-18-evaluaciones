#Calcular acuantos minutos equivalen los segundos ingresados por teclado
segundos=int(input("ingrese los segundos: "))
segundos_totales=segundos%60
minutos=segundos//60
print("{0} segundos es igual a {1} minutos y {2} segundos".format(segundos,minutos,segundos_totales))
