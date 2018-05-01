#Programa que permite ingresar por teclado la longitud y ancho de una habitacion y calcular la superficie de la misma.
longitud=float(input("\nIngrese la longitud de la habitacion: "))
ancho=float(input("Ingrese el ancho de la habitacion: "))
superficie = longitud * ancho
print("Superfie: %.3f" %superficie)