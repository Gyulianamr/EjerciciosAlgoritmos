#23.	Contar Hojas en un Árbol Binario Escribe una función que cuente cuántos nodos hoja (nodos sin hijos) tiene un árbol binario.#

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def contar_hojas(arbol):
    # Si el árbol es vacío, no hay hojas
    if arbol is None:
        return 0
    
    # Si el nodo no tiene hijos, es una hoja
    if arbol.izquierda is None and arbol.derecha is None:
        return 1
    
    # Recursión en los subárboles izquierdo y derecho
    return contar_hojas(arbol.izquierda) + contar_hojas(arbol.derecha)

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

# Llamar a la función
print("Número de nodos hoja:", contar_hojas(raiz))
