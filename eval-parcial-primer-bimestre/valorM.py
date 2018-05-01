#Calcular el valor de m, ingresando por teclado los valores de x,y,z
x=float(input("\ningrese el valor de 'X': "))
y=float(input("ingrese el valor de 'Y': "))
z=float(input("ingrese el valor de 'Z': "))
m=(x+(y/z))/(x-(y/z))
print("el valor de m, en base a las variables\n\tx= {0}\n\t\ty= {1}\n\t\t\tz= {2}\nda como resultado:\n".format(x,y,z),"\t\t\t\tm: %.2f"%m)