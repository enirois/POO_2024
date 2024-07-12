from conexionBD import *
try:
      micursor=conexion.cursor()
      sql="update clientes2 set direccion='col. Nueva Vizcaya'where id=1"
      micursor.execute(sql)
      conexion.commit()
except:
    print("hubo un error fatal")
else:
   print("Dato borrado exitosamente")
