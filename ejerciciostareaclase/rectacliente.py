from Rectangulo import Rectangulo


    # Crear dos rectángulos
rect1 = Rectangulo(5, 10)
rect2 = Rectangulo(3, 7)

    # Imprimir información de los rectángulos
print(rect1)
print(rect2)

    # Comparar rectángulos por altura
if rect1.altura > rect2.altura:
    print("El primer rectángulo es más alto que el segundo.")
elif rect2.altura > rect1.altura:
    print("El segundo rectángulo es más alto que el primero.")
else:
    print("Ambos rectángulos tienen la misma altura.")


