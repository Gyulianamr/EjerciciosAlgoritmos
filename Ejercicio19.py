# 19.	Fusionar Dos Listas Enlazadas Dadas dos listas enlazadas ordenadas, escribe una función que las combine en una nueva lista enlazada también ordenada.
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
        if not self.cabeza or self.cabeza.dato > dato:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.dato < dato:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

def fusionar_listas(lista1, lista2):
    nueva_lista = ListaEnlazada()
    nodo1 = lista1.cabeza
    nodo2 = lista2.cabeza

    while nodo1 and nodo2:
        if nodo1.dato < nodo2.dato:
            nueva_lista.agregar(nodo1.dato)
            nodo1 = nodo1.siguiente
        else:
            nueva_lista.agregar(nodo2.dato)
            nodo2 = nodo2.siguiente

    while nodo1:
        nueva_lista.agregar(nodo1.dato)
        nodo1 = nodo1.siguiente

    while nodo2:
        nueva_lista.agregar(nodo2.dato)
        nodo2 = nodo2.siguiente

    return nueva_lista

# Ejemplo de uso:
lista1 = ListaEnlazada()
lista2 = ListaEnlazada()

# Agregar elementos a las listas enlazadas
for valor in [1, 3, 5]:
    lista1.agregar(valor)
for valor in [2, 4, 6]:
    lista2.agregar(valor)

print("Lista 1:")
lista1.imprimir()
print("Lista 2:")
lista2.imprimir()

# Fusionar las listas
lista_fusionada = fusionar_listas(lista1, lista2)
print("Lista fusionada:")
lista_fusionada.imprimir()
