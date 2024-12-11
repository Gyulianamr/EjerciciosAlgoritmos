#16.	Implementar una Lista Enlazada Simple Crea una clase Nodo y una clase ListaEnlazada. Implementa métodos para agregar elementos al final, eliminar un elemento, y buscar un elemento.
#

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        if not self.cabeza:
            print("La lista está vacía.")
            return

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            print(f"El elemento {dato} fue eliminado.")
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            print(f"El elemento {dato} fue eliminado.")
        else:
            print(f"El elemento {dato} no se encuentra en la lista.")

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                print(f"El elemento {dato} fue encontrado en la lista.")
                return True
            actual = actual.siguiente
        print(f"El elemento {dato} no se encuentra en la lista.")
        return False

    def mostrar(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía.")
            return

        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.mostrar()

lista.buscar(20)
lista.eliminar(20)
lista.mostrar()

lista.buscar(40)
lista.eliminar(40)
