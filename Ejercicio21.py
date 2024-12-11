#21.	Altura de un Árbol Binario Escribe una función que calcule la altura de un árbol binario.
#
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def altura_arbol(nodo):
    if nodo is None:
        return -1  # Por convención, la altura de un árbol vacío es -1
    else:
        altura_izquierda = altura_arbol(nodo.izquierdo)
        altura_derecha = altura_arbol(nodo.derecho)
        return 1 + max(altura_izquierda, altura_derecha)


raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("La altura del árbol es:", altura_arbol(raiz))
