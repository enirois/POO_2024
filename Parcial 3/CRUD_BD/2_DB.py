import mysql.connector
try:
   conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python"
)
   micursor=conexion.cursor()
except:
    (f"ocurrio un error con el sistema de verificasion")
    if conexion.is_connected():
#crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
      micursor=conexion.cursor()
  
    sql="create database bd_python"
  #Ejecutar la consulta  SQL
    micursor.execute(sql)
  
    if micursor:
      print(f"Se creo la base de datos exitosamente")
      
      #Mostrar las bases de datos que existen en el servidor MYSQL
      micursor.execute("show database")
      
      for x in micursor:
          print(x)
          


   