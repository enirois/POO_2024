# Inicializamos una lista vacía
lista = []

# Añadir valores a la lista mientras su longitud sea menor a 120
contador = 1
while len(lista) < 120:
    lista.append(contador)
    contador += 1

# Mostrar la lista usando un bucle for
print("Lista con valores añadidos:")
for valor in lista:
    print(valor)
