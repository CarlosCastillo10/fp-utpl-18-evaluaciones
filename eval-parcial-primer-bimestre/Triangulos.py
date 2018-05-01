#Determinar si dos triangulos son congruentes
print("\nTRIANGULO 1\n")
lado1 = float(input("\tLado 1: "))
lado2 = float(input("\tLado 2: "))
lado3 = float(input("\tLado 3: "))
angulo1 = float(input("\tAngulo 1: "))
angulo2 = float(input("\tAngulo 2: "))
angulo3 = float(input("\tAngulo 3: "))
print("\nTRIANGULO 2\n")
lado4 = float(input("\tLado 1: "))
lado5 = float(input("\tLado 2: "))
lado6 = float(input("\tLado 3: "))
angulo4 = float(input("\tAngulo 1: "))
angulo5 = float(input("\tAngulo 2: "))
angulo6 = float(input("\tAngulo 3: "))
if (lado1 == lado4 and lado2 == lado5 and lado3 == lado6):
	if(angulo1 == angulo4 and angulo2 == angulo5 and angulo3 == angulo6):
		print("\nLos triangulos son CONGRUENTES")
	else:
		print("\nLos triangulos NO SON congruentes")
else:
	print("\nLos triangulos NO SON congruentes")
