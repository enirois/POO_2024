""""
    Los errores de excepciones en un lenguaje de programación no es otra cosa que los errores
    en tiempo de ejecución. Cuando se manejan errores mediantes las excepciones en realidad
    se dice que se evita que se presenten esos erorres en el programa en el tiempo de ejecución
"""
#Ejemplo: se representa un error cuando no es generada una variable
try:
    nombre = input("Dame el nombre completo de una persona: ")

    if len(nombre)>0:
        nombre_usuario="El nombre del usuario del sistema es: "+nombre

    print(nombre_usuario)    
except:
    print("Es necesario introducir un nombre de una persona")    

#Ejemplo: cuando se solicita un numero y se ingresa otra cosa
try: 
    numero = int(input("Ingresa un numero entero")) 

    if numero>0:
        print ("Es positivo")
    else:
        print ("Es negativo")
except ValueError:
    print("No es posible convertir una letra a un numero")

#Ejemplo 3: cuando se generan multiples excepciones
try:
    numero1=int(input("Ingresa un numero: "))
    print("El cuadrado del numero es: "+str(numero1+numero1))
except TypeError:
    print("Es necesario convertir el numero a entero")
except ValueError:
    print("No es posible convertir una letra a numero")
else:
    print("Todo se ejecuto correctamente")        
finally:
    print("Ya termino")