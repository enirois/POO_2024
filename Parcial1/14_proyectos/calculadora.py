from principal import solicitarDatos, getCalculadora
from principal import n1,n2, ope

print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 6.- Salir")
opcion=input("\t Elige una opción: ").upper()


solicitarDatos()
print(getCalculadora(n1,n2,ope))
