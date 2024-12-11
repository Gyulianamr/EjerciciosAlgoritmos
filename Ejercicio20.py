#20.	Implementar un Árbol Binario Crea una clase NodoArbol y una clase ArbolBinario. Implementa métodos para insertar elementos, recorrer el árbol en orden (inorder) y buscar un elemento.
#

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def recorrido_inorder(self):
        elementos = []
        self._recorrido_inorder_recursivo(self.raiz, elementos)
        return elementos

    def _recorrido_inorder_recursivo(self, nodo, elementos):
        if nodo is not None:
            self._recorrido_inorder_recursivo(nodo.izquierdo, elementos)
            elementos.append(nodo.valor)
            self._recorrido_inorder_recursivo(nodo.derecho, elementos)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)



arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido inorder:", arbol.recorrido_inorder())
print("Buscar 40:", arbol.buscar(40))  # True
print("Buscar 90:", arbol.buscar(90))  # False
