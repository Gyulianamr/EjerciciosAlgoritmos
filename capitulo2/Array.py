import random
class Array(object):
    def __init__(self, initialSize): 
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):    
        return self.__nItems

    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value

    def insert(self, item): 
        self.__a[self.__nItems] = item 
        self.__nItems += 1

    def find(self, item): 
        for j in range(self.__nItems): 
            if self.__a[j] == item: 
                return j 
        return -1

    def search(self, item): 
        return self.get(self.find(item))

    def delete(self, item): 
        for j in range(self.__nItems): 
            if self.__a[j] == item: 
                self.__nItems -= 1 
                for k in range(j, self.__nItems): 
                    self.__a[k] = self.__a[k+1] 
                return True
        return False

    def traverse(self, function=print): 
        for j in range(self.__nItems):
            function(self.__a[j])
#2.1
# añada un método llamado getMaxNum() que devuelve el valor del número más
#  alto de la matriz, o None si la matriz no tiene números.
#  obtener numero maximo

    def getMaxNum(self):
        max_num = None
        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int, float)):
                if max_num is None or self.__a[i] > max_num:
                    max_num = self.__a[i]
        return max_num
#2.2
#el elemento con el valor numérico más alto no solo
#  sea devuelto por el método
#  sino que también se elimine de la matriz. 
# Llame al método deleteMaxNum().
    def deleteMaxNum(self):
        max_num = None  #inicia variable vacia 
        max_index = -1   
        for i in range(self.__nItems): 
            item = self.__a[i] 
            if isinstance(item, (int, float)):
                if max_num is None or item > max_num:
                    max_num = item
                    max_index = i
        
        if max_index != -1: #que sea diferente
            # Eliminar el elemento con el valor más alto
            for j in range(max_index, self.__nItems - 1): #Este bucle desplaza los elementos hacia la izquierda para cubrir el espacio dejado por el elemento que se va a eliminar.
                self.__a[j] = self.__a[j + 1]
            self.__nItems -= 1
            self.__a[self.__nItems] = None  # Limpiar el último elemento
        
        return max_num

#2.4
#set diferencia los conjuntos 
    def removeDupes(self):
        unique_items = set()
        new_index = 0  # Índice para almacenar elementos únicos

        # Recorrer la matriz y agregar elementos únicos al conjunto
        for i in range(self.__nItems):
            if self.__a[i] not in unique_items:  # Asegúrate de que sea self.__a
                unique_items.add(self.__a[i])
                self.__a[new_index] = self.__a[i]
                new_index += 1

        self.__nItems = new_index  # Actualiza el número de elementos
        for i in range(new_index, len(self.__a)):
            self.__a[i] = None  # Limpia los elementos restantes

#ejercicios hecho en clase
    def getPromedio(self):
        prom= 0
        suma= 0
        contador=0

        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int,float)):
                contador += 1
                suma +=self.__a[i]
        
            if contador>0:
                prom=suma/contador

        return prom
    
    def cuentapares(self, tipo):
        pares = 0
        impares = 0
        num= []
        if tipo == 0:
            for i in range(self.__nItems):
                if isinstance(self.__a[i], int):
                    if self.__a[i] % 2 == 0:
                        pares += 1  # Aumentar el contador de pares
                        num.append(self.__a[i])
            return pares , num
        elif tipo == 1:
            for i in range(self.__nItems):
                if isinstance(self.__a[i], int):
                    if self.__a[i] % 2 == 1:
                        impares += 1  # Aumentar el contador de impares
                        num.append(self.__a[i])
            return impares , num

                  
    def imprimenonumeros(self):
        nonum = []
        for i in range(self.__nItems):
            if isinstance(self.__a[i], str):
                nonum.append(self.__a[i])  # Añadir el elemento a la lista nonum
        return nonum
    
   