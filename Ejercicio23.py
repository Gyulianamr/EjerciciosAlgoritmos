#23.	Contar Hojas en un Árbol Binario Escribe una función que cuente cuántos nodos hoja (nodos sin hijos) tiene un árbol binario.#

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_hojas(arbol):
    
    if arbol is None:
        return 0
    
   
    if arbol.izquierda is None and arbol.derecha is None:
        return 1
    
   
    return contar_hojas(arbol.izquierda) + contar_hojas(arbol.derecha)


raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)


print("Número de nodos hoja:", contar_hojas(raiz))
