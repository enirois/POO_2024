from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nombre varchar (60), direccion varchar (120), tel varchar(10))"

    micursor.execute(sql)

    if micursor:
        print(f"se creo la tabla exitosamente")
except:
    print(f"Ocurrio un problema porfavor verifica")

else:
    print(f"se creo la tabla exitosamente")

