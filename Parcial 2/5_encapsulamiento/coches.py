"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

"""este metodo especila se coloca dentro de la clase y se utiliza 
para dar un valor a lñpoa triburos del objeto al momento de crearlo """
#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    color="rojo"
    marca="Ferrari"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2
def init(self,color,marca,modelo,velocidad,caballaje,plazas):
     self.color=color
     self.marca=marca
     self.modelo=modelo
     self.velocidad=velocidad
     self.caballaje=caballaje
     self.plazas=plazas
    #Metodos o acciones o funciones que hace el objeto 

def acelerar(self):
        self.velocidad+=1

def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
#   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

def getColor(self):
      return self.color

def setColor(self,color):
      self.color=color 

def getMarca(self):
      return self.marca

def setMarca(self,marca):
      self.marca=marca 

def getModelo(self):
      return self.modelo

def setModelo(self,modelo):
      self.modelo=modelo        
def getVelocidad(self):
       return self.velocidad

def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

def getCaballaje(self):
       return self.caballaje

def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

def getPlazas(self):
       return self.plazas

def setPlazas(self,plazas):
      self.plazas=plazas

def getInfo(self):
        print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")     

    #Fin definir clase

#Crear un objetos o instanciar la clase

#en python el encapsulamiento tambbien se llama 
#visibilidad y por lo general define como seran los atributos y metdos publicos y privados
publico_atributo="soy un atributo publico"
#atributo privado
_privado_atributo="soy un atributo privado"
def  getPrivadorAtributo(self):
  return self._privado_atributo
#metodo privado
def _getFuncionaPrivada(self):
      print("soy metodo prividas")
      #es necesario haecrlo dentro de un metodo pubblico 
def getMetodoPublico(self):
      self._getMetodoPrivado()