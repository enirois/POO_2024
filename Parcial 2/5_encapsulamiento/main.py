from coches import *

print("Objeto 1")
coche1=Coches("blanco","2010",300,500,2)
coche1.getInfo()

print("Objeto 2")
coche2=Coches("Azul","2012",200,900,1)
coche2.getInfo()

#print(coche1.publico_atributo) esto no es permitido
print(coche1.getPrivadoAtributo(self))