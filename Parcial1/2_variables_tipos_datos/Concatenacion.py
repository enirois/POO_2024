# formas de concatenacion en python

nombre = 'Miguel Ramirez'
especialidad = "Area de SW multiplataforma"
carrera = "Ingeniería en Gestión y Desarrollo de SW"

# 1er forma
print("Mi nombre es"+nombre+", estoy en la especialidad de "+especialidad+" en la carrera de "+carrera)

print("\n")

# 2da forma
print("Mi nombre es", nombre, ", estoy en la especialidad de ", especialidad, " en la carrera de ", carrera)

print("\n")

# 3er forma MAS COMUN EN PYTHON
print(f"Mi nombre es", {nombre}, ", estoy en la especialidad de ", {especialidad}, " en la carrera de ", {carrera})

print("\n")

# 4ta forma
print("Mi nombre es {}, estoy en la especialidad de {} en la carrera de {}" .format (nombre, especialidad, carrera))

print("\n")

# 5ta forma
print('Mi nombre es '+nombre+', estoy en la especialidad de '+especialidad+' en la carrera de '+carrera)

print("\n")