print("Bienvenido a nuestro programa para sacar el porcentaje de un numero")
try:
    porcentaje = float(input("Ingrese el porcentaje: "))
    numero = float(input("Ingrese el número: "))
    resultado = (porcentaje/100) * numero
    print(f"El {porcentaje}% de {numero} es {resultado}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")