#12.	Simular una Fila de Banco Usa una cola para simular la atención al cliente en un banco. Cada cliente tiene un número asignado y se atiende en orden.

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

    def atender(self):
        if not self.esta_vacia():
            cliente = self.dequeue()
            print(f"Atendiendo al cliente {cliente}")
        else:
            print("No hay clientes en espera.")

cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)



cola.atender()  # Atendiendo al cliente 1
cola.atender()  # Atendiendo al cliente 2
cola.atender()  # Atendiendo al cliente 3
cola.atender()  # No hay clientes en espera
