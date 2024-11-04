class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def es_mas_alto_que(self, otro_rectangulo):
        return self.altura > otro_rectangulo.altura()

    def __str__(self):
        return f"Rectángulo(base={self.base}, altura={self.altura}, área={self.area()}, perímetro={self.perimetro()})"


    







       




