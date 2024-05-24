print("Bienvenido a nuestro programa \"Adivinando el número \". A continuación tienes que adivinar el numero entre 1 y 120")
while True:
    try:
        numero=int(input("Elija su numero: "))
        if(numero<1 or numero>120):
            print("El numero debe ser entre 1 y 120")
        elif(numero<111):
            print("El numero es más grande")
        elif(numero>111):
            print("El numero es más pequeño")
        elif(numero==111):
            print("--------------------------------")
            print("\n")
            print("CORRECTO, HAZ GANADO")
            print("\n")
            print("--------------------------------")
            break    
    except ValueError:
        print("Su numero no es un entero, pruebe de nuevo")     