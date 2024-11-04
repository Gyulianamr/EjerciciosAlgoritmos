class Pila(object):
    def __init__(self, initialSize):  # inicializa el constructor 
        self.__a = [None] * initialSize # atributo privado, determina el tama;o fijo                                
        self.__nItems = 0 # cuenta los elementos, ayudara a determinar el tama;o


    def push(self, item): # """Agrega un elemento a la pila."""
        if self.__nItems < len(self.__a): #verifica si hay espacio disponible
            self.__a[self.__nItems] = item #ejemplo  self.__a[0] = item
            self.__nItems += 1

    def empty(self): #"""Verifica si la pila está vacía."""
        return self.__nItems == 0

    def peek(self):#"""Devuelve el último elemento agregado a la pila sin eliminarlo."""
        if self.empty():   #si el objeto vacio
            raise IndexError("peek from empty stack") 
        return self.__a[self.__nItems - 1] #devuelve el ultimo elemento agregado a la pila

    def size(self): # """Devuelve el número de elementos en la pila."""
        return self.__nItems

    def pop(self): # """Elimina y devuelve el último elemento agregado a la pila."""
        if self.empty():
            raise IndexError("pop from empty stack")
        self.__nItems -= 1 #el ultimo puesto
        return self.__a[self.__nItems]   #y devuelve el valor 

    def __str__(self): # """Devuelve una representación en cadena de la pila."""
        return str(self.__a[:self.__nItems])

    def contar_sumar_pares_impares(self):
        suma_pares = 0
        suma_impares = 0
        conteo_pares = 0
        conteo_impares = 0

        for i in range(self.__nItems):
            if self.__a[i] % 2 == 0:
                suma_pares += self.__a[i]
                conteo_pares += 1
            else:
                suma_impares += self.__a[i]
                conteo_impares += 1

        promedio_pares = suma_pares / conteo_pares if conteo_pares > 0 else 0
        promedio_impares = suma_impares / conteo_impares if conteo_impares > 0 else 0

        return {
            "suma_pares": suma_pares,
            "promedio_pares": promedio_pares,
            "conteo_pares": conteo_pares,
            "suma_impares": suma_impares,
            "promedio_impares": promedio_impares,
            "conteo_impares": conteo_impares
        }


