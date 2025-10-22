import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Punto(2, 3)
p2 = Punto(5, 7)
print("Punto 1:", p1)
print("Punto 2:", p2)
print("Distancia entre puntos:", p1.distancia(p2))
