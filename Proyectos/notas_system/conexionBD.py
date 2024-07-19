<<<<<<< HEAD
import mysql.connector

try:
    #Conectar con la BD en MySQL
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'
    )
    #Crear un objeto de tipo cursor que tenga un parametro que permita reutilizar el objeto 
    cursor=conexion.cursor(buffered=True)
except:
     print(f"Ocurrio un error con el Sistema por favor verifique ...")    
=======
import mysql.connector

try:
    conexion=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='bd_python'
    )
except:
    print(f"Ocurrio un Error con el Seridor Por Favor Verifica...")
>>>>>>> 4c82360a4039eba87752e1a115fd4797f2f5c1f1
