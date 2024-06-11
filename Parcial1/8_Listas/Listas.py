"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo 
 un mismo nombre, para acceder a los valores se
 hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
import os


#Ejemplo 1 crear una lista con datos numericos e imprimir el contenido 

lista=[23,34]
print(lista)

#recorrer la lista con el for

for i in lista:
 print(i)

#recorrer la lsiat con el while
i=0
while i<=len(lista)-1:
   print(lista[i]) 
   i+=1

#Ejemplo2 Crear una lista de 4 palabras, solicitar una palabra y buscar la coincidencia en la lista e indicar si la encontro o no y en que posición


# palabras=["hola","2024","hola","UTD"]
# print(palabras)

# palabra_buscar=input("Ingresa la palabra a buscar: ")

# noencontre=True

# # for i in palabras:
# #   if palabra_buscar==i:
# #     print(f"Encontre la palabra: {i}, en la posición: {palabras.index(i)}")
# #     noencontre=False

# i=0
# while i<len(palabras):
#    if palabra_buscar==palabras[i]:
#       print(f"Encontre la palabra: {palabra_buscar}, en la posición: {i}")
#       noencontre=False
#    i+=1     
  

# if noencontre:
#     print(f"No encontre la palabra") 

#Ejemplo 3 Agregar y Eliminar elementos de una lista
os.system("clear")

numeros=[23,34,23]

print(numeros)

#agregar un elemento
numeros.append(100) 
print(numeros)
numeros.insert(3,200)
print(numeros)

#eliminar un elemento
numeros.remove(100) #indicar el elemento a borrar
print(numeros)
numeros.pop(2) #indicar la posicion del el elemento a borrar
print(numeros)

#Ejemplo 4.- Crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

agenda=[
   ["Carlos",6182334567],
   ["Karin",6182334568],
   ["Leon",6182334569],
   ["Pedro",6182334569],
]

print(agenda)

for i in agenda:
   print(f"{agenda.index(i)+1}.- {i}")




#ejemplo 5 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas. 
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas

# Archivo: peliculas.py

# Función para agregar una película a la lista
def agregar_pelicula(peliculas, nombre):
    peliculas.append(nombre)
    print("Película agregada con éxito.")

# Función para remover una película de la lista
def remover_pelicula(peliculas, nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print("Película removida con éxito.")
    else:
        print("La película no está en la lista.")

# Función para consultar las películas en la lista
def consultar_peliculas(peliculas):
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print("-", pelicula)
    else:
        print("No hay películas en la lista.")

# Función principal que ejecuta el programa
def main():
    peliculas = []  # Lista para almacenar los nombres de las películas

    while True:
        print("\n=== Menú de opciones ===")
        print("1. Agregar película")
        print("2. Remover película")
        print("3. Consultar películas")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película que desea agregar: ")
            agregar_pelicula(peliculas, nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la película que desea remover: ")
            remover_pelicula(peliculas, nombre)
        elif opcion == "3":
            consultar_peliculas(peliculas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

