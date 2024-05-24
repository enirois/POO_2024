"""

   Existe una estructura de condicion llama "if" 
   la cual evalua una condicion para encontrar el valor "True" o se cumple
   la condicion se ejecuta la linea o lineas codigo 

   Tenes 4 variantes del if

   1.- if simple
   2.- if compuesto
   3.- if anidado
   4.- if y elif
   
"""

#Ejemplo 1 if simple

color="rojo"
if color=="rojo":
    print("Soy el color rojo")

#Ejemplo 2 if compuesto

color="rojo"
if color=="rojo":
    print("Soy el color rojo")  
else:      
    print("No soy el color rojo")


#Ejemplo 3 if anidado

color="rojo"
if color=="rojo":
    print("Soy el color rojo")  
    if color!="rojo":
       print("Soy otro color")   
else:      
    print("No soy el color rojo")
    if color!="rojo":
       print("Soy otro color") 

#Ejemplo 4 if con elif

color="rojo"
if color=="rojo":
    print("Soy el color rojo")  
elif color=="negro":    
    print(" soy el color negro")
elif color=="verde":    
    print(" soy el color verde")   
else:
    print("No soy rojo, verde o negro")