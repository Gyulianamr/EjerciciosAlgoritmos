def identity(x):  # La función identidad
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, growthFactor, key=identity):  # Constructor
        self.__a = [None] * initialSize  # El arreglo almacenado como una lista
        self.__nItems = 0  # No hay elementos en el arreglo inicialmente
        self.__key = key  # Función clave que obtiene la clave del registro
        self.__growthFactor = growthFactor  # Factor de crecimiento

    def __len__(self):  # Método especial para la función len()
        return self.__nItems  # Devuelve el número de elementos
    
    def find(self, key):
        # Este método encuentra el índice de un registro con la clave dada
        for index, record in enumerate(self.__a):
            if self.__key(record) == key:
                return index
        return -1  # Devuelve -1 si la clave no se encuentra

    def get(self, n):  # Devuelve el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]  # Solo devuelve el elemento si está dentro de los límites
        raise IndexError("Índice " + str(n) + " está fuera de rango")

    def traverse(self, function=print):  # Recorre todos los elementos
        # y aplica una función
        for j in range(self.__nItems):  
            function(self.__a[j])

    def insert(self, record):  # Inserta un registro manteniendo el orden
        if self.__nItems >= len(self.__a):  # Verifica si el arreglo está lleno
            raise Exception("El arreglo está lleno")
        
        # Encuentra la posición para insertar el nuevo registro
        position = 0
        while (position < self.__nItems and
               self.__key(self.__a[position]) < self.__key(record)):
            position += 1
        
        # Desplaza elementos para hacer espacio para el nuevo registro
        for j in range(self.__nItems, position, -1):
            self.__a[j] = self.__a[j - 1]
        
        # Inserta el nuevo registro
        self.__a[position] = record
        self.__nItems += 1  # Incrementa el conteo de elementos
#2.5
    def merge(self, other):  # Método para combinar con otro OrderedRecordArray
        if not isinstance(other, OrderedRecordArray):
            raise TypeError("El argumento debe ser una instancia de OrderedRecordArray.")
        if self.__key != other.__key:  # Verifica si las funciones clave son idénticas
            raise ValueError("Las funciones clave deben ser idénticas para combinar.")

        merged_size = self.__nItems + other.__nItems  # Crea una nueva lista suficientemente grande para contener ambos arreglos
        if merged_size > len(self.__a):  
            self.__a.extend([None] * (merged_size - len(self.__a)))

        merged_array = [None] * merged_size

        # Índices para los arreglos
        i = j = k = 0

        # Combina ambas listas en orden
        while i < self.__nItems and j < other.__nItems:
            if self.__key(self.__a[i]) <= self.__key(other.__a[j]):
                merged_array[k] = self.__a[i]
                i += 1
            else:
                merged_array[k] = other.__a[j]
                j += 1
            k += 1

        # Agrega cualquier elemento restante de self
        while i < self.__nItems:
            merged_array[k] = self.__a[i]
            i += 1
            k += 1

        # Agrega cualquier elemento restante de other
        while j < other.__nItems:
            merged_array[k] = other.__a[j]
            j += 1
            k += 1

        # Actualiza el arreglo actual con el nuevo contenido combinado
        self.__a = merged_array
        self.__nItems = merged_size  # Actualiza el conteo de elementos

    def __str__(self):  # Método especial para la función str()
        ans = "["  # Rodea con corchetes cuadrados
        for i in range(self.__nItems):  # Recorre los elementos
            if i > 0:  # Excepto junto al corchete izquierdo,
                ans += ", "  # separa elementos con una coma
            ans += str(self.__a[i])  # Agrega la representación en forma de cadena del elemento
        ans += "]"  # Cierra con el corchete derecho
        return ans
   #2.6 
    def remove(self, record):  # Método para eliminar registros
        index = 0
        found = False
        while index < self.__nItems:
            if self.__key(self.__a[index]) == self.__key(record):
                found = True
                # Desplazar elementos hacia la izquierda para eliminar el registro
                for j in range(index, self.__nItems - 1):
                    self.__a[j] = self.__a[j + 1]
                self.__a[self.__nItems - 1] = None  # Limpiar la última posición
                self.__nItems -= 1  # Decrementar el conteo de elementos
                break  # Sale del bucle si solo necesitas eliminar la primera ocurrencia
            else:
                index += 1  # Solo avanzar si no se eliminó un elemento

        return found  # Devuelve si se encontró y eliminó algún elemento
#2.7
    def __resize(self):
        # Redimensiona el arreglo
        newSize = self.__maxSize * self.__growthFactor
        self.__a.extend([None] * (newSize - self.__maxSize))  # Aumenta la capacidad
        self.__maxSize = newSize  # Actualiza el tamaño máximo
