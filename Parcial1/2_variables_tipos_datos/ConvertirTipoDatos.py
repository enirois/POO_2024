"""

Comentario de varias lineas

Nota:Cuando se imprime en pantalla una cadena de caracteres 
se trabaja por default con "cadenas", es decir python no puede
concatenar otra cosa que no sea un string (str)

"""


texto="Soy una cadena de caracteres"
numero=23

#Concatenar str con str

print("Soy otra cadena y "+texto)

#Concatenar str con int
numero_str=str(numero)
print("El numero es: "+numero_str)

print("El numero: "+str(numero))


#Concatenar float con e int con str

n3=23
n4=33.0

suma=float(n3)+n4

print(f"La suma es: {suma}")



#Concatenar int con str

n1=int('23')
n2=33

suma=n1+n2

print("La suma es: "+str(suma))

print(f"La suma es: {suma}")