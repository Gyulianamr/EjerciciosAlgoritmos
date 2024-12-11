#18Eliminar Duplicados de una Lista EnlazadaEscribe un método que recorra una lista enlazada y elimine los nodos con valores duplicados.#

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

    def eliminar_duplicados(self):
        if not self.cabeza:
            return

        valores = set()
        actual = self.cabeza
        valores.add(actual.valor)
        while actual.siguiente:
            if actual.siguiente.valor in valores:
                # Eliminar el nodo duplicado
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores.add(actual.siguiente.valor)
                actual = actual.siguiente

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(2)
lista.agregar(4)
lista.agregar(1)

print("Lista antes de eliminar duplicados:")
lista.imprimir_lista()

lista.eliminar_duplicados()

print("Lista después de eliminar duplicados:")
lista.imprimir_lista()
