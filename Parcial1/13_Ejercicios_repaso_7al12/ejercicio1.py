#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#a.- Recorrer la lista y mostrarla
#b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#c.- ordenarla y mostrarla
#d.- mostrar su longitud
#e.- buscar algun elemento que el usuario pida por teclado

numeros = [23, 45, 12, 67, 34, 89, 78, 56]

#A: Recorrer la lista y mostrarla
def mostrar_lista(lista):
    for numero in lista:
        print(numero)

print("a. Recorrer la lista y mostrarla:")
mostrar_lista(numeros)

#B: Hacer una función que recorra la lista de números y devuelva un string
def lista_a_string(lista):
    return ' '.join(map(str, lista))

print("\nb. Función que recorre la lista y devuelve un string:")
string_lista = lista_a_string(numeros)
print(string_lista)

#C: Ordenarla y mostrarla
numeros_ordenados = sorted(numeros)
print("\nc. Lista ordenada:")
print(numeros_ordenados)

#D: Mostrar su longitud
print("\nd. Longitud de la lista:")
print(f"La longitud de la lista es: {len(numeros)} números")

#E: Buscar algún elemento que el usuario pida por teclado
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El numero {elemento} se encuentra en la lista."
    else:
        return f"El numero {elemento} no se encuentra en la lista."

elemento_buscado = int(input("\ne. Ingresa el número que deseas buscar en la lista: "))
resultado_busqueda = buscar_elemento(numeros, elemento_buscado)
print(resultado_busqueda)
