from principal import agregar_pelicula, remover_pelicula, consultar_peliculas, main, actualizar_pelicula, buscar_pelicula, vaciar_peliculas

peliculas=[]
op=True
while op:
    print(f"\n .-.-.-CINEPOLIS-.-.-. \n 1.- Agregar \n 2.- Remover \n 3.- Consultar peliculas \n 4.- Actualizar Peliculas \n 5.- Buscar Peliculas \n 6.- Vaciar Peliculas \n 7.- Salir" )
    op=input("\t Elija una opcion para realizar a la pelicula: ")
    
    if op!="7":
        op(op, peliculas)
    else:
      op=False
      print("\n \t ....----Gracias por utilizar el sistema----....")