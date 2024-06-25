from coches import *

print("Objeto 1")
coche1=Coches("blanco","2010",300,500,2)
coche1.getInfo()

print("Objeto 2")
coche2=Coches("Azul","2012",200,900,1)
coche2.getInfo()

print("Objeto 3")
camion1=Camiones("Azul","dina",180,300,12,8,2500)
camion1.getInfo()

print("Objeto 4")
camion2=Camiones("Azul","Mitsubichi",180,300,12,8,2500)
camion2.getInfo()


print("Objeto 5")
camioneta1=Camionetas("verde","Mitsubichi",60,450,12,8,True)
camioneta1.getInfo()

print("Objeto 6")
camioneta2=Camionetas("morado","Nisan",50,700,10,5,False)
camioneta2.getInfo()