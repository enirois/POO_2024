#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas

lista = []

# Comprobamos si la lista está vacía

if not lista:
    print("La lista está vacía. Vamos a llenarla.")
    while True:
        entrada = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        lista.append(entrada)

# Imprimimos el contenido de la lista en mayúsculas

print("\nContenido de la lista en mayúsculas:")
for elemento in lista:
    print(elemento.upper())
