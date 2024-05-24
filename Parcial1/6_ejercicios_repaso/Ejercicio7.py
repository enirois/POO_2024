print("Bienvenido a nuestro programa para ver numeros impares")
lim1=int(input("Elija un limite: "))
lim2=int(input("Elija otro limite: "))

if(lim1>lim2):
    lim1, lim2 = lim2, lim1

for i in range(lim1,lim2+1):
    if i % 2 !=0:
        print(i)