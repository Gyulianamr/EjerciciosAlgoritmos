class StackOverflowError(Exception):
    """Excepción lanzada al intentar agregar a una pila llena."""
    pass

class StackUnderflowError(Exception):
    """Excepción lanzada al intentar quitar de una pila vacía."""
    pass

class Stack(object):
    def __init__(self, max):            # Constructor
        self.__stackList = [None] * max  # La pila se almacena como una lista
        self.__top = -1                  # No hay elementos inicialmente
        
    def push(self, item):               # Insertar elemento en la parte superior de la pila
        if self.isFull():               # Comprobar si la pila está llena
            raise StackOverflowError("No se puede agregar a una pila llena.")
        self.__top += 1                  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento
        
    def pop(self):                      # Eliminar el elemento superior de la pila
        if self.isEmpty():              # Comprobar si la pila está vacía
            raise StackUnderflowError("No se puede eliminar de una pila vacía.")
        top = self.__stackList[self.__top]   # Elemento superior 
        self.__stackList[self.__top] = None  # Eliminar la referencia del elemento
        self.__top -= 1                  # Disminuir el puntero
        return top                       # Devolver el elemento superior
    
    def peek(self):                     # Devolver el elemento superior
        if not self.isEmpty():           # Si la pila no está vacía
            return self.__stackList[self.__top] # Devolver el elemento superior
    
    def isEmpty(self):                  # Comprobar si la pila está vacía
        return self.__top < 0

    def isFull(self):                   # Comprobar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):                  # Devolver la cantidad de elementos en la pila
        return self.__top + 1
    
    def __str__(self):                  # Convertir la pila a cadena
        ans = "["                        # Comenzar con corchete izquierdo
        for i in range(self.__top + 1):  # Iterar a través de los elementos actuales
            if len(ans) > 1:              # Excepto junto al corchete izquierdo,
                ans += ", "                # separar elementos con coma
            ans += str(self.__stackList[i]) # Agregar la representación en cadena del elemento
        ans += "]"                       # Cerrar con corchete derecho
        return ans


    def es_palindromo(cadena):
        # Filtrar la cadena: quitar espacios, puntuación, y convertir a minúsculas
        cadena_filtrada = ''.join(c for c in cadena if c.isalpha()).lower()
        
        # Crear una pila con tamaño adecuado
        pila = Stack(len(cadena_filtrada))

        # Apilar cada carácter de la cadena filtrada
        for char in cadena_filtrada:
            pila.push(char)

        # Comprobar si la cadena es un palíndromo
        for char in cadena_filtrada:
            if char != pila.pop():
                return False
        
        return True
