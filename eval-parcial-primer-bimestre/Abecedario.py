#Ingrear por teclado 3 letras
#Presentar cual de las letras ingresadas es la primera que aparece en el abecedario
print("\nABECEDARIO\n")
letra1 = input("\tLetra 1: ")
letra2 = input("\tLetra 2: ")
letra3 = input("\tLetra 3: ")
if (letra1 < letra2):
	if (letra1 < letra3):
		print("\nLa primera letra que aparece en el abecedario es %s"%letra1)
	else:
		if (letra3 < letra2):
			print("\nLa primera letra que aparece en el abecedario es %s"%letra3)
else:
	if (letra2 < letra3):
		print("\nLa primera letra que aparece en el abecedario es %s"%letra2)
	else:
		print("\nLa primera letra que aparece en el abecedario es %s"%letra3)





