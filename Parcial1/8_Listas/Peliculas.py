from Peliculas import opc

peliculas=[]
os.system("cls")
op=True
while op:
    print(f"\n .-.-.-CINEPOLIS-.-.-. \n 1.- Agregar \n 2.- Remover \n 3.- Consultar peliculas \n 4.- Salir")
    op=input("\t Elija una opcion para realizar a la pelicula: ")
    
    if op!="4":
        opc(op, peliculas)
    else:
      op=False
      print("\n \t ....----Gracias por utilizar el sistema----....")