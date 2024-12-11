#14 Reorganizar una Cola Dada una cola de números, escribe un programa que reorganice los elementos para que los números pares queden al principio y los impares al final.#

class CircularQueue:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.cola = [None] * tamaño
        self.frente = -1
        self.final = -1

    def is_empty(self):
        return self.frente == -1

    def is_full(self):
        return (self.final + 1) % self.tamaño == self.frente

    def enqueue(self, valor):
        if self.is_full():
            print("La cola está llena. No se puede insertar el elemento.")
        elif self.is_empty():
            self.frente = self.final = 0
            self.cola[self.final] = valor
        else:
            self.final = (self.final + 1) % self.tamaño
            self.cola[self.final] = valor

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía. No se puede eliminar el elemento.")
            return None
        elif self.frente == self.final:
            valor_eliminado = self.cola[self.frente]
            self.frente = self.final = -1
            return valor_eliminado
        else:
            valor_eliminado = self.cola[self.frente]
            self.frente = (self.frente + 1) % self.tamaño
            return valor_eliminado

    def display(self):
        if self.is_empty():
            print("La cola está vacía.")
        else:
            indice = self.frente
            while True:
                print(self.cola[indice], end=" ")
                if indice == self.final:
                    break
                indice = (indice + 1) % self.tamaño
            print()

    def organizarpares(self):
        if self.is_empty():
            print("La cola está vacía. No se puede organizar.")
            return

        pares = []
        impares = []

        # Separar pares e impares
        indice = self.frente
        while True:
            if self.cola[indice] % 2 == 0:
                pares.append(self.cola[indice])
            else:
                impares.append(self.cola[indice])

            if indice == self.final:
                break
            indice = (indice + 1) % self.tamaño

        # Combinar pares e impares
        nueva_cola = pares + impares

        # Actualizar la cola con la nueva organización
        self.cola = nueva_cola + [None] * (self.tamaño - len(nueva_cola))
        self.frente = 0
        self.final = len(nueva_cola) - 1

        return nueva_cola


# Ejemplo de uso
cola = CircularQueue(5)

cola.enqueue(10)
cola.enqueue(15)
cola.enqueue(20)
cola.enqueue(25)
cola.enqueue(30)

print("Cola original:")
cola.display()

print("\nCola reorganizada (pares al frente):")
cola.organizarpares()
cola.display()
