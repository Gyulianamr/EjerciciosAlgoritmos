class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

def es_palindromo(cadena):
    # Filtrar la cadena: quitar espacios, puntuación, y convertir a minúsculas
    cadena_filtrada = ''.join(c for c in cadena if c.isalpha()).lower()
    
    # Crear una pila
    pila = Pila()

    # Apilar cada carácter de la cadena filtrada
    for char in cadena_filtrada:
        pila.apilar(char)

    # Comprobar si la cadena es un palíndromo
    for char in cadena_filtrada:
        if char != pila.desapilar():
            return False
    
    return True

# Prueba con la cadena dada
cadena_prueba = "arroz zorra"
if es_palindromo(cadena_prueba):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
