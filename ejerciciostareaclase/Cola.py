class Cola:
    def __init__(self, initialsize):
        self.__a = [None] * initialsize
        self.__nItems = 0

    def empty(self):
        return self.__nItems == 0

    def enqueue(self, item):  # ENCOLAR
        if self.__nItems < len(self.__a):  # Compare with the length of the list
            self.__a[self.__nItems] = item
            self.__nItems += 1
        else:
            print("La cola está llena")

    def dequeue(self):  # DESENCOLAR
        if not self.empty():  # si esta lleno
            item = self.__a[0]  # Get the first item
            # Desplazar elementos
            for i in range(1, self.__nItems):
                self.__a[i - 1] = self.__a[i]
            self.__a[self.__nItems - 1] = None
            self.__nItems -= 1
            return item
        else:
            return "La cola está vacía"

    def mostrar_cola(self):
        return self.__a[:self.__nItems]  # Retorna solo los elementos válidos

    def __str__(self):
        return str(self.__a[:self.__nItems])  # Retorna solo los elementos válidos

    def contar_sumar_pares_impares(self):
        suma_pares = 0
        suma_impares = 0
        conteo_pares = 0
        conteo_impares = 0

        for i in range(self.__nItems):
            if self.__a[i] % 2 == 0:
                suma_pares += self.__a[i]
                conteo_pares += 1
            else:
                suma_impares += self.__a[i]
                conteo_impares += 1

        promedio_pares = suma_pares / conteo_pares if conteo_pares > 0 else 0
        promedio_impares = suma_impares / conteo_impares if conteo_impares > 0 else 0

        return {
            "suma_pares": suma_pares,
            "promedio_pares": promedio_pares,
            "conteo_pares": conteo_pares,
            "suma_impares": suma_impares,
            "promedio_impares": promedio_impares,
            "conteo_impares": conteo_impares
        }
