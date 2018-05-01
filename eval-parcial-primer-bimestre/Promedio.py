#Ingrear por teclado 4 calificaciones
#Calcular el promedio
#Presentar su promedio y calificacion
print("\nSISTEMA DE CALIFICACIONES\n")
nota1=float(input("\tCalificacion 1: "))
nota2=float(input("\tCalificacion 2: "))
nota3=float(input("\tCalificacion 3: "))
nota4=float(input("\tCalificacion 4: "))
promedio=(nota1+nota2+nota3+nota4)/4
if(promedio>=90 and promedio<=100):
	print("\nEl estudiante con promedio %.2f tiene una puntuacion de A"%promedio)
else:
	if(promedio>=80 and promedio<90):
		print("\nEl estudiante con promedio %.2f tiene una puntuacion de B"%promedio)
	else:
		if(promedio>=79 and promedio<80):
			print("\nEl estudiante con promedio %.2f tiene una puntuacion de C"%promedio)
		else:
			print("\nEl estudiante con promedio %.2f tiene una puntuacion de D"%promedio)


