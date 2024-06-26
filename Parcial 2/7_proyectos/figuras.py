from figuras import Rectangulo, Circulo, Triangulo

rectangulo = Rectangulo(5.0, 10.0)
print(f'Área del rectángulo: {rectangulo.CalcularArea()}')

circulo = Circulo(7.0)
print(f'Área del círculo: {circulo.CalcularArea()}')

triangulo = Triangulo(8.0, 6.0)
print(f'Área del triángulo: {triangulo.CalcularArea()}')