from main import menu_principal
from notas.nota import *
from funciones import *

class usuario:
    def __init__(self,id,nombre,apellidos,email,password,fecha):
        self.id=id
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.password=password
        self.fecha=fecha

    #Funcion para incriptar la contraseña
    def hash_password(self,contrasena)
        return

    def iniciar_sesion(self):
        menu_principal()
    
    def registrar(self):
        menu_principal()