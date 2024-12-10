#6.	Implementación Básica de una Pila Crea una clase Pila que implemente las operaciones básicas: push, pop y peek. Prueba la clase añadiendo y quitando elementos.
#
class pila():

    def __init__(self, tam, elem):
        self.__tam=tam
        self.__elem=elem

    def push(self, elem):
        if len(self.__elem)< self.__tam:
          self.__elem.append(elem)

        else:
            print("la pila esta llena")

    def __str__(self):
        return str(self.__elem)


    def pop(self):
        if self.__elem:
            elem=self.__elem[-1] 
            self.__elem = self.__elem[:-1]
            return elem
        else:
            print("La pila está vacía")
            return None
        
    def peek(self):
        if self.__elem:
            elem=self.__elem[-1]
            return elem
        else:
            print("la pila esta vacia")
            return None
        

Pila = pila(5, [])
Pila.push(10)
Pila.push(20)
Pila.push(5)
Pila.push(3)
Pila.push(5)
Pila.push(4) #no entra a la lista
print(Pila)  
print("Elemento removido:", Pila.pop()) 
print(Pila)  

print("Elemento removido:", Pila.pop()) 
print(Pila)  #

print("Elemento ",Pila.peek())