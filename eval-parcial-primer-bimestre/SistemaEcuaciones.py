#Calcular el  valor de x,y ingresando por teclado los valores respectivos
a=float(input("\ningrese el valor de 'a': "))
b=float(input("ingrese el valor de 'b': "))
c=float(input("ingrese el valor de 'c': "))
d=float(input("ingrese el valor de 'd': "))
e=float(input("ingrese el valor de 'e': "))
f=float(input("ingrese el valor de 'f': "))
x = ((c*e) - (b*f)) / ((a*e)- (b*d))
y = ((c*e) - (b*f)) / ((a*e)- (b*d))
print("\nx: %.2f\n"%x,"y: %.2f"%y)