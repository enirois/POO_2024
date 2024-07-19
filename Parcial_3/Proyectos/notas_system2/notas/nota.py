from Parcial_3.Proyectos.notas_system2.usuarios.usuario import *
from main import menu_notas
from funciones import *

class Notas:
    def __init__(self,id,usuario_id,titulo,descripcion,fecha):
        self.id=id
        self.usuario_id=usuario_id
        self.titulo=titulo
        self.descripcion=descripcion
        self.fecha=fecha


    def crear(self):
        menu_notas()

    def mostrar(self):
        menu_notas()

    def actualizar(self):
        menu_notas()    