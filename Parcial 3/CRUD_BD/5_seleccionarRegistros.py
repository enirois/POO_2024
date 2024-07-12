from conexionBD import *

micursor=conexion.cursor()
sql="select from clientes"
micursor.execute(sql)
#crear un objeto para enviat el resultado la ejecucion del execute para posteriormente mostrar un ciclo
resultado=micursor.fetchall()

for x in resultado:
    print(x)