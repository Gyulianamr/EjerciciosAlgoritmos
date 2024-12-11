#13.	Cola Circular Implementa una cola circular con una longitud fija. Incluye métodos para añadir y eliminar elementos#
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
        elif self.frente == self.final:
            valor_eliminado = self.cola[self.frente]
            self.frente = self.final = -1
            return valor_eliminado
        else:
            valor_eliminado = self.cola[self.frente]
            self.frente = (self.frente + 1) % self.tamaño
            return valor_eliminado

    def peek(self):
        if self.is_empty():
            print("La cola está vacía.")
        else:
            return self.cola[self.frente]

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


cola = CircularQueue(5)

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

cola.display()

print("Elemento eliminado:", cola.dequeue())
cola.display()

cola.enqueue(60)
cola.display()
