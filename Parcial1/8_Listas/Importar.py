def opc(operacion, peliculas):
     
    if operacion=="1" or operacion=="Agregar" or operacion=="agregar":
            op2="Si"
            while op2=="Si" or op2=="si":
                    agrega=input("¿Qué pelicula agregaras? ")
                    peliculas.append(agrega)
                    print("\t Su pelicula se agrego correctamente")
                    op2=input("\t ¿Desea agregar otra pelicula? (Si/No) ")
          
    elif operacion=="2" or operacion=="Remover" or operacion=="remover":
                op2="Si"
                while op2=="Si" or op2=="si":
                    if peliculas:
                        print(f"Las películas disponibles son: {', '.join(peliculas)}")
                        quitar = input("¿Qué película deseas remover? ")
                        try:
                            peliculas.remove(quitar)
                            print("\t La película se removió correctamente")
                        except ValueError:
                            print("\t -----La película no está en la lista-----")
                    else:
                        print("\t No hay películas para remover")
                    op2 = input("\t ¿Desea remover otra película? (Si/No) ")

    elif operacion=="3" or operacion=="Consultar" or operacion=="consultar":
                    if peliculas:
                        print(f"\n Las películas disponibles son: {', '.join(peliculas)}")
                    else:
                        print("\t No hay películas en la lista")
    else:
        print("\t ..---Operación no válida---..")


