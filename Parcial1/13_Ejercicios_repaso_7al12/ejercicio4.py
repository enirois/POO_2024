#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = [1, 2, 3]
cadena = "Hola, mundo"
entero = 42
logico = True

# Función para determinar el tipo de dato y imprimir un mensaje
def imprimir_tipo_dato(variable):
    if isinstance(variable, list):
        print(f"La variable {variable} es de tipo lista.")
    elif isinstance(variable, str):
        print(f"La variable '{variable}' es de tipo cadena.")
    elif isinstance(variable, int):
        print(f"La variable {variable} es de tipo entero.")
    elif isinstance(variable, bool):
        print(f"La variable {variable} es de tipo lógico.")
    else:
        print(f"La variable {variable} es de un tipo no identificado.")

# Imprimir mensajes para cada variable
imprimir_tipo_dato(lista)
imprimir_tipo_dato(cadena)
imprimir_tipo_dato(entero)
imprimir_tipo_dato(logico)
