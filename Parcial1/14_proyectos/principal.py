def solicitarDatos():
   print("\n")
   global n1,n2,ope
   n1=int(input("Numero #1: "))
   n2=int(input("Numero #2: "))
   ope=input("Operacion: ").upper()
  

def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = f"{num1} + {num2} = {int(num1) + int(num2)}"
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        resultado = f"{num1} - {num2} = {int(num1) - int(num2)}"
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = f"{num1} * {num2} = {int(num1) * int(num2)}"
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = f"{num1} / {num2} = {int(num1) / int(num2)}"
    elif operacion == "5" or operacion == "^" or operacion == "POTENCIA":
        resultado = f"{num1} ^ {num2} = {int(num1) ** int(num2)}"
    elif operacion == "6" or operacion == "RAIZ":
        resultado = f"√{num1} = {int(num1) ** 0.5}"
    elif operacion == "0" or operacion == "SALIR":
        resultado = "Saliendo del programa..."
    else:
        resultado = "Operación no válida"
    return resultado

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

# Función para actualizar una película en la lista
def actualizar_pelicula(peliculas, nombre_viejo, nombre_nuevo):
    if nombre_viejo in peliculas:
        index = peliculas.index(nombre_viejo)
        peliculas[index] = nombre_nuevo
        print("Película actualizada con éxito.")
    else:
        print("La película no está en la lista.")

# Función para buscar una película en la lista
def buscar_pelicula(peliculas, nombre):
    if nombre in peliculas:
        print(f"La película '{nombre}' está en la lista.")
    else:
        print(f"La película '{nombre}' no está en la lista.")

# Función para vaciar la lista de películas
def vaciar_peliculas(peliculas):
    peliculas.clear()
    print("Lista de películas vaciada con éxito.")

# Función principal que ejecuta el programa
def main():
    peliculas = []  # Lista para almacenar los nombres de las películas

    while True:
        print("\n=== Menú de opciones ===")
        print("1. Agregar película")
        print("2. Remover película")
        print("3. Consultar películas")
        print("4. Actualizar película")
        print("5. Buscar película")
        print("6. Vaciar lista de películas")
        print("7. Salir")

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
            nombre_viejo = input("Ingrese el nombre de la película que desea actualizar: ")
            nombre_nuevo = input("Ingrese el nuevo nombre de la película: ")
            actualizar_pelicula(peliculas, nombre_viejo, nombre_nuevo)
        elif opcion == "5":
            nombre = input("Ingrese el nombre de la película que desea buscar: ")
            buscar_pelicula(peliculas, nombre)
        elif opcion == "6":
            vaciar_peliculas(peliculas)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")