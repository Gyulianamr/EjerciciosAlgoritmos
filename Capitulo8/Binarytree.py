"""8.2 Escriba un programa que tome una cadena que contenga una expresión de sufijo y construya un árbol binario para representar
la expresión algebraica como la que se muestra en la Figura 8-16. Necesita una clase BinaryTree, como la de BinarySearchTree, 
pero sin claves ni orden de los nodos. En lugar de los métodos find(), insert() y delete(), necesita la capacidad de crear BinaryTrees
de un solo nodo que contenga un solo operando y un método para combinar dos árboles binarios para crear un tercero con un operador como nodo raíz
La sintaxis de los operadores y operandos es la misma que se utilizó en el módulo PostfixTranslate.py del Capítulo 4. 
Puede usar la función nextToken() en ese módulo para analizar la cadena de entrada en tokens de operador y operando.
No es necesario que los paréntesis sean delimitadores porque las expresiones de sufijo no los utilizan. Compruebe que la expresión de entrada
produce una sola expresión algebraica y genere una excepción si no lo hace. En el caso de los árboles binarios algebraicos válidos,
utilice recorridos previos, internos y posteriores al orden del árbol para traducir la entrada en los formularios de salida.
Incluya paréntesis para el recorrido en orden para que la prioridad del operador quede clara en la traducción de salida. 
Ejecute su programa con al menos las siguientes expresiones: a. 91 95 + 15 + 19 + 4 * b. B B * A C 4 * * c. 42 d. A 57 # esto debería producir una excepción e. + / # esto debería producir una excepción"""

class BinaryTree:
    def __init__(self, valor):
        """Inicializa un nodo del árbol con un valor."""
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def combinar_arboles(operator, arbolizquierdo, arbolderecho):
        """Combina dos árboles con un operador como raíz."""
        raiz = BinaryTree(operator)
        raiz.izquierda = arbolizquierdo
        raiz.derecha= arbolderecho
        return raiz

    def preorder(self):
        result = [self.valor]
        if self.izquierda:
            result += self.izquierda.preorder()
        if self.derecha:
            result += self.derecha.preorder()
        return result

    def inorder(self):
        """Devuelve la travesía en inorden con paréntesis para la precedencia."""
        result = []
        if self.izquierda:
            result += ["("] + self.izquierda.inorder()
        result += [self.valor]
        if self.derecha:
            result += self.derecha.inorder() + [")"]
        return result

    def postorder(self):
        """Devuelve la travesía en postorden."""
        result = []
        if self.izquierda:
            result += self.izquierda.postorder()
        if self.derecha:
            result += self.derecha.postorder()
        result += [self.valor]
        return result


def Construir_arbol(postfix_expr):
    """a partir de una expresión posfija."""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in postfix_expr.split():
        if token.isalnum():  # Operando
            stack.append(BinaryTree(token))
        elif token in operators:  # Operador
            if len(stack) < 2:
                raise ValueError("Expresión inválida: no hay suficientes operandos.")
            right = stack.pop()
            left = stack.pop()
            stack.append(BinaryTree.combinar_arboles(token, left, right))
        else:
            raise ValueError(f"Token inválido encontrado: {token}")

    if len(stack) != 1:
        raise ValueError("Expresión inválida: demasiados operandos o operadores.")
    return stack.pop()


def Evaluar_Expresion(postfix_expr):
    """Evalúa la expresión y devuelve las travesías preorden, inorden y postorden."""
    try:
        tree = Construir_arbol(postfix_expr)
        print(f"Expresión posfija: {postfix_expr}")
        print("Preorden: ", " ".join(tree.preorder()))
        print("Inorden: ", "".join(tree.inorder()))
        print("Postorden:", " ".join(tree.postorder()))
    except ValueError as e:
        print(f"Error: {e}")


# Pruebas con las expresiones dadas
expressions = [
    "91 95 + 15 + 19 + 4 *",  # Válida
    "B B * A C 4 * *",       # Válida
    "42",                    # Válida
    "A 57",                  # Inválida
    "+ /"                    # Inválida
]

for expr in expressions:
    print("\n---")
    Evaluar_Expresion(expr)
