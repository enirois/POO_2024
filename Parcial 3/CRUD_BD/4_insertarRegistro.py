from conexionBD import *

try:
    micursor=conexion.cursor()
    nombre=input("cual es tu nombre:")
    direccion=input("cual es tu direccion?")
    tel=input("cual es tu numero de telefono?")
    # sql="INSERT INTO clientes    (id, nombre, direccion, tel) VALUES (NULL, 'Daniel Contreras', 'Col. Centro', '6181563424')"

    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL,%s,%s, %s)"
    valores=(nombre, direccion, tel)

    micursor.execute(sql, valores)

    # Sirve para finalizar de manera exitosa la ejecicion del SQL
    conexion.commit()

except:
    print("Error porfavor verifica")

else:
    print("El registro se hizo ")