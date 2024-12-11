#11.	Implementación Básica de una Cola Crea una clase Cola que implemente las operaciones básicas: enqueue, dequeue y peek

class Cola:
    def __init__(self):
        self.cola = []
    
    def enqueue(self, elemento):
        self.cola.append(elemento)
    
    def dequeue(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return "La cola está vacía"
    
    def peek(self):
        if not self.esta_vacia():
            return self.cola[0]
        else:
            return "La cola está vacía"
    
    def esta_vacia(self):
        return len(self.cola) == 0
    
    def __str__(self):

        return str(self.cola)


cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print("Cola después de agregar elementos:", cola)
print("Elemento en la parte frontal:", cola.peek())
print("Elemento extraído:", cola.dequeue())
print("Cola después de dequeue:", cola)
