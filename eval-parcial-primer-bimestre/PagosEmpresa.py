#Ingresar por teclado la cantidad de ventas de un empleado.
#Calcular el sueldo total y presentarlo.
sueldo_fijo = 360.40
porcentaje1 = 0.5
porcentaje2 = 0.8
porcentaje3 = 0.10
porcentaje4 = 0.15
ventas = float(input("\nIngrese la cantidad de ventas: "))
if (ventas <= 500):
	subtotal = ventas * porcentaje1
	total = subtotal + sueldo_fijo
	print("\nSueldo total: %.2f"%total)
elif (ventas > 500 and ventas <= 1000):
	subtotal = ventas * porcentaje2
	total = subtotal + sueldo_fijo
	print("\nSueldo total: %.2f"%total)
elif (ventas > 1000 and ventas <= 5000):
	subtotal = ventas * porcentaje3
	total = subtotal + sueldo_fijo
	print("\nSueldo total: %.2f"%total)
elif (ventas > 5000):
	subtotal = ventas * porcentaje4
	total = subtotal + sueldo_fijo
	print("\nSueldo total: %.2f"%total)