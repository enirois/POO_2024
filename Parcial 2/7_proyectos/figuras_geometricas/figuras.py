from clases import Rectangulos, Circulos, Figuras, rectangulo1, circulo1

print("Rectángulo 1:")
print(f"Posición: ({rectangulo1.x}, {rectangulo1.y})")
print(f"Visible: {rectangulo1.estaVisible()}")
print(f"Área: {rectangulo1.calcularArea()}")

print("\nCírculo 1:")
print(f"Posición: ({circulo1.x}, {circulo1.y})")
print(f"Visible: {circulo1.estaVisible()}")
print(f"Área: {circulo1.calcularArea()}")