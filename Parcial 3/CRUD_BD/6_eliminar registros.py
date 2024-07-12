from conexionBD import *
try:
  micursor=conexion.cursor()
  sql="delete from clientes where id=3"
  micursor.execute(sql)
  conexion.commit()
except:
 print("hubo un error fatal")
else:
 print("Dato borrado exitosamente")
