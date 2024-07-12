import mysql.connector

try:
#conectar con la BD en MYSQL

  conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
except Exception as e:
 print(f"tipo de excepcion:{type(e)._name_}")
 print("ocurrio un error con la conexion al server")

print()   
#verificar si la conexion es exitosa
if conexion.is_connected():
      print(f"se creo la conexion exitosamnete")
else:
     print(f"no fue posible conectyar con la BD")
     