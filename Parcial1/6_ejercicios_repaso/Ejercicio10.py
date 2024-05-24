reprobados=0
aprobados=0
i=1
print("Bienvenido a nuestro programa para saber cuantos aprobados y reprobados hay")
while i<=15:
    try:
        promedio=float(input(f"Introduzca su promedio {i}: "))
        if promedio<0 or promedio>10:
            print("El promedio es incorrecto")
        else:
            if promedio<8:
                reprobados+=1
                i+=1
            if promedio>=8:
                aprobados+=1
                i+=1    
    except ValueError:
        print("El promedio tiene que ser un numero")
print(f"La cantidad de alumnos que aprobaron es {aprobados}\nLa cantidad de alumnos que reprobaron es {reprobados}")   