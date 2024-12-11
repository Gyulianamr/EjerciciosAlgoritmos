# 22.Recorrido por Niveles (BFS) Implementa un método para recorrer un árbol binario por niveles utilizando una cola.
#

from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def recorrido_por_niveles(self):
        if not self.raiz:
            return []

        resultado = []
        cola = deque([self.raiz])

        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual.valor)

            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)

            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)

        return resultado


arbol = ArbolBinario()
arbol.raiz = Nodo(1)
arbol.raiz.izquierdo = Nodo(2)
arbol.raiz.derecho = Nodo(3)
arbol.raiz.izquierdo.izquierdo = Nodo(4)
arbol.raiz.izquierdo.derecho = Nodo(5)
arbol.raiz.derecho.izquierdo = Nodo(6)
arbol.raiz.derecho.derecho = Nodo(7)

print("Recorrido por niveles:", arbol.recorrido_por_niveles())
