#Crear una lista y un diccionario con el contenido de esta tabla: 

#  ACCION              TERROR        DEPORTES
#  MAXIMA VELOCIDAD    LA MONJA       ESPN
#  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#  RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#  imprimir la información

lista_contenido = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

diccionario_contenido = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

# Imprimir la información de la lista
print("Información de la lista:")
for fila in lista_contenido:
    print(", ".join(fila))

# Imprimir la información del diccionario
print("\nInformación del diccionario:")
for categoria, titulos in diccionario_contenido.items():
    print(f"{categoria}: {', '.join(titulos)}")
