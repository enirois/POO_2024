def sol_info():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura}, Tipo de Sangre: {tipo_sangre}")

def show_info(nombre, edad, estatura, tipo_sangre):
    print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura}, Tipo de Sangre: {tipo_sangre}")

def obtain_info():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    return nombre, edad, estatura, tipo_sangre

def crear_paciente(nombre, edad, estatura, tipo_sangre):
    paciente = {
        "Nombre": nombre,
        "Edad": edad,
        "Estatura": estatura,
        "Tipo de Sangre": tipo_sangre
    }
    return paciente

# Uso de las funciones

# Función sin argumentos y sin retorno
sol_info()

# Función con argumentos y sin retorno
nombre = "Juan Perez"
edad = 30
estatura = 1.75
tipo_sangre = "O+"
show_info(nombre, edad, estatura, tipo_sangre)

# Función sin argumentos y con retorno
nombre, edad, estatura, tipo_sangre = obtain_info()
print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura}, Tipo de Sangre: {tipo_sangre}")

# Función con argumentos y con retorno
paciente = crear_paciente(nombre, edad, estatura, tipo_sangre)
print(paciente)
