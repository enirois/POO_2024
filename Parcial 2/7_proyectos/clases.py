from abc import ABC
from math import pi

class Figura(ABC):
    def CalcularArea(self) -> float:
        pass

class Rectangulo(Figura):
    def __init__(self, largo: float, ancho: float):
        self.largo = largo
        self.ancho = ancho

    def Largo(self) -> float:
        return self.largo

    def Largo(self, value: float):
        self.largo = value

    def Ancho(self) -> float:
        return self.ancho

    def Ancho(self, value: float):
        self.ancho = value

    def CalcularArea(self) -> float:
        return self.largo * self.ancho

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def Radio(self) -> float:
        return self.radio

    def Radio(self, value: float):
        self.radio = value

    def CalcularArea(self) -> float:
        return pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura: float, ancho: float):
        self.altura = altura
        self.ancho = ancho

    def Altura(self) -> float:
        return self.altura

    def Altura(self, value: float):
        self.altura = value

    def Ancho(self) -> float:
        return self.ancho

    def Ancho(self, value: float):
        self.ancho = value

    def CalcularArea(self) -> float:
        return (self.ancho * self.altura) / 2