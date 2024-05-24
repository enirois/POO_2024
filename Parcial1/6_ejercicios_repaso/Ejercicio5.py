print("Bienvenido a nuestro programa que muestra los numeros")
lim1=int(input("Ingrese el limite numero 1: "))
lim2=int(input("Ingrese el limite numero 2: "))
if lim1 > lim2:
    lim1, lim2 = lim2, lim1

for i in range(lim1, lim2+1):
    print(i)