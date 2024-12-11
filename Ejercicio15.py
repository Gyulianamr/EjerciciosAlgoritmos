#15.	Ordenar una Cola Escribe un programa que use solo operaciones de cola (enqueue y dequeue) para ordenar los elementos de una cola#

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

def sort_queue(q):
    """
    Ordena una cola utilizando solo operaciones de enqueue y dequeue.
    """
    n = q.size()

    for i in range(n):
        # Encuentra el elemento más pequeño en el rango restante
        min_index = -1
        min_value = float('inf')

        for j in range(n):
            value = q.dequeue()

            # Actualiza el índice del elemento mínimo
            if value < min_value and j < n - i:
                min_value = value
                min_index = j

            q.enqueue(value)

        # Vuelve a insertar la cola excluyendo el elemento mínimo
        for j in range(n):
            value = q.dequeue()

            if j != min_index:
                q.enqueue(value)

        # Inserta el elemento mínimo al final
        q.enqueue(min_value)

# Ejemplo de uso
if __name__ == "__main__":
    q = Queue()
    elements = [3, 1, 4, 1, 5, 9, 2]

    for element in elements:
        q.enqueue(element)

    print("Cola original:", q.items)
    sort_queue(q)
    print("Cola ordenada:", q.items)