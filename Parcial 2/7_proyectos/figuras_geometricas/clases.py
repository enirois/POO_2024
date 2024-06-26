import math

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, x, y):
        self.x = x
        self.y = y


class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho


class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2


rectangulo1 = Rectangulos(x=3,y=4, alto=10, ancho=20, visible=True)
circulo1 = Circulos(x=3, y=3, visible=True, radio=6)
