def promedioparciales(parcial1, parcial2, parcial3):
    return (parcial1 + parcial2 + parcial3) / 3

def calfinal(promedio_parciales, proyecto_final):
    return (promedio_parciales + proyecto_final) / 2

def solicitar_datos_alumno():
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")
    parcial1 = float(input("Calificación del primer parcial: "))
    parcial2 = float(input("Calificación del segundo parcial: "))
    parcial3 = float(input("Calificación del tercer parcial: "))
    proyecto_final = float(input("Calificación del proyecto final: "))
    
    promedio_parciales = promedioparciales(parcial1, parcial2, parcial3)
    calificacion_final = calfinal(promedio_parciales, proyecto_final)
    
    print(f"\nAlumno: {nombre}")
    print(f"Carrera: {carrera}")
    print(f"Promedio de los parciales: {promedio_parciales:.2f}")
    print(f"Calificación final: {calificacion_final:.2f}")
    
    return nombre, promedio_parciales, calificacion_final, proyecto_final

def main():
    seguir = "SI"
    calificaciones_finales = []
    alumnos_extraordinario = []
    
    while seguir.upper() == "SI":
        nombre, promedio_parciales, calificacion_final, proyecto_final = solicitar_datos_alumno()
        calificaciones_finales.append(calificacion_final)
        
        if calificacion_final<80 and proyecto_final>50:
            alumnos_extraordinario.append(nombre)
        
        seguir = input("\n¿Desea ingresar los datos de otro alumno? (SI/NO): ")
    
    if calificaciones_finales:
        promedio_final_alumnos = sum(calificaciones_finales) / len(calificaciones_finales)
        print(f"\nPromedio de la calificación final de los alumnos capturados: {promedio_final_alumnos:.2f}")
        
        if alumnos_extraordinario:
            print("\nAlumnos que deben presentar examen extraordinario:")
            for alumno in alumnos_extraordinario:
                print(f"- {alumno}: Presenta examen extraordinario")
        else:
            print("\nNingún alumno necesita presentar examen extraordinario.")

if __name__ == "__main__":
    main()
