#17.	Invertir una Lista Enlazada Crea un método en la clase ListaEnlazada para invertir el orden de los nodos.
#

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  # Guardar referencia al siguiente nodo
            actual.siguiente = previo  # Invertir el enlace
            previo = actual  # Mover el puntero "previo" al nodo actual
            actual = siguiente  # Mover al siguiente nodo
        self.cabeza = previo  # Actualizar la cabeza de la lista al nuevo inicio

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

print("Lista original:")
lista.mostrar()

lista.invertir()

print("Lista invertida:")
lista.mostrar()
