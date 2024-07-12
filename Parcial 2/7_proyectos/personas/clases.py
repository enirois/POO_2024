class Personas:
    def __init__(self, nombre, edad, tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel



    def info_personal(self):
            print(f"Informacion de la persona: {self.getNombre(), self.getEdad(), self.getTel()}")


    def getNombre(self):
         return self.nombre
    
    def getEdad(self):
         return self.edad
    
    def getTel(self):
         return self.tel
    
    def getNombre(self, nombre):
        self.nombre=nombre
    
    def getEdad(self, edad):
        self.edad=edad
    
    def getTel(self, tel):
        self.tel=tel

class Docentes:
     w

